import asyncio
import logging
from pprint import pprint
from typing import TypeVar, Union

import aiohttp
from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.config import settings
from app.db import base  # noqa: F401

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


T = TypeVar('T')

DOWNLOAD_POKEMONS_ON_INIT = True


def using_context(context_manager):
    async def do(coroutine):
        async with context_manager:
            return await coroutine

    return do


async def download_pokemon_by_id(session: aiohttp.ClientSession,
                                 pokemon_url: str,
                                 default: T = None) -> Union[schemas.Pokemon, T]:
    async with session.get(pokemon_url) as resp:
        try:
            resp_json = await resp.json()
            if resp_json['sprites']['front_default'] is None:
                return default
            pokemon = schemas.PokemonCreate(
                id=resp_json['id'],
                name=resp_json['name'],
                picture_url=resp_json['sprites']['front_default']
            )
            return pokemon
        except Exception:
            logging.error(f'download pokemon error {pokemon_url}', exc_info=True)
            return default


async def download_pokemon_database(db: Session, max_workers=15):
    semaphore = asyncio.Semaphore(max_workers)
    async with aiohttp.ClientSession() as session:
        async with session.get('https://pokeapi.co/api/v2/pokemon?limit=-1') as resp:
            pokemons_uris = await resp.json()
        pokemon_urls = (r['url'] for r in pokemons_uris['results'])
        tasks = (
            using_context(semaphore)(download_pokemon_by_id(session, p_url))
            for p_url in pokemon_urls
        )
        pokemons_info = filter(lambda x: x is not None, await asyncio.gather(*tasks))

        for pokemon_in in pokemons_info:
            db_object = crud.pokemon.get(db, pokemon_in.id)
            if db_object:
                crud.pokemon.update(db, obj_in=pokemon_in, db_obj=db_object)
            else:
                crud.pokemon.create(db, obj_in=pokemon_in)


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)

    user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    if not user:
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = crud.user.create(db, obj_in=user_in)  # noqa: F841

    if DOWNLOAD_POKEMONS_ON_INIT:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(download_pokemon_database(db))

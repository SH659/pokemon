from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.config import settings
from app.db import base  # noqa: F401

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28
import requests


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

    pokemons = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100')
    for pokemon_result in pokemons.json()['results']:
        pokemon_data = requests.get(pokemon_result['url']).json()
        pokemon_in = schemas.PokemonCreate(
            name=pokemon_data['name'],
            picture_url=pokemon_data['sprites']['front_default']
        )
        pokemon = crud.pokemon.create(db, obj_in=pokemon_in)  # noqa: F841

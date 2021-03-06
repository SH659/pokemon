from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Pokemon])
def read_pokemons(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve pokemons.
    """
    pokemons = crud.pokemon.get_multi(db, skip=skip, limit=limit)
    return pokemons


@router.get("/total_count")
def get_total_count(
    db: Session = Depends(deps.get_db),
) -> int:
    """
    Retrieve Pokemons Count
    """
    pokemons = crud.pokemon.get_total_count(db)
    return pokemons


@router.get("/{pokemon_id}", response_model=schemas.Pokemon)
def read_pokemon_by_id(
    pokemon_id: int,
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Retrieve pokemon by id.
    """
    pokemon = crud.pokemon.get(db, id=pokemon_id)
    return pokemon

import uuid
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas, models
from app.api import deps
from app.schemas import UserPokemonInDB

router = APIRouter()


@router.get("/user/{user_id}", response_model=List[schemas.UserPokemon])
def read_user_pokemons(
    user_id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve pokemons.
    """
    pokemons = crud.user_pokemon.get_multi_by_owner(db, owner_id=user_id)
    return pokemons


@router.get("/{user_pokemon}", response_model=List[schemas.UserPokemon])
def read_user_pokemon(
    user_pokemon_id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve pokemons.
    """
    pokemons = crud.user_pokemon.get(db, user_pokemon_id)
    return pokemons


@router.post("/", response_model=schemas.UserPokemon)
def create_user_pokemon(
    *,
    db: Session = Depends(deps.get_db),
    user_pokemon_in: schemas.UserPokemonCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new item.
    """

    if not crud.pokemon.get(db, user_pokemon_in.pokemon):
        raise HTTPException(status_code=404, detail="Pokemon not found")

    if not crud.user.get(db, user_pokemon_in.user):
        raise HTTPException(status_code=404, detail="User not found")

    if not crud.user.is_superuser(current_user) and (user_pokemon_in.user != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")

    obj_in = UserPokemonInDB(id=uuid.uuid4().hex, user=user_pokemon_in.user, pokemon=user_pokemon_in.pokemon)
    item = crud.user_pokemon.create(db, obj_in=obj_in)
    return item


@router.delete("/{id}", response_model=schemas.UserPokemon)
def delete_user_pokemon(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an item.
    """
    item = crud.user_pokemon.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    if not crud.user.is_superuser(current_user) and (item.user != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    item = crud.user_pokemon.remove(db=db, id=id)
    return item

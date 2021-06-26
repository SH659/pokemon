from typing import Optional

from pydantic import BaseModel


# Shared properties
class UserPokemonBase(BaseModel):
    user: int = None
    pokemon: int


# Properties to receive via API on creation
class UserPokemonCreate(BaseModel):
    user: int = None
    pokemon: int


# Properties to receive via API on update
class UserPokemonUpdate(UserPokemonBase):
    pass


class UserPokemonInDBBase(UserPokemonBase):
    id: str
    user: int
    pokemon: int

    class Config:
        orm_mode = True


# Additional properties to return via API
class UserPokemon(UserPokemonInDBBase):
    pass


# Additional properties stored in DB
class UserPokemonInDB(UserPokemonInDBBase):
    pass

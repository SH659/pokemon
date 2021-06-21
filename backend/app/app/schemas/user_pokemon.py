from pydantic import BaseModel


# Shared properties
class UserPokemonBase(BaseModel):
    owner_id: int
    pokemon_id: int


# Properties to receive via API on creation
class UserPokemonCreate(UserPokemonBase):
    pass


# Properties to receive via API on update
class UserPokemonUpdate(UserPokemonBase):
    pass


class UserPokemonInDBBase(UserPokemonBase):
    id: int
    owner_id: int
    pokemon_id: int

    class Config:
        orm_mode = True


# Additional properties to return via API
class UserPokemon(UserPokemonInDBBase):
    pass


# Additional properties stored in DB
class UserPokemonInDB(UserPokemonInDBBase):
    pass

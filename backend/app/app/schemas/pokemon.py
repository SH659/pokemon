from pydantic import BaseModel


# Shared properties
class PokemonBase(BaseModel):
    name: str
    picture_url: str


# Properties to receive via API on creation
class PokemonCreate(PokemonBase):
    pass


# Properties to receive via API on update
class PokemonUpdate(PokemonBase):
    pass


class PokemonInDBBase(PokemonBase):
    id: int
    name: str
    picture_url: str

    class Config:
        orm_mode = True


# Additional properties to return via API
class Pokemon(PokemonInDBBase):
    pass


# Additional properties stored in DB
class PokemonInDB(PokemonInDBBase):
    pass

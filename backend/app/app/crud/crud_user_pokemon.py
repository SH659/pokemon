from app.crud.base import CRUDBase
from app.models.pokemon import Pokemon
from app.models.user_pokemon import UserPokemon
from app.schemas.user_pokemon import UserPokemonCreate, UserPokemonUpdate


class CRUDUserPokemon(CRUDBase[UserPokemon, UserPokemonCreate, UserPokemonUpdate]):
    pass


user_pokemon = CRUDUserPokemon(Pokemon)

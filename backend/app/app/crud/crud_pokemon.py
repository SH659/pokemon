from app.crud.base import CRUDBase
from app.models.pokemon import Pokemon
from app.schemas.pokemon import PokemonCreate, PokemonUpdate


class CRUDPokemon(CRUDBase[Pokemon, PokemonCreate, PokemonUpdate]):
    pass


pokemon = CRUDPokemon(Pokemon)

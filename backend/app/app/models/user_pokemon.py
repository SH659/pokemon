from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401
    from .pokemon import Pokemon  # noqa: F401


class UserPokemon(Base):
    id = Column(Integer, primary_key=True, index=True)

    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="user_pokemons")

    pokemon_id = Column(Integer, ForeignKey("pokemon.id"))
    pokemon = relationship("Pokemon", back_populates="pokemons")

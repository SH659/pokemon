from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401
    from .pokemon import Pokemon  # noqa: F401


class UserPokemon(Base):
    __tablename__ = "user_pokemon"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    pokemon_id = Column(Integer, ForeignKey("pokemon.id"), primary_key=True)

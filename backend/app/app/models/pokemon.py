from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user_pokemon import UserPokemon  # noqa: F401


class Pokemon(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    picture_url = Column(String, index=False)
    users = relationship("User", secondary="user_pokemon", back_populates="pokemons")

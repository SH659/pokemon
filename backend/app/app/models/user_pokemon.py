from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401
    from .pokemon import Pokemon  # noqa: F401


class UserPokemon(Base):
    __tablename__ = "user_pokemon"

    id = Column(String, primary_key=True, index=True)
    user = Column(Integer, ForeignKey("user.id"), index=True)
    pokemon = Column(Integer, ForeignKey("pokemon.id"), index=True)

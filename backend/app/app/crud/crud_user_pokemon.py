from pprint import pprint
from typing import Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.user_pokemon import UserPokemon
from app.schemas.user_pokemon import UserPokemonCreate, UserPokemonUpdate


class CRUDUserPokemon(CRUDBase[UserPokemon, UserPokemonCreate, UserPokemonUpdate]):
    def create_with_owner_and_pokemon(self, db: Session, *, obj_in: UserPokemon, owner_id: int) -> UserPokemon:
        obj_in_data = jsonable_encoder(obj_in)
        pprint(obj_in)
        pprint(obj_in_data)
        db_obj = UserPokemon(**obj_in_data, user=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(self, db: Session, owner_id: int) -> Optional[UserPokemon]:
        return db.query(self.model).filter(UserPokemon.user == owner_id).all()


user_pokemon = CRUDUserPokemon(UserPokemon)

# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.item import Item  # noqa
from app.models.pokemon import Pokemon  # noqa
from app.models.user_pokemon import UserPokemon  # noqa
from app.models.user import User  # noqa

from fastapi import APIRouter

from app.api.api_v1.endpoints import items, login, users, utils, pokemons, user_pokemons

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(pokemons.router, prefix="/pokemons", tags=["pokemons"])
api_router.include_router(user_pokemons.router, prefix="/user_pokemons", tags=["user_pokemons"])

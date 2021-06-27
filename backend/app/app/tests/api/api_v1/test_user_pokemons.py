from typing import Dict

from fastapi.testclient import TestClient

from app.core.config import settings


def test_user_pokemons(client: TestClient, normal_user_token_headers: Dict[str, str]) -> None:
    me = client.get(
        f"{settings.API_V1_STR}/users/me", headers=normal_user_token_headers
    )

    user_id = me.json()['id']

    # get pokemons
    response = client.get(
        f"{settings.API_V1_STR}/user_pokemons/user/{user_id}", headers=normal_user_token_headers
    )
    assert response.status_code == 200
    user_pokemons = response.json()
    for pokemon in user_pokemons:
        assert 'id' in pokemon
        assert 'user' in pokemon
        assert 'pokemon' in pokemon

    # create
    json = {'user': user_id, 'pokemon': 1}
    response = client.post(
        f"{settings.API_V1_STR}/user_pokemons/", json=json, headers=normal_user_token_headers
    )
    assert response.status_code == 200
    created_pokemon = response.json()
    assert "id" in created_pokemon

    # get pokemons
    response = client.get(
        f"{settings.API_V1_STR}/user_pokemons/user/{user_id}", headers=normal_user_token_headers
    )
    assert response.status_code == 200
    user_pokemons = response.json()
    for pokemon in user_pokemons:
        assert 'id' in pokemon
        assert 'user' in pokemon
        assert 'pokemon' in pokemon

    # delete pokemons
    for pokemon in user_pokemons:
        response = client.delete(
            f"{settings.API_V1_STR}/user_pokemons/{pokemon['id']}", headers=normal_user_token_headers
        )
        assert response.status_code == 200

    # get pokemons
    response = client.get(
        f"{settings.API_V1_STR}/user_pokemons/user/{user_id}", headers=normal_user_token_headers
    )
    assert response.status_code == 200
    user_pokemons = response.json()
    assert len(user_pokemons) == 0

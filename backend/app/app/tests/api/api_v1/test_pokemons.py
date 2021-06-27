from fastapi.testclient import TestClient

from app.core.config import settings


def test_read_pokemons(client: TestClient) -> None:
    data = {"skip": 50, "limit": 50}
    response = client.get(
        f"{settings.API_V1_STR}/pokemons/", params=data,
    )
    assert response.status_code == 200
    content = response.json()

    assert len(content) == 50
    for pokemon in content:
        assert "id" in pokemon
        assert "name" in pokemon
        assert "picture_url" in pokemon


def test_read_pokemon_by_id(client: TestClient) -> None:
    pokemon_id = 1
    response = client.get(
        f"{settings.API_V1_STR}/pokemons/{pokemon_id}"
    )
    assert response.status_code == 200
    pokemon = response.json()

    assert "id" in pokemon
    assert "name" in pokemon
    assert "picture_url" in pokemon

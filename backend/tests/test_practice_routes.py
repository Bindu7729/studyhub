"""Unit and integration tests for practice sets and question routes."""
import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_all_practice_sets(async_client: AsyncClient):
    response = await async_client.get("/api/practice/sets")
    assert response.status_code == 200
    data = response.json()
    assert "sets" in data
    assert "count" in data
    assert isinstance(data["sets"], list)
    assert data["count"] > 0


@pytest.mark.asyncio
async def test_get_practice_sets_with_filter(async_client: AsyncClient):
    response = await async_client.get("/api/practice/sets?domain=dsa")
    assert response.status_code == 200
    data = response.json()
    assert data["count"] > 0
    for item in data["sets"]:
        assert "dsa" in item["domain"].lower()


@pytest.mark.asyncio
async def test_get_practice_sets_pagination(async_client: AsyncClient):
    response = await async_client.get("/api/practice/sets?limit=2&offset=0")
    assert response.status_code == 200
    data = response.json()
    assert len(data["sets"]) <= 2
    assert data["limit"] == 2
    assert data["offset"] == 0


@pytest.mark.asyncio
async def test_get_valid_practice_set(async_client: AsyncClient):
    # Fetch all sets first to obtain an existing ID
    list_res = await async_client.get("/api/practice/sets")
    sets = list_res.json()["sets"]
    first_id = sets[0]["id"]

    response = await async_client.get(f"/api/practice/sets/{first_id}")
    assert response.status_code == 200
    data = response.json()
    assert "set" in data
    assert "questions" in data
    assert data["set"]["id"] == first_id


@pytest.mark.asyncio
async def test_get_invalid_practice_set_404(async_client: AsyncClient):
    response = await async_client.get("/api/practice/sets/non-existent-set-id-999")
    assert response.status_code == 404
    data = response.json()
    assert data["success"] is False

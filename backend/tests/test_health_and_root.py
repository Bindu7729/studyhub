"""Unit tests for root and health check endpoints."""
import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_root_endpoint(async_client: AsyncClient):
    response = await async_client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "Welcome to StudyHub API" in data["message"]


@pytest.mark.asyncio
async def test_health_endpoint(async_client: AsyncClient):
    response = await async_client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["app"] == "StudyHub API"
    assert data["database"]["status"] == "connected"
    assert isinstance(data["database"]["latency_ms"], (int, float))
    assert "timestamp" in data


@pytest.mark.asyncio
async def test_not_found_endpoint(async_client: AsyncClient):
    response = await async_client.get("/api/non-existent-endpoint")
    assert response.status_code == 404
    data = response.json()
    assert data["success"] is False
    assert data["error"]["code"] == "HTTP_404"

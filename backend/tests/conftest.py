"""Shared fixtures for backend test suite."""
import pytest
import asyncio
from typing import AsyncGenerator
from httpx import AsyncClient, ASGITransport

from app.main import app
from app.core.database import AsyncSessionLocal
from app.core.security import UserStub


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    """Provides an asynchronous HTTP test client for FastAPI routes."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client


@pytest.fixture
async def db_session():
    """Provides a transactional database session for tests."""
    async with AsyncSessionLocal() as session:
        yield session


@pytest.fixture
def mock_user() -> UserStub:
    """Provides a standard authenticated test user stub."""
    return UserStub(
        uid="test-user-uuid-1234",
        email="teststudent@studyhub.dev",
        user_metadata={"name": "Test Student", "role": "student"},
    )

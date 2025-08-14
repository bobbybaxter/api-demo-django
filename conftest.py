"""
Conftest file for the API demo application.

This module contains the fixtures for the API demo application.
"""

import pytest
from rest_framework.test import APIClient
import users.store as store


@pytest.fixture
def api_client():
    """Provide a Django REST Framework API client for testing.

    Returns:
        APIClient: A test client for making API requests in tests.
    """
    return APIClient()


@pytest.fixture(autouse=True)
def fresh_users_store():
    """Ensure each test starts with a fresh, seeded users store.

    This fixture automatically runs for every test, resetting the in-memory
    users store to a deterministic state with 10 seeded users at the start
    of each test, and clearing it after the test completes.

    Yields:
        None: This fixture doesn't return a value, it just manages state.
    """
    # Ensures each test starts with the same 10 seeded users
    store.reset_and_seed()
    yield
    store.clear_users()

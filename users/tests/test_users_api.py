"""API tests for user endpoints.

This module contains integration tests for the user API endpoints,
testing the complete request-response cycle for user operations.
"""

# pylint: disable=import-error,unused-import
import pytest
from rest_framework import status


@pytest.mark.api
def test_list_users(api_client):
    """Test retrieving the list of all users.

    Verifies that the users list endpoint returns a 200 status
    and the expected number of seeded users.

    Args:
        api_client: Django REST framework API client fixture.
    """
    response = api_client.get("/users")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 10


@pytest.mark.api
def test_create_user(api_client):
    """Test creating a new user via API.

    Verifies that the user creation endpoint correctly processes
    valid user data and returns the created user with a 201 status.

    Args:
        api_client: Django REST framework API client fixture.
    """
    response = api_client.post(
        "/user",
        data={
            "firstName": "John",
            "lastName": "Doe",
            "email": "john.doe@example.com",
            "phone": "+1234567890",
        },
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["firstName"] == "John"
    assert response.json()["lastName"] == "Doe"
    assert response.json()["email"] == "john.doe@example.com"
    assert response.json()["phone"] == "+1234567890"

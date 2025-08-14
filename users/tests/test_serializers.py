"""Tests for user serializers.

This module contains unit tests for UserCreateSerializer and UserUpdateSerializer
to verify their validation behavior and data handling.
"""

# pylint: disable=import-error
from users.serializers import UserCreateSerializer, UserUpdateSerializer


def test_user_create_serializer_valid_data():
    """Test UserCreateSerializer with valid data.

    Verifies that the serializer correctly validates and processes
    valid user creation data.
    """
    serializer = UserCreateSerializer(
        data={
            "firstName": "John",
            "lastName": "Doe",
            "email": "john.doe@example.com",
            "phone": "+1234567890",
        }
    )
    assert serializer.is_valid()
    assert serializer.validated_data == {
        "firstName": "John",
        "lastName": "Doe",
        "email": "john.doe@example.com",
        "phone": "+1234567890",
    }


def test_user_update_serializer_valid_data():
    """Test UserUpdateSerializer with valid data.

    Verifies that the serializer correctly validates and processes
    valid user update data.
    """
    serializer = UserUpdateSerializer(
        data={
            "firstName": "John",
            "lastName": "Doe",
            "email": "john.doe@example.com",
            "phone": "+1234567890",
        }
    )
    assert serializer.is_valid()
    assert serializer.validated_data == {
        "firstName": "John",
        "lastName": "Doe",
        "email": "john.doe@example.com",
        "phone": "+1234567890",
    }

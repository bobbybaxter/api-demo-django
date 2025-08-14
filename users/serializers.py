"""Serializers for the users app.

This module contains serializers for creating and updating user data
using Django REST Framework.
"""

# pylint: disable=import-error
from rest_framework import serializers
from users import store


class UserCreateSerializer(serializers.Serializer):
    """Serializer for creating new users.

    Validates and creates new user instances with required firstName and email,
    and optional lastName and phone fields.
    """

    firstName = serializers.CharField(max_length=255)
    lastName = serializers.CharField(max_length=255, required=False)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=50, required=False)

    def create(self, validated_data):
        """Create method required by Serializer base class."""
        return store.create_user(validated_data)

    def update(self, instance, validated_data):
        """Update method required by Serializer base class."""
        # Not used for create serializer but required by base class
        raise NotImplementedError("Use UserUpdateSerializer for updates")


class UserUpdateSerializer(serializers.Serializer):
    """Serializer for updating existing users.

    Validates and updates user instances with optional firstName, lastName,
    email, and phone fields.
    """

    firstName = serializers.CharField(max_length=255, required=False)
    lastName = serializers.CharField(max_length=255, required=False)
    email = serializers.EmailField(required=False)
    phone = serializers.CharField(max_length=50, required=False)

    def create(self, validated_data):
        """Create method required by Serializer base class."""
        # Not used for update serializer but required by base class
        raise NotImplementedError("Use UserCreateSerializer for creation")

    def update(self, instance, validated_data):
        """Update method required by Serializer base class."""
        user_id = instance.get("id") if isinstance(instance, dict) else instance
        return store.update_user(user_id, validated_data)

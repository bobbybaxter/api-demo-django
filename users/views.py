"""API views for user management.

Provides REST API endpoints for user CRUD operations using Django REST Framework.
Includes views for listing users, creating users, and managing individual user details.
"""

# pylint: disable=import-error,too-few-public-methods
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .store import list_users, get_user, create_user, update_user, delete_user
from .serializers import UserCreateSerializer, UserUpdateSerializer


class UsersListView(APIView):
    """API view for listing all users."""

    def get(self, _request):
        """Retrieve all users.

        Returns:
            Response: JSON response containing list of all users.
        """
        return Response(list_users())


class UserCreateView(APIView):
    """API view for creating new users."""

    def post(self, request):
        """Create a new user.

        Args:
            request: HTTP request containing user data.

        Returns:
            Response: JSON response with created user data and 201 status.
        """
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_user(serializer.validated_data)
        return Response(user, status=status.HTTP_201_CREATED)


class UserDetailView(APIView):
    """API view for individual user operations (retrieve, update, delete)."""

    def get(self, _request, uid: str):
        """Retrieve a specific user by ID.

        Args:
            _request: HTTP request (unused).
            uid (str): User ID to retrieve.

        Returns:
            Response: JSON response with user data or 404 error.
        """
        user = get_user(uid)
        if not user:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
        return Response(user)

    def patch(self, request, uid: str):
        """Update a specific user by ID.

        Args:
            request: HTTP request containing updated user data.
            uid (str): User ID to update.

        Returns:
            Response: JSON response with updated user data or 404 error.
        """
        serializer = UserUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = update_user(uid, serializer.validated_data)
        if not user:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
        return Response(user)

    def delete(self, _request, uid: str):
        """Delete a specific user by ID.

        Args:
            _request: HTTP request (unused).
            uid (str): User ID to delete.

        Returns:
            Response: Empty response with 204 status or 404 error.
        """
        success = delete_user(uid)
        if not success:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
        return Response(status=status.HTTP_204_NO_CONTENT)

"""User store module for managing in-memory user data.

This module provides a simple in-memory store for user data with CRUD operations.
It includes functionality for seeding sample data and managing user lifecycle.
"""

from __future__ import annotations
from datetime import datetime, timezone
from uuid import uuid4


class _UserStore:
    """Internal user store class to encapsulate state."""

    def __init__(self):
        self.users: list[dict] = []
        self.seeded: bool = False

    def is_seeded(self) -> bool:
        """Check if the store has been seeded with initial data.

        Returns:
            bool: True if seeded, False otherwise.
        """
        return self.seeded

    def mark_seeded(self) -> None:
        """Mark the store as seeded."""
        self.seeded = True

    def clear(self) -> None:
        """Clear all users and reset seeded status."""
        self.users.clear()
        self.seeded = False


# Global store instance
_store = _UserStore()


def now_iso() -> str:
    """Get current UTC datetime as ISO format string.

    Returns:
        str: Current UTC datetime in ISO format.
    """
    return datetime.now(timezone.utc).isoformat()


def seed_once() -> None:
    """Seed the store with sample data if not already seeded."""
    if _store.is_seeded():
        return
    sample = [
        {
            "id": "4b1335f4-788b-4e8d-9ed5-04b99ce430a4",
            "firstName": "Emma",
            "lastName": "Johnson",
            "email": "emma.johnson@email.com",
            "phone": "+1-555-555-0123",
            "createdAt": "2023-01-15T08:30:00Z",
            "updatedAt": "2023-08-22T14:15:30Z",
        },
        {
            "id": "c27d2af0-b713-4092-a73b-024d1313233f",
            "firstName": "Liam",
            "lastName": "Williams",
            "email": "liam.williams@email.com",
            "phone": "+1-555-555-0456",
            "createdAt": "2023-02-03T12:45:15Z",
            "updatedAt": "2023-09-10T09:22:45Z",
        },
        {
            "id": "02ad7f8d-9a4d-4f00-b101-7744851880a2",
            "firstName": "Sophia",
            "lastName": "Brown",
            "email": "sophia.brown@email.com",
            "phone": "+1-555-555-0789",
            "createdAt": "2023-03-22T16:20:30Z",
            "updatedAt": "2023-07-18T11:33:20Z",
        },
        {
            "id": "a3fdef38-b254-4139-b93c-7e576baf9536",
            "firstName": "Noah",
            "lastName": "Davis",
            "email": "noah.davis@email.com",
            "phone": "+1-555-555-0321",
            "createdAt": "2023-04-07T10:15:45Z",
            "updatedAt": "2023-09-25T15:40:10Z",
        },
        {
            "id": "872afdbd-639e-495f-94f0-c008799f7914",
            "firstName": "Olivia",
            "lastName": "Miller",
            "email": "olivia.miller@email.com",
            "phone": "+1-555-555-0654",
            "createdAt": "2023-05-12T13:25:20Z",
            "updatedAt": "2023-08-30T16:55:35Z",
        },
        {
            "id": "3415a2d7-8f54-4e17-8966-55d1b0219ee4",
            "firstName": "Ethan",
            "lastName": "Wilson",
            "email": "ethan.wilson@email.com",
            "phone": "+1-555-555-0987",
            "createdAt": "2023-01-28T09:40:10Z",
            "updatedAt": "2023-06-14T12:28:50Z",
        },
        {
            "id": "a81f014a-efea-40d1-9a53-ff7f329b653c",
            "firstName": "Ava",
            "lastName": "Moore",
            "email": "ava.moore@email.com",
            "phone": "+1-555-555-0147",
            "createdAt": "2023-06-05T14:55:25Z",
            "updatedAt": "2023-09-12T10:18:40Z",
        },
        {
            "id": "3d4c5f82-909d-474c-95ee-0ab44fec640e",
            "firstName": "Mason",
            "lastName": "Taylor",
            "email": "mason.taylor@email.com",
            "phone": "+1-555-555-0258",
            "createdAt": "2023-07-19T11:30:50Z",
            "updatedAt": "2023-09-28T13:42:15Z",
        },
        {
            "id": "8b5fac60-b246-4601-81e7-a517ceea1c6d",
            "firstName": "Isabella",
            "lastName": "Anderson",
            "email": "isabella.anderson@email.com",
            "phone": "+1-555-555-0369",
            "createdAt": "2023-08-01T07:15:35Z",
            "updatedAt": "2023-09-05T08:50:25Z",
        },
        {
            "id": "798ada0b-a752-449c-9138-551a4850fb03",
            "firstName": "William",
            "lastName": "Thomas",
            "email": "william.thomas@email.com",
            "phone": "+1-555-555-0741",
            "createdAt": "2023-09-14T15:20:10Z",
            "updatedAt": "2023-09-20T17:35:55Z",
        },
    ]
    _store.users.extend(sample)
    _store.mark_seeded()


def list_users() -> list[dict]:
    """Get all users from the store.

    Returns:
        list[dict]: List of all user dictionaries.
    """
    return _store.users


def get_user(uid: str) -> dict | None:
    """Get a user by ID.

    Args:
        uid (str): The user ID to search for.

    Returns:
        dict | None: User dictionary if found, None otherwise.
    """
    return next((u for u in _store.users if u["id"] == uid), None)


def create_user(data: dict) -> dict:
    """Create a new user with the provided data.

    Args:
        data (dict): User data containing firstName, lastName, email, and phone.

    Returns:
        dict: The created user with generated ID and timestamps.
    """
    user = {
        "id": str(uuid4()),
        "firstName": data["firstName"],
        "lastName": data["lastName"],
        "email": data["email"],
        "phone": data["phone"],
        "createdAt": now_iso(),
        "updatedAt": now_iso(),
    }
    _store.users.append(user)
    return user


def update_user(uid: str, data: dict) -> dict | None:
    """Update an existing user with new data.

    Args:
        uid (str): The user ID to update.
        data (dict): New user data (firstName, lastName, email, phone).

    Returns:
        dict | None: Updated user dictionary if found, None otherwise.
    """
    user = get_user(uid)
    if not user:
        return None
    user.update(
        {
            key: value
            for key, value in data.items()
            if key in {"firstName", "lastName", "email", "phone"}
        }
    )
    user["updatedAt"] = now_iso()
    return user


def delete_user(uid: str) -> bool:
    """Delete a user by ID.

    Args:
        uid (str): The user ID to delete.

    Returns:
        bool: True if user was deleted, False if not found.
    """
    user_list = len(_store.users)
    new_user_list = [user for user in _store.users if user["id"] != uid]
    if len(new_user_list) == user_list:
        return False
    _store.users.clear()
    _store.users.extend(new_user_list)
    return True


def clear_users() -> None:
    """Clear all users from the store."""
    _store.clear()


def reset_and_seed() -> None:
    """Reset the store and reseed with initial data."""
    clear_users()
    seed_once()

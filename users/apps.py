"""Django app configuration for the users app.

Configures the users application and handles app initialization,
including seeding the user store with initial data.
"""

from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Configuration class for the users Django app.

    Handles app initialization and sets up the user store
    with initial seed data when the app is ready.
    """

    name = "users"

    def ready(self):
        """Initialize the app when Django starts.

        Seeds the user store with initial data. The import is done here
        to avoid circular imports and ensure Django is fully initialized.
        """
        from .store import seed_once  # pylint: disable=import-outside-toplevel

        seed_once()

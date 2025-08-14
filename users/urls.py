"""URL configuration for the users app.

Defines URL patterns for user-related API endpoints including
list, create, retrieve, update, and delete operations.
"""

from django.urls import path
from .views import UsersListView, UserDetailView, UserCreateView

urlpatterns = [
    path("users", UsersListView.as_view(), name="users-list"),
    path("user", UserCreateView.as_view(), name="user-create"),
    path("user/<str:uid>", UserDetailView.as_view(), name="user-detail"),
]

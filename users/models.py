"""
User models for the API demo application.

This module contains the User model which represents user data in the system.
"""

from django.db import models


class User(models.Model):
    """
    User model representing a user in the system.

    Attributes:
        firstName (CharField): User's first name
        lastName (CharField): User's last name
        email (EmailField): User's unique email address
        phone (CharField): User's phone number
        createdAt (DateTimeField): Timestamp when user was created
        updatedAt (DateTimeField): Timestamp when user was last updated
    """

    firstName = models.CharField(max_length=255, null=False, blank=False)
    lastName = models.CharField(max_length=255, null=False)
    email = models.EmailField(unique=True, null=False)
    phone = models.CharField(max_length=50, null=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

#!/bin/bash

# Run migrations (for Django admin and built-in apps)
python manage.py migrate

# Seed the internal user store
python manage.py shell -c "
from users.store import seed_once
seed_once()
print('User store seeded with sample data')
"

# Create superuser if it doesn't exist (for Django admin)
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    print('Superuser created: admin/admin')
else:
    print('Superuser already exists')
"

# Start the application
exec "$@"

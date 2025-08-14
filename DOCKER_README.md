# Docker Setup for Django API Demo

This project includes Docker configuration for both development and production environments. The application uses an in-memory store for user data, so no external database is required.

## Prerequisites

- Docker
- Docker Compose

## Development Setup

### Using Docker Compose (Recommended)

1. **Build and start the service:**

   ```bash
   docker-compose up --build
   ```

2. **Access the application:**

   - Django API: http://localhost:8000
   - Users API: http://localhost:8000/api/users/

3. **Admin access:**

   - Username: `admin`
   - Password: `admin`
   - URL: http://localhost:8000/admin/

4. **To run in detached mode:**

   ```bash
   docker-compose up -d
   ```

5. **To stop the service:**

   ```bash
   docker-compose down
   ```

### Using Docker directly

1. **Build the image:**

   ```bash
   docker build -t django-api-demo .
   ```

2. **Run the container:**
   ```bash
   docker run -p 8000:8000 django-api-demo
   ```

## Production Setup

1. **Use the production compose file:**

   ```bash
   docker-compose -f docker-compose.prod.yml up --build
   ```

2. **Environment variables for production:**
   Create a `.env` file with:
   ```
   DEBUG=0
   SECRET_KEY=your-production-secret-key
   DJANGO_ALLOWED_HOSTS=your-domain.com
   ```

## Useful Commands

### Django Management Commands in Docker

```bash
# Run migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser

# Collect static files
docker-compose exec web python manage.py collectstatic

# Django shell
docker-compose exec web python manage.py shell

# Run tests
docker-compose exec web python manage.py test
```

### User Store Operations

```bash
# Reset and reseed the user store
docker-compose exec web python manage.py shell -c "
from users.store import reset_and_seed
reset_and_seed()
print('User store reset and reseeded')
"

# Clear user store
docker-compose exec web python manage.py shell -c "
from users.store import clear_users
clear_users()
print('User store cleared')
"
```

### Docker Management

```bash
# View logs
docker-compose logs web

# View running containers
docker-compose ps

# Rebuild without cache
docker-compose build --no-cache

# Remove all containers and networks
docker-compose down --remove-orphans
```

## Troubleshooting

1. **Port already in use:**

   - Change the port mapping in `docker-compose.yml`
   - Or stop the service using the port: `sudo lsof -i :8000`

2. **Application startup issues:**

   - Check container logs: `docker-compose logs web`
   - Ensure the container started successfully: `docker-compose ps`

3. **Permission issues:**

   - The Dockerfile creates a non-root user for security
   - If you need to modify files, use: `docker-compose exec --user root web bash`

4. **Clean slate restart:**
   ```bash
   docker-compose down
   docker-compose build --no-cache
   docker-compose up
   ```

## File Structure

```
├── Dockerfile              # Main Docker image definition
├── docker-compose.yml      # Development environment
├── docker-compose.prod.yml # Production environment
├── entrypoint.sh           # Container initialization script
├── .dockerignore           # Files to exclude from Docker context
└── requirements.txt        # Python dependencies
```

## Notes

- The development setup uses volume mounting for hot reloading
- The production setup uses Gunicorn as the WSGI server
- User data is stored in-memory and will be reset when the container restarts
- The entrypoint script automatically seeds the user store with sample data and creates a Django admin superuser
- SQLite is used only for Django's built-in functionality (admin interface, sessions, etc.)

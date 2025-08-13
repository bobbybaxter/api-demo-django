# API Demo - Django

A Python-based RESTful API built with Django showcasing modern Python development practices and CRUD operations for user management.

## 🎯 Project Overview

This project is part of a multi-language series demonstrating equivalent server implementations across different technologies. This Django version showcases:

- **Django** framework with Django REST Framework
- RESTful API design patterns
- Input validation with Django serializers
- Comprehensive testing with Django's testing framework
- Docker containerization
- Modern Python development practices
- Clean architecture with Django's MVC pattern

## 🛠 Tech Stack

- **Runtime**: Python 3.8+
- **Framework**: Django 5.2.5
- **Database**: SQLite (default)
- **Validation**: Django serializers
- **Testing**: Django testing framework with coverage
- **Package Management**: pip with requirements.txt
- **Containerization**: Docker & Docker Compose

## 🚀 Quick Start

### Prerequisites

- Python 3.8+ and pip
- OR Docker and Docker Compose

### Option 1: Local Development

1. **Clone and navigate to the project**

   ```bash
   git clone <repository-url>
   cd api-demo-django
   ```

2. **Create and activate virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**

   ```bash
   python manage.py migrate
   ```

5. **Start the development server**

   ```bash
   python manage.py runserver
   ```

6. **Server is now running at** `http://localhost:8000`

### Option 2: Docker (Recommended for Testing)

1. **Clone and navigate to the project**

   ```bash
   git clone <repository-url>
   cd api-demo-django
   ```

2. **Start with Docker Compose**

   ```bash
   docker-compose up --build
   ```

3. **Server is now running at** `http://localhost:8000`

4. **Stop the container when done**
   ```bash
   docker-compose down
   ```

## 📋 API Endpoints

The API provides the following endpoints for user management:

### Base URL

```
http://localhost:8000
```

### Endpoints

| Method   | Endpoint    | Description       | Body Required |
| -------- | ----------- | ----------------- | ------------- |
| `GET`    | `/`         | Homepage          | No            |
| `GET`    | `/users`    | Get all users     | No            |
| `POST`   | `/user`     | Create a new user | Yes           |
| `GET`    | `/user/:id` | Get user by ID    | No            |
| `PATCH`  | `/user/:id` | Update user by ID | Yes           |
| `DELETE` | `/user/:id` | Delete user by ID | No            |

### User Data Structure

```json
{
	"id": "string (UUID)",
	"firstName": "string",
	"lastName": "string",
	"email": "string",
	"phone": "string",
	"createdAt": "string (ISO date)",
	"updatedAt": "string (ISO date)"
}
```

## 🧪 Testing the API

### Using curl

**1. Get all users:**

```bash
curl http://localhost:8000/users
```

**2. Get a specific user:**

```bash
curl http://localhost:8000/user/1
```

**3. Create a new user:**

```bash
curl -X POST http://localhost:8000/user \
  -H "Content-Type: application/json" \
  -d '{
    "firstName": "John",
    "lastName": "Doe",
    "email": "john.doe@example.com",
    "phone": "+1-555-555-1234"
  }'
```

**4. Update a user:**

```bash
curl -X PATCH http://localhost:8000/user/1 \
  -H "Content-Type: application/json" \
  -d '{
    "firstName": "Jane",
    "email": "jane.doe@example.com"
  }'
```

**5. Delete a user:**

```bash
curl -X DELETE http://localhost:8000/user/1
```

### Using a GUI Tool (Postman, Insomnia, etc.)

Import the following collection or manually create requests:

- **Base URL**: `http://localhost:8000`
- Set `Content-Type: application/json` for POST/PATCH requests
- Use the endpoints listed above

## 🏗 Project Structure

```
api-demo-django/
├── config/                   # Django project configuration
│   ├── __init__.py
│   ├── settings.py           # Django settings
│   ├── urls.py               # Main URL configuration
│   ├── wsgi.py               # WSGI configuration
│   └── asgi.py               # ASGI configuration
├── users/                    # Django app for user operations
│   ├── models.py             # User data models
│   ├── views.py              # API views/controllers
│   ├── serializers.py        # Data serialization and validation
│   ├── urls.py               # App-specific URL patterns
│   └── tests.py              # Unit tests
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── Dockerfile               # Docker configuration
└── docker-compose.yml       # Docker Compose setup
```

## 🧪 Running Tests

**Run all tests:**

```bash
python manage.py test
```

**Run tests with verbose output:**

```bash
python manage.py test --verbosity=2
```

**Run tests with coverage report:**

```bash
pip install coverage
coverage run --source='.' manage.py test
coverage report
coverage html  # Generate HTML coverage report
```

## 🔧 Development Scripts

```bash
python manage.py runserver        # Start development server
python manage.py migrate          # Apply database migrations
python manage.py makemigrations   # Create new migrations
python manage.py test             # Run tests
python manage.py shell            # Open Django shell
python manage.py createsuperuser  # Create admin user
python manage.py collectstatic    # Collect static files
```

## 🐳 Docker Commands

```bash
docker-compose build        # Build Docker image
docker-compose up           # Start container
docker-compose up --build   # Build and start container
docker-compose down         # Stop container
docker-compose logs         # View container logs
```

## ✨ Features Demonstrated

- **RESTful API Design**: Proper HTTP methods and status codes
- **Input Validation**: Joi schemas for request validation
- **Error Handling**: Centralized error handling middleware
- **Type Safety**: Full TypeScript implementation
- **Testing**: Comprehensive unit tests with high coverage
- **Code Quality**: ESLint and Prettier for consistent code style
- **Containerization**: Docker setup for consistent deployment
- **Logging**: Request logging middleware
- **Separation of Concerns**: Clean architecture with controllers, models, and routes

## 💾 Data Storage

This demo uses **in-memory storage** for simplicity. The application comes pre-loaded with 10 sample users. Data will persist during the application session but will reset when the server restarts.

## 🔄 Sample Data

The API comes with 10 pre-loaded users for testing. You can immediately test GET requests without needing to create data first.

## 📝 Notes for Reviewers

- **No Database**: Uses in-memory storage for demo simplicity
- **Environment**: Configured for development with detailed logging
- **Validation**: All inputs are validated using Joi schemas
- **Error Handling**: Proper HTTP status codes and error responses
- **Testing**: High test coverage with realistic test scenarios
- **Code Style**: Follows TypeScript and Express.js best practices

---

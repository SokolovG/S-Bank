# S-Bank

![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![Litestar](https://img.shields.io/badge/litestar-2.14.0-blue.svg)
![SQLAlchemy](https://img.shields.io/badge/sqlalchemy-2.0.37-blue.svg)
![Pydantic](https://img.shields.io/badge/pydantic-2.10.6-blue.svg)

S-Bank is a modern banking application built with Domain-Driven Design (DDD) architecture. The project implements core banking system functionality with emphasis on clean architecture and clear separation of business logic.

## 📋 Features

- **User Management**: Registration, authentication and profile management
- **Banking Accounts**: Creation and management of different account types
- **Payment Operations**: Card and balance management
- **Transactions**: Account transfers, deposits, withdrawals
- **Analytics**: Basic analysis of money flow

## 🧠 Architecture

The project follows Domain-Driven Design (DDD) principles with clear layer separation:

### 1. Domain Layer
- **Entities**: Domain entities with business logic
- **Value Objects**: Immutable objects without identity
- **Domain Events**: Events that occur in the domain
- **Repositories (interfaces)**: Interfaces for data access
- **Domain Services**: Services containing business logic

### 2. Application Layer
- **Services**: Coordination of business scenario execution
- **Event Handlers**: Domain event handlers

### 3. Infrastructure Layer
- **Repositories (implementations)**: Concrete repository implementations
- **Database**: DB models, settings, migrations
- **External Services**: Integrations with external services

### 4. Interfaces Layer
- **API**: REST API controllers, DTOs, schemas
- **CLI**: Command line interface

### Bounded Contexts
The project is divided into the following bounded contexts:
- **user_context**: Everything related to users and authorization
- **account_context**: Banking account management
- **payment_context**: Card and balance operations
- **transaction_context**: Transfers, deposits, withdrawals

## 🛠️ Technology Stack

### Backend
- **Python 3.12**
- **Litestar**: Modern asynchronous API framework
- **SQLAlchemy 2.0**: ORM for database operations
- **Pydantic 2.x**: Data validation and serialization
- **PostgreSQL**: Primary database
- **Alembic**: Migration management
- **JWT**: Authentication tokens

### DevOps
- **Docker & Docker Compose**: Containerization
- **GitHub Actions**: CI/CD

## 🚀 Installation and Setup

### Using Docker (recommended)

1. Clone the repository:
```bash
git clone https://github.com/yourusername/s-bank.git
cd s-bank
```

2. Create `.env` file with the following content:
```
# Database
POSTGRES_DB=s_bank
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/s_bank
```

3. Build and run containers:
```bash
docker-compose up --build
```

4. Access the application:
    - Backend API: http://localhost:8000
    - API Documentation: http://localhost:8000/schema/swagger
    - Admin Panel: http://localhost:8000/admin

### Local Development

1. Clone the repository
2. Create virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

3. Create `.env` file with local development settings
4. Run migrations:
```bash
alembic upgrade head
```

5. Start development server:
```bash
litestar --app src.main:app run --reload
```

## 🧪 Test Data

To populate the database with test data:
```bash
# With Docker
docker-compose exec backend python -m src.infrastructure.database.seeders.run_seeder

# Locally
python -m src.infrastructure.database.seeders.run_seeder
```

## 📝 API Documentation

API documentation is available at:
- Swagger UI: http://localhost:8000/schema/swagger
- ReDoc: http://localhost:8000/schema/redoc

## 💻 Development

### Creating Migrations

When changing database models:
```bash
# With Docker
docker-compose exec backend alembic revision --autogenerate -m "description"

# Locally
alembic revision --autogenerate -m "description"
```

### Running Tests
```bash
pytest
```

### Code Style
The project uses:
- Mypy for type checking
- Ruff for formatting and linting

```bash
# Linting and formatting
ruff src/

# Type checking
mypy src/
```

## 🤝 Contributing

We welcome contributions to the project! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is distributed under the MIT License.

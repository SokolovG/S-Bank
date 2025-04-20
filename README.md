# S-Bank

![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![Litestar](https://img.shields.io/badge/litestar-2.14.0-blue.svg)
![SQLAlchemy](https://img.shields.io/badge/sqlalchemy-2.0.37-blue.svg)
![Pydantic](https://img.shields.io/badge/pydantic-2.10.6-blue.svg)

S-Bank — это современное банковское приложение с архитектурой на основе Domain-Driven Design (DDD). Проект реализует основные функции банковской системы с акцентом на чистую архитектуру и четкое разделение бизнес-логики.

## 📋 Функциональность

- **Управление пользователями**: Регистрация, аутентификация и управление профилями
- **Банковские счета**: Создание и управление различными типами счетов
- **Платежные операции**: Управление картами и балансами
- **Транзакции**: Переводы между счетами, пополнения, снятия
- **Аналитика**: Базовый анализ движения средств

## 🧠 Архитектура

Проект следует принципам Domain-Driven Design (DDD) с четким разделением на слои:

### 1. Domain Layer
- **Entities**: Доменные сущности с бизнес-логикой
- **Value Objects**: Неизменяемые объекты без идентичности
- **Domain Events**: События, возникающие в домене
- **Repositories (interfaces)**: Интерфейсы для доступа к данным
- **Domain Services**: Сервисы, содержащие бизнес-логику

### 2. Application Layer
- **Services**: Координация выполнения бизнес-сценариев
- **Event Handlers**: Обработчики доменных событий

### 3. Infrastructure Layer
- **Repositories (implementations)**: Конкретные реализации репозиториев
- **Database**: Модели БД, настройки, миграции
- **External Services**: Интеграции с внешними сервисами

### 4. Interfaces Layer
- **API**: REST API контроллеры, DTO, схемы
- **CLI**: Интерфейс командной строки

### Bounded Contexts
Проект разделен на следующие ограниченные контексты:
- **user_context**: Всё, что связано с пользователями и авторизацией
- **account_context**: Управление банковскими счетами
- **payment_context**: Операции с картами и балансом
- **transaction_context**: Переводы, пополнения, снятия

## 🛠️ Технологический стек

### Backend
- **Python 3.12**
- **Litestar**: Современный асинхронный API-фреймворк
- **SQLAlchemy 2.0**: ORM для работы с базой данных
- **Pydantic 2.x**: Валидация данных и сериализация
- **PostgreSQL**: Основная база данных
- **Alembic**: Управление миграциями
- **JWT**: Токены для аутентификации

### DevOps
- **Docker & Docker Compose**: Контейнеризация
- **GitHub Actions**: CI/CD

## 🚀 Установка и запуск

### Использование Docker (рекомендуется)

1. Клонировать репозиторий:
```bash
git clone https://github.com/yourusername/s-bank.git
cd s-bank
```

2. Создать файл `.env` со следующим содержимым:
```
# Database
POSTGRES_DB=s_bank
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/s_bank
```

3. Собрать и запустить контейнеры:
```bash
docker-compose up --build
```

4. Доступ к приложению:
    - Backend API: http://localhost:8000
    - API Documentation: http://localhost:8000/schema/swagger
    - Admin Panel: http://localhost:8000/admin

### Локальная разработка

1. Клонировать репозиторий
2. Создать виртуальное окружение:
```bash
python -m venv .venv
source .venv/bin/activate  # На Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

3. Создать файл `.env` с настройками для локальной разработки
4. Запустить миграции:
```bash
alembic upgrade head
```

5. Запустить сервер разработки:
```bash
litestar --app src.main:app run --reload
```

## 🧪 Тестовые данные

Для заполнения базы данных тестовыми данными используйте:
```bash
# С Docker
docker-compose exec backend python -m src.infrastructure.database.seeders.run_seeder

# Локально
python -m src.infrastructure.database.seeders.run_seeder
```

## 📝 API Документация

API-документация доступна по адресам:
- Swagger UI: http://localhost:8000/schema/swagger
- ReDoc: http://localhost:8000/schema/redoc

## 💻 Разработка

### Создание миграций

При изменении моделей базы данных:
```bash
# С Docker
docker-compose exec backend alembic revision --autogenerate -m "description"

# Локально
alembic revision --autogenerate -m "description"
```

### Запуск тестов
```bash
pytest
```

### Код-стиль
Проект использует:
- Mypy для проверки типов
- Ruff для форматирования и линтинга

```bash
# Линтинг и форматирование
ruff src/

# Проверка типов
mypy src/
```

## 🤝 Участие в разработке

Мы приветствуем вклад в развитие проекта! Вот как вы можете помочь:

1. Форкните репозиторий
2. Создайте ветку для своей фичи (`git checkout -b feature/amazing-feature`)
3. Закоммитьте изменения (`git commit -m 'Add some amazing feature'`)
4. Отправьте изменения в ветку (`git push origin feature/amazing-feature`)
5. Откройте Pull Request

## 📜 Лицензия

Этот проект распространяется под лицензией MIT.

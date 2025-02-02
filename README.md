doc# DevEvents

**[English](#english) | [Русский](#russian)**

## English

### About DevEvents
DevEvents is a platform that aggregates and manages tech conferences and developer meetups. The service helps developers stay updated about upcoming tech events and allows organizers to promote their meetups.

### Key Features
- Browse upcoming tech events and conferences
- Track interesting events and set reminders
- Event organizers can create and manage their own events
- User profiles and event registration system
- Comments and discussions for each event

### Tech Stack
- Backend: Django + Django REST Framework
- Frontend: Svelte
- Database: PostgreSQL
- Containerization: Docker

### Installation and Setup
1. Clone the repository:
```bash
git clone https://github.com/yourusername/DevEvents.git
cd DevEvents
```

2. Start the containers:
```bash
docker-compose up --build
```

3. The application will be available at:
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000

### Project Structure
```
DevEvents/
├── backend/         # Django application
├── frontend/        # Svelte application
└── docker-compose.yaml
```

---

## Russian

### О проекте DevEvents
DevEvents - это платформа-агрегатор технологических конференций и встреч разработчиков. Сервис помогает разработчикам быть в курсе предстоящих технологических мероприятий и позволяет организаторам продвигать свои мероприятия.

### Основные возможности
- Просмотр предстоящих технологических мероприятий и конференций
- Отслеживание интересных событий и установка напоминаний
- Организаторы могут создавать и управлять своими мероприятиями
- Система профилей пользователей и регистрации на мероприятия
- Комментарии и обсуждения для каждого события

### Технологический стек
- Бэкенд: Django + Django REST Framework
- Фронтенд: Svelte
- База данных: PostgreSQL
- Контейнеризация: Docker

### Установка и запуск
1. Клонируйте репозиторий:
```bash
git clone https://github.com/yourusername/DevEvents.git
cd DevEvents
```

2. Запустите контейнеры:
```bash
docker-compose up --build
```

3. Приложение будет доступно по адресам:
- Фронтенд: http://localhost:5173
- API бэкенда: http://localhost:8000

### Структура проекта
```
DevEvents/
├── backend/         # Django приложение
├── frontend/        # Svelte приложение
└── docker-compose.yaml
```
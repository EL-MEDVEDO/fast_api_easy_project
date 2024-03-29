# Task Management API

Это API для управления задачами, реализованное с использованием FastAPI и асинхронной работы с базой данных через aiosqlite. Оно позволяет создавать, обновлять, получать и удалять задачи в асинхронной манере, обеспечивая высокую производительность и эффективность работы с данными.

## Особенности

- Асинхронное создание, чтение, обновление и удаление задач.
- Использование SQLite базы данных для хранения информации о задачах.
- Возможность фильтрации задач по их статусу выполнения.
- Включает примеры тестов для проверки функциональности API.

## Установка

Чтобы начать работу с API, клонируйте репозиторий и установите зависимости:

```bash
git clone <URL_репозитория>
cd <имя_клонированной_директории>
pip install fastapi uvicorn aiosqlite pytest httpx
```

## Запуск

uvicorn main:app --reload

## Использование
- POST /add_task/: Создать новую задачу.
- PUT /update_task/{task_id}: Обновить существующую задачу.
- GET /tasks/: Получить список всех задач.
- GET /tasks/{task_id}: Получить задачу по ID.
- DELETE /tasks/{task_id}: Удалить задачу по ID.

## Тестирование

Для запуска тестов используйте команду: pytest

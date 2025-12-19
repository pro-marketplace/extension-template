# Extension Name

## Описание
Краткое описание что делает расширение.

## Зависимости

### Python
```
fastapi
pydantic
```

### React
```
axios
```

## Backend

### Эндпоинты
- `POST /api/example` — описание

### Модели
- `ExampleModel` — описание

## Frontend

### Компоненты
- `ExampleComponent` — описание

### Хуки
- `useExample` — описание

## Интеграция

### 1. Backend
1. Скопировать файлы из `backend/` в `app/src/api/v1/routers/`
2. Добавить роутер в `app.py`
3. Запустить миграцию если есть

### 2. Frontend
1. Скопировать компоненты из `frontend/` в `app/components/`
2. Добавить импорты где нужно

### 3. Переменные окружения
```env
EXAMPLE_API_KEY=xxx
```

## Конфигурация

| Переменная | Описание | Обязательно |
|------------|----------|-------------|
| `EXAMPLE_API_KEY` | API ключ для сервиса | Да |

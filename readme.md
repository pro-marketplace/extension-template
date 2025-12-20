# Extension Template

Шаблон для создания расширений Airnold Marketplace.

## Структура

```
your-extension/
├── backend/
│   ├── example/
│   │   └── index.py         # основная функция
│   └── example-webhook/
│       └── index.py         # webhook (опционально)
├── frontend/
│   ├── ExampleComponent.tsx
│   └── useExample.ts
└── readme.md                 # инструкция для ассистента
```

## Backend

Каждая функция — папка с `index.py`.

```python
# backend/example/index.py
import os
import json

def handler(event: dict, context) -> dict:
    """Описание функции"""

    api_key = os.environ.get('EXAMPLE_API_KEY')

    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({'status': 'ok'})
    }
```

**Правила:**
- Python 3.11
- Точка входа: `handler(event, context)` в `index.py`
- Секреты через `os.environ`
- Типизация обязательна

## Frontend

React 18 компоненты и хуки.

```tsx
// frontend/ExampleComponent.tsx
interface Props {
  onSuccess: () => void;
}

export function ExampleComponent({ onSuccess }: Props) {
  return <button onClick={onSuccess}>Нажми</button>;
}
```

## readme.md — Инструкция для ассистента

Ассистент читает этот файл и интегрирует расширение в проект.

**Обязательные секции:**

### Секреты
Какие переменные окружения нужны.

### База данных
SQL для создания таблиц (если нужны).

### Backend
Что делает каждая функция, какие параметры принимает.

### Frontend
Как использовать компоненты, какие пропсы.

### Пример использования
Код интеграции в проект.

---

Пример готового расширения: [robokassa](https://github.com/pro-marketplace/robokassa)

## Как работает установка

1. Пользователь нажимает "Добавить" в маркетплейсе
2. `backend/*` копируется в проект
3. `frontend/*` копируется в проект
4. Ассистент получает `readme.md` и:
   - Просит добавить секреты
   - Создаёт таблицы в БД
   - Подключает компоненты где нужно

## Чеклист

- [ ] Backend функции в папках с `index.py`
- [ ] Frontend компоненты экспортируются
- [ ] readme.md описывает: секреты, БД, API, компоненты
- [ ] Нет захардкоженных ключей
- [ ] Протестировано

# Extension Template

Шаблон для создания расширений Airnold Marketplace.

## Структура репозитория

```
your-extension/
├── backend/
│   ├── example/
│   │   ├── index.py
│   │   └── requirements.txt
│   └── example-webhook/
│       ├── index.py
│       └── requirements.txt
├── frontend/
│   ├── ExampleComponent.tsx
│   └── useExample.ts
├── package.json              # зависимости frontend
└── readme.md
```

## Как писать readme.md

Ассистент читает `readme.md` и интегрирует расширение в проект.

README должен описывать **5 модальностей:**

---

## 1. Зависимости

Какие пакеты нужны для работы расширения.

**Backend (Python)** — указать в `requirements.txt` каждой функции:

```
pydantic>=2.0.0
requests>=2.28.0
```

**Frontend (npm)** — указать в `package.json` или в README:

```json
{
  "dependencies": {
    "axios": "^1.6.0"
  }
}
```

---

## 2. База данных

Какие таблицы нужно создать.

Пример описания:

> **Таблица orders**
> - `id` SERIAL PRIMARY KEY — ID заказа
> - `email` TEXT — Email клиента
> - `amount` INTEGER — Сумма в копейках
> - `status` TEXT — pending / paid / failed

SQL миграция:

```sql
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  email TEXT NOT NULL,
  amount INTEGER NOT NULL,
  status TEXT DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT NOW()
);
```

---

## 3. Облачные функции

Какие функции есть, что делают, какие параметры.

Пример описания:

> **example/**
>
> Создаёт заказ и возвращает URL для оплаты.
>
> Метод: `POST`
>
> Параметры: `{ "email": "...", "amount": 1000 }`
>
> Ответ: `{ "id": 123, "url": "https://..." }`

> **example-webhook/**
>
> Принимает уведомления от внешнего сервиса.
>
> Метод: `POST`
>
> Вызывается автоматически внешним сервисом.

---

## 4. Секреты

Какие переменные окружения нужны.

Пример описания:

| Переменная | Описание | Где взять |
|------------|----------|-----------|
| `EXAMPLE_API_KEY` | API ключ сервиса | Личный кабинет example.com |
| `EXAMPLE_SECRET` | Секретный ключ | Настройки → API |

---

## 5. S3 хранилище

Если расширение работает с файлами.

Пример описания:

> Расширение сохраняет файлы в S3:
> - `uploads/` — загруженные пользователем файлы
> - `generated/` — сгенерированные файлы
>
> CDN: `https://cdn.poehali.dev/projects/{id}/bucket/...`

---

## 6. Frontend компоненты

Описание компонентов и как их использовать.

Пример описания:

> **ExampleComponent**
>
> Кнопка для запуска действия.
>
> Пропсы:
> - `onSuccess: () => void` — колбэк при успехе
> - `onError: (error: Error) => void` — колбэк при ошибке

Пример использования:

```tsx
import { ExampleComponent } from './components/ExampleComponent';

<ExampleComponent
  onSuccess={() => alert('Готово!')}
  onError={(e) => console.error(e)}
/>
```

---

## Полный пример

Смотри [robokassa](https://github.com/pro-marketplace/robokassa) — реальное расширение.

---

## Как работает установка

1. Пользователь нажимает "Добавить"
2. `backend/*` копируется в проект
3. `frontend/*` копируется в проект
4. Ассистент получает `readme.md` и:
   - Устанавливает зависимости
   - Создаёт таблицы в БД
   - Просит добавить секреты
   - Настраивает S3 если нужно
   - Интегрирует компоненты

## Чеклист

- [ ] Backend функции в папках с `index.py`
- [ ] `requirements.txt` в каждой функции
- [ ] Frontend компоненты экспортируются
- [ ] `package.json` с зависимостями (если есть)
- [ ] readme.md описывает:
  - [ ] Зависимости (backend + frontend)
  - [ ] База данных (если есть)
  - [ ] Облачные функции
  - [ ] Секреты
  - [ ] S3 хранилище (если есть)
- [ ] Нет захардкоженных ключей

# Extension Template

Шаблон для создания расширений Airnold Marketplace.

## Структура репозитория

```
your-extension/
├── backend/
│   ├── example/
│   │   └── index.py
│   └── example-webhook/
│       └── index.py
├── frontend/
│   ├── ExampleComponent.tsx
│   └── useExample.ts
└── readme.md
```

## Как писать readme.md

Ассистент читает `readme.md` и интегрирует расширение в проект.

**README должен описывать 5 модальностей:**

---

### 1. База данных

Какие таблицы нужно создать.

```markdown
## База данных

### Таблица orders
| Поле | Тип | Описание |
|------|-----|----------|
| id | SERIAL PRIMARY KEY | ID заказа |
| email | TEXT | Email клиента |
| amount | INTEGER | Сумма в копейках |
| status | TEXT | pending / paid / failed |

SQL:
```sql
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  email TEXT NOT NULL,
  amount INTEGER NOT NULL,
  status TEXT DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT NOW()
);
```
```

---

### 2. Облачные функции

Какие функции есть, что делают, какие параметры.

```markdown
## Облачные функции

### example/
Создаёт что-то и возвращает результат.

**Метод:** POST

**Параметры:**
```json
{
  "email": "user@example.com",
  "amount": 1000
}
```

**Ответ:**
```json
{
  "id": 123,
  "url": "https://..."
}
```

### example-webhook/
Принимает уведомления от внешнего сервиса.

**Метод:** POST
**Вызывается:** автоматически внешним сервисом
```

---

### 3. Секреты

Какие переменные окружения нужны.

```markdown
## Секреты

| Переменная | Описание | Где взять |
|------------|----------|-----------|
| EXAMPLE_API_KEY | API ключ сервиса | Личный кабинет example.com |
| EXAMPLE_SECRET | Секретный ключ для подписей | Настройки → API |
```

---

### 4. S3 хранилище

Если расширение работает с файлами.

```markdown
## S3 хранилище

Расширение сохраняет файлы в S3:
- `uploads/` — загруженные пользователем файлы
- `generated/` — сгенерированные файлы

Доступ через CDN: `https://cdn.poehali.dev/projects/{id}/bucket/...`
```

---

### 5. Рекурентные задачи

Если нужны периодические задачи.

```markdown
## Рекурентные задачи

| Функция | Расписание | Описание |
|---------|------------|----------|
| example-cleanup/ | Каждый день в 03:00 | Удаляет старые записи |
| example-sync/ | Каждый час | Синхронизирует данные |
```

---

## Frontend компоненты

Описание компонентов и как их использовать.

```markdown
## Frontend

### ExampleComponent
Кнопка для запуска действия.

**Пропсы:**
| Проп | Тип | Описание |
|------|-----|----------|
| onSuccess | () => void | Колбэк при успехе |
| onError | (error: Error) => void | Колбэк при ошибке |

**Пример:**
```tsx
import { ExampleComponent } from './components/ExampleComponent';

<ExampleComponent
  onSuccess={() => alert('Готово!')}
  onError={(e) => console.error(e)}
/>
```

### useExample
Хук для работы с API.

```tsx
const { sendRequest, loading, error } = useExample();
await sendRequest({ message: 'test' });
```
```

---

## Полный пример readme.md

Смотри [robokassa](https://github.com/pro-marketplace/robokassa) — реальное расширение с описанием всех модальностей.

---

## Как работает установка

1. Пользователь нажимает "Добавить"
2. `backend/*` копируется в проект
3. `frontend/*` копируется в проект
4. Ассистент получает `readme.md` и:
   - Создаёт таблицы в БД
   - Просит добавить секреты
   - Подключает функции
   - Настраивает S3 если нужно
   - Создаёт cron задачи
   - Интегрирует компоненты

## Чеклист

- [ ] Backend функции в папках с `index.py`
- [ ] Frontend компоненты экспортируются
- [ ] readme.md описывает все используемые модальности:
  - [ ] База данных (если есть)
  - [ ] Облачные функции
  - [ ] Секреты
  - [ ] S3 хранилище (если есть)
  - [ ] Рекурентные задачи (если есть)
- [ ] Нет захардкоженных ключей
- [ ] Протестировано

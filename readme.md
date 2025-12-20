# Extension Template

Шаблон для создания расширений poehali.dev

## Быстрый старт

```
my-extension/
├── backend/
│   └── create-order/
│       ├── index.py          # твоя функция
│       └── requirements.txt  # зависимости
├── frontend/
│   └── OrderButton.tsx       # твой компонент
└── readme.md                 # инструкция для ассистента
```

Когда пользователь добавляет расширение, ассистент читает `readme.md` и делает всё остальное: ставит зависимости, создаёт таблицы, просит секреты.

---

## Что писать в readme.md

Просто опиши что нужно для работы расширения. Вот секции:

### Зависимости

**Python** — пиши в `requirements.txt` каждой функции. Деплоится автоматически.

**npm** — напиши в README, ассистент установит:
```
npm install axios date-fns
```

### База данных

Опиши какие таблицы нужны:

```sql
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  email TEXT NOT NULL,
  amount INTEGER NOT NULL,
  status TEXT DEFAULT 'pending'
);
```

### Функции

Опиши что делает каждая функция:

- **create-order/** — создаёт заказ, `POST { email, amount }` → `{ id, url }`
- **webhook/** — принимает уведомления от платёжки

### Секреты

Какие переменные окружения нужны:

| Переменная | Где взять |
|------------|-----------|
| `PAYMENT_API_KEY` | Личный кабинет платёжки |

### S3 (если нужно)

Если работаешь с файлами — опиши структуру папок:
- `uploads/` — загрузки пользователей
- `generated/` — сгенерированные файлы

### Компоненты

Как использовать твои React-компоненты:

```tsx
<OrderButton onSuccess={() => alert('Оплачено!')} />
```

---

## Пример

Смотри [robokassa](https://github.com/pro-marketplace/robokassa) — рабочее расширение.

---

## Чеклист перед публикацией

- [ ] Функции в `backend/*/index.py`
- [ ] `requirements.txt` рядом с каждой функцией
- [ ] readme.md описывает всё что нужно
- [ ] Нет захардкоженных ключей

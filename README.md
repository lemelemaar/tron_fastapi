# 🚀 Tron Wallet Info Microservice

Микросервис на FastAPI, который позволяет получать информацию о кошельке в сети Tron — баланс TRX, Bandwidth и Energy.

## 📦 Стек технологий

- **FastAPI** — API-фреймворк
- **SQLAlchemy** — ORM для работы с базой данных
- **SQLite** — СУБД
- **Tronpy** — библиотека для взаимодействия с Tron
- **Pytest** — тестирование

---

## 📌 Возможности

- `POST /wallet` — получить информацию по кошельку и сохранить в базу данных
- `GET /wallets` — получить список последних запросов с пагинацией

---

## 🛠 Установка и запуск

### 1. Клонируй репозиторий:

```bash
git clone https://github.com/lemelemaar/tron_fastapi.git
cd tron_fastapi
```
### 2. Установи зависимости:
```bash
pip install -r requirements.txt
```
### 3. Добавь .env файл:
```bash
TRON_API_KEY=your_api_key_from_trongrid
DATABASE_URL=sqlite:///./wallets.db
```
### 4. Запусти сервер:
```bash
uvicorn app.main:app --reload
```

## 🧪 Тесты
Для запуска тестов:
```bash
pytest
```

## 💬 Примечания

- Для доступа к `api.trongrid.io` необходим API-ключ (получить можно на [https://www.trongrid.io](https://www.trongrid.io))

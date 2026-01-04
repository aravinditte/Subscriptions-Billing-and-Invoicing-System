# Subscription Billing & Invoicing System

An enterprise-grade **Subscription Billing & Invoicing System** designed to demonstrate backend engineering skills expected by product and SaaS companies, particularly in **Japan**.

This project focuses on **correctness, reliability, and system design**, not just CRUD APIs.

---

## 🚀 Key Features

- Subscription lifecycle management (trial, active, past-due, cancelled)
- Recurring billing with background workers
- Invoice generation (immutable financial records)
- Mock payment gateway with success/failure simulation
- Retry handling for failed payments
- Audit logging for all critical actions
- Clean Domain-Driven Design (DDD) architecture
- Full test pyramid: unit, integration, and E2E tests
- Dockerized setup (API, worker, DB, Redis)

---

## 🏗️ Architecture Overview

```
API (FastAPI)
  ↓
Service Layer
  ↓
Domain Layer (Pure business logic)
  ↓
PostgreSQL
```

Background jobs are handled using **Celery + Redis**.

---

## 🧠 Why This Project Matters

This system models **real-world billing behavior**, including:

- State machines for subscriptions
- Idempotent billing jobs
- Immutable invoices for audit safety
- Separation of business logic from transport layers

These are key qualities evaluated in backend interviews.

---

## ⚙️ Tech Stack

- Backend: FastAPI (Python)
- Database: PostgreSQL
- ORM: SQLAlchemy + Alembic
- Background Jobs: Celery
- Cache/Broker: Redis
- Testing: Pytest
- Deployment: Docker & Docker Compose

---

## ▶️ How to Run

### 1. Setup environment

```bash
cp .env.example .env
```

### 2. Start services

```bash
make up
```

### 3. Run migrations

```bash
make migrate
```

### 4. Seed initial data

```bash
make seed
```

### 5. Create admin user

```bash
make admin
```

### 6. Access API docs

Open: http://localhost:8000/docs

---

## 🧪 Running Tests

```bash
make test
```

---

## 📂 Project Structure

```
app/
 ├── api/        # HTTP layer
 ├── core/       # Configuration, DB, logging
 ├── domain/     # Business logic
 ├── services/   # Use-case orchestration
 ├── tasks/      # Background jobs
 ├── utils/      # Helpers
 └── exceptions/ # Custom errors
```

---

## 💼 Interview Talking Points

- Why invoices are immutable
- How idempotency prevents double billing
- Why state machines are used for subscriptions
- Handling payment failures safely
- Importance of audit logs in financial systems

---

## 📌 Author

Built as a **portfolio-quality backend system** to demonstrate production-ready engineering skills.

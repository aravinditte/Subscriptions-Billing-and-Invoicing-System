# Subscription Billing & Invoicing System

An enterprise-grade backend system for managing subscriptions, recurring billing,
invoice generation, and payment processing.

This project is designed to demonstrate real-world backend engineering skills,
including domain-driven design, financial correctness, background processing,
and test discipline.

---

## Features

- Subscription lifecycle management
- Plan-based recurring billing
- Immutable invoice generation
- Payment processing (mock gateway)
- Automatic retries for failed payments
- Audit logging for all critical operations
- Background billing jobs using Celery
- Fully tested (unit, integration, end-to-end)

---

## Tech Stack

- Python 3.11
- FastAPI
- PostgreSQL
- SQLAlchemy + Alembic
- Celery + Redis
- Pytest
- Docker & Docker Compose

---

## Architecture Overview

- `domain/` – Pure business logic and entities
- `services/` – Use case orchestration
- `api/` – HTTP layer (FastAPI)
- `tasks/` – Background billing jobs
- `utils/` – Shared helpers
- `tests/` – Full test pyramid

This separation ensures correctness, maintainability, and scalability.

---

## Setup Instructions

### 1. Clone repository
```bash
git clone <repository-url>
cd subscription-billing-system

.PHONY: help up down restart logs migrate test seed admin

help:
	@echo "Available commands:"
	@echo "  make up        - Start all services"
	@echo "  make down      - Stop all services"
	@echo "  make restart   - Restart services"
	@echo "  make logs      - View logs"
	@echo "  make migrate   - Run database migrations"
	@echo "  make test      - Run test suite"
	@echo "  make seed      - Seed initial data"
	@echo "  make admin     - Create admin user"

up:
	docker compose up --build -d

down:
	docker compose down

restart:
	docker compose down && docker compose up --build -d

logs:
	docker compose logs -f

migrate:
	docker compose exec api alembic upgrade head

test:
	docker compose exec api pytest

seed:
	docker compose exec api python scripts/seed_data.py

admin:
	@read -p "Email: " email; \
	read -p "Name: " name; \
	docker compose exec api python scripts/create_admin.py $$email "$$name"

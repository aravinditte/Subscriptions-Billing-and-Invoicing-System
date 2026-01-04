"""
Seed initial application data.

This script is intended to be run once during initial setup
or in development environments to populate base plans.
"""

from decimal import Decimal

from app.core.database import SessionLocal
from app.domain.plans.repository import PlanRepository


def run():
    db = SessionLocal()
    try:
        repo = PlanRepository(db)

        existing_basic = repo.get(1)
        if existing_basic:
            print("Seed data already exists. Skipping.")
            return

        plans = [
            {
                "name": "Basic",
                "price": Decimal("19.99"),
                "currency": "USD",
                "interval": "monthly",
            },
            {
                "name": "Pro",
                "price": Decimal("49.99"),
                "currency": "USD",
                "interval": "monthly",
            },
            {
                "name": "Enterprise",
                "price": Decimal("199.99"),
                "currency": "USD",
                "interval": "monthly",
            },
        ]

        for plan in plans:
            repo.create(**plan)

        print("Seed data inserted successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    run()

"""
Create an initial administrative user.

This script is intentionally simple and explicit.
Authentication layers can later attach roles/permissions.
"""

import sys

from app.core.database import SessionLocal
from app.domain.users.repository import UserRepository


def run(email: str, name: str):
    db = SessionLocal()
    try:
        repo = UserRepository(db)

        existing = repo.get_by_email(email)
        if existing:
            print(f"Admin user already exists: {email}")
            return

        user = repo.create(email=email, name=name)
        print(f"Admin user created with ID: {user.id}")

    finally:
        db.close()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python create_admin.py <email> <name>")
        sys.exit(1)

    run(sys.argv[1], sys.argv[2])

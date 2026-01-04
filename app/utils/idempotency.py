import hashlib


def generate_idempotency_key(*parts: str) -> str:
    """
    Generates a deterministic idempotency key
    from provided input parts.
    """
    raw = "|".join(parts)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()

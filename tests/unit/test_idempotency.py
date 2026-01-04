from app.utils.idempotency import generate_idempotency_key


def test_idempotency_key_deterministic():
    key1 = generate_idempotency_key("sub_1", "2025-01")
    key2 = generate_idempotency_key("sub_1", "2025-01")

    assert key1 == key2

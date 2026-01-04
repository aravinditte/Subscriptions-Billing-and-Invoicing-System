from app.domain.subscriptions.state_machine import SubscriptionStateMachine
from app.core.constants import SubscriptionStatus


def test_valid_transition():
    assert SubscriptionStateMachine.can_transition(
        SubscriptionStatus.TRIAL,
        SubscriptionStatus.ACTIVE,
    )


def test_invalid_transition():
    assert not SubscriptionStateMachine.can_transition(
        SubscriptionStatus.CANCELLED,
        SubscriptionStatus.ACTIVE,
    )

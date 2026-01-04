from app.core.constants import SubscriptionStatus


class SubscriptionStateMachine:
    """
    Explicit state machine for subscription lifecycle.
    """

    ALLOWED_TRANSITIONS = {
        SubscriptionStatus.TRIAL: {SubscriptionStatus.ACTIVE},
        SubscriptionStatus.ACTIVE: {
            SubscriptionStatus.PAST_DUE,
            SubscriptionStatus.CANCELLED,
        },
        SubscriptionStatus.PAST_DUE: {
            SubscriptionStatus.ACTIVE,
            SubscriptionStatus.SUSPENDED,
        },
        SubscriptionStatus.SUSPENDED: {
            SubscriptionStatus.ACTIVE,
            SubscriptionStatus.CANCELLED,
        },
    }

    @classmethod
    def can_transition(cls, from_state: str, to_state: str) -> bool:
        return to_state in cls.ALLOWED_TRANSITIONS.get(from_state, set())

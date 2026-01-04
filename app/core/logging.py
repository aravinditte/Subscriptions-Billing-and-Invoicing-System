import logging
import sys


def configure_logging() -> None:
    """
    Configure structured application logging.

    Logging is intentionally simple and stdout-based
    for container compatibility.
    """

    logging.basicConfig(
        level=logging.INFO,
        format=(
            "%(asctime)s | %(levelname)s | "
            "%(name)s | %(message)s"
        ),
        handlers=[logging.StreamHandler(sys.stdout)],
    )

    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)

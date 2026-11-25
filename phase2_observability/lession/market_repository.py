
import logging

logger = logging.getLogger(__name__)


def fetch_market_data(product_id, request_id):
    logger.debug(
    "Fetching market data for product_id=%s",
    product_id,
    extra={"request_id": request_id}
)
    logger.info(
    "Repository received request",
    extra={"request_id": request_id}
)

    try:
        market_data = {
            "product_id": product_id,
            "market_size": 500000,
            "market_name": "Indian Pharma Market"
        }

        # Simulate a database failure
        raise ConnectionError("Database connection failed")

        return market_data

    except Exception:
        logger.exception(
            "Failed to fetch market data for product_id=%s",
            product_id,
            extra={"request_id": request_id}
        )
        raise

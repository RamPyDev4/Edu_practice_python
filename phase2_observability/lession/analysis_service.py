
import logging

from market_repository import fetch_market_data

logger = logging.getLogger(__name__)


def generate_analysis(product_id, request_id):
    logger.debug(
    "Starting market analysis",
    extra={"request_id": request_id}
)
    logger.info(
    "Analysis started",
    extra={"request_id": request_id}
    )
    market_data = fetch_market_data(product_id, request_id)

    logger.info("Market analysis generated successfully")
    

    return {
        "product_id": product_id,
        "market_size": market_data["market_size"],
        "status": "completed"
    }

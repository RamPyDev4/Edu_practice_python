
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    force=True
)

logger = logging.getLogger(__name__)


def fetch_market_data(product_id):
    logger.info("Fetching market data for product ID: %s", product_id)

    try:
        market_data = {
            "product_id": product_id,
            "market_size": 500000
        }

        return market_data

    except Exception:
        logger.exception("Failed to retrieve market data")
        raise


def fetch_competitor_data(product_id):
    logger.info("Fetching competitor data for product ID: %s", product_id)

    try:
        # Simulate database connection failure
        raise ConnectionError("Database connection failed")

    except ConnectionError:
        logger.exception("Failed to retrieve competitor data")
        return []

    except Exception:
        logger.exception("Unexpected error while retrieving competitor data")
        raise


def generate_market_analysis(product_id):
    logger.info("Market analysis started")
    logger.debug("Processing product ID: %s", product_id)

    try:
        market_data = fetch_market_data(product_id)

        competitors = fetch_competitor_data(product_id)

        if not competitors:
            logger.error("No competitor data available for product ID: %s", product_id)

        logger.info("Generating final market analysis")

        return {
            "market_data": market_data,
            "competitors": competitors,
            "status": "completed"
        }

    except Exception:
        logger.exception("Market analysis failed unexpectedly")

        return {
            "status": "failed",
            "message": "Unable to generate market analysis"
        }


# Simulate a backend request
result = generate_market_analysis(201)

print("Final result:", result)




import logging

logger = logging.getLogger(__name__)


def fetch_market_data(product_id):
    logger.debug("Fetching market data for product_id=%s", product_id)

    market_data = {
        "product_id": product_id,
        "market_size": 500000,
        "market_name": "Indian Pharma Market"
    }

    logger.info("Market data retrieved successfully")

    return market_data


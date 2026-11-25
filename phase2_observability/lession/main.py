
import logging
import json
import uuid

from analysis_service import generate_analysis


class JsonFormatter(logging.Formatter):

    def format(self, record):
        log_data = {
            
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "product_id": getattr(record, "product_id", None),
            "market_size": getattr(record, "market_size", None),
            "request_id": getattr(record, "request_id", None),
            "exception": (
                self.formatException(record.exc_info)
                if record.exc_info else None
            )
        }

        return json.dumps(log_data)


handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())

logging.basicConfig(
    level=logging.DEBUG,
    handlers=[handler],
    force=True
)

logger = logging.getLogger(__name__)


def main():
    logger.info("Application started")
    request_id = str(uuid.uuid4())

    logger.info(
        "Request started",
        extra={"request_id": request_id}
        )
    result = generate_analysis(501, request_id)

    logger.info("Final result: %s", result)


if __name__ == "__main__":
    main()
       
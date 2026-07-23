import logging

from config.settings import LOG_DIR, LOG_FILE

# Create logs directory if it doesn't exist
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)
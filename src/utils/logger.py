import logging
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "sdlc_tool.log")

def setup_logger():
    """Configure logging for the application."""
    
    # Ensure logs directory exists
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    return logging.getLogger(__name__)

logger = setup_logger()

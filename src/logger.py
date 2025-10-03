import logging
import os
from datetime import datetime

# Create logs directory if not exists
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Unique log file name based on timestamp
LOG_FILE = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
LOG_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Logging format
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"

# Configure logging
logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format=LOG_FORMAT,
    filemode="w"
)

# Get logger instance for other files
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Logging has started")
    print("Logger file ran successfully")

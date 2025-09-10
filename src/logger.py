import logging
import os
from datetime import datetime

# Create unique log file name using current datetime
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create "logs" folder inside your project if not exists
log_path = os.path.join(os.getcwd(), "logs")
os.makedirs(log_path, exist_ok=True)   # <-- fixed (was os.makedir)

# Full path for log file
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

# Logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,  # where to store logs
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    level=logging.INFO       # default logging level
)


# to check is logging.py file is working or not

# if __name__ == "__main__":
#     logging.info("Logging is Started")

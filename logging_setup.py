import logging
import os
from datetime import datetime

def setup_logging():
    # Define the log directory
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Define the log filename
    log_file = f"{log_dir}/fishing_game_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    
    # Define the format of log messages
    format_str = "%(asctime)s - %(levelname)s - %(message)s"

    # Set up the root logger
    logging.basicConfig(
        filename=log_file, 
        level=logging.INFO, 
        format=format_str
    )

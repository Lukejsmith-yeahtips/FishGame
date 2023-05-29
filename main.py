import logging
import logging.config
import os
from fishing_game import Game

# Set up logging configuration
LOG_CONFIG_PATH = "logging_config.ini"
if os.path.exists(LOG_CONFIG_PATH):
    logging.config.fileConfig(LOG_CONFIG_PATH)
else:
    logging.basicConfig(level=logging.DEBUG)

# Initialize logger
logger = logging.getLogger("Main")

def main():
    try:
        game = Game()
        game.run()

    except Exception as e:
        logger.exception("An error occurred in the main function.")

if __name__ == "__main__":
    main()

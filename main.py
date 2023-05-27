import logging  
# you also need to import the logging module
import pygame
from fishing_game import Game
from logging_setup import setup_logging
# Call the function to setup logging
setup_logging()

# Initialize pygame
pygame.init()

def main():
    """
    The main function creates an instance of the Game class from the fishing_game.py script.
    It then runs the game using the run() method of the Game class.
    """
    logging.info("Starting game...")  # log game start
    g = Game()  # Create the game instance
    g.run()  # Run the game
    logging.info("Game ended.")  # log game end

if __name__ == "__main__":
    # If this script is the entry point of the program, run the main function and then shut down Pygame
    main()
    pygame.quit()
    exit()

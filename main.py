import logging
import pygame
from fishing_game import Game
from logging_setup import setup_logging

# Call the function to set up logging
setup_logging()

# Initialize pygame
pygame.init()

def main():
    """
    The main function creates an instance of the Game class from the fishing_game.py script.
    It then runs the game using the game_loop() method of the Game class.
    """
    logging.info("Starting game...")  # Log game start
    g = Game()  # Create the game instance
    g.game_loop()  # Run the game loop
    logging.info("Game ended.")  # Log game end

if __name__ == "__main__":
    # If this script is the entry point of the program, run the main function and then shut down pygame
    main()
    pygame.quit()
    exit()

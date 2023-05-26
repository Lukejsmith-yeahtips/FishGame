# FishGame
Fishing Game is a Python game built using the Pygame library. The game allows players to control a fishing character to catch fish within a time limit. The score increases for each caught fish, and the level increases every 10 points. The game includes an intro screen, a main menu, and gameplay with fish animation and user input.

The game's file structure and functions are organized as follows:

main.py: This is the main entry point of the game. It imports necessary modules and initializes the Game class from fishing_game.py. It sets up logging using the setup_logging() function from logging_setup.py. It initializes Pygame and defines the main() function, which creates a game instance and starts the game loop.

fishing_game.py: This file contains the core implementation of the Fishing Game. It includes the Game class, which represents the game logic. The Game class handles game objects, game state, rendering, events, and gameplay elements. It has methods such as show_intro_screen(), show_main_menu(), render_menu(), wait_for_menu_selection(), start_game(), handle_events(), update(), render(), check_fish_creation(), check_level_up(), and quit_game().

fish.py: This file contains the FishAnimation class, which represents the fish animation and behavior. The FishAnimation class has methods such as __init__() for initializing the fish animation, update() for updating the fish's position and behavior, and draw() for drawing the fish on the screen.

fishing_man.py: This file contains the FishingManAnimation class, which represents the fishing man animation and behavior. The FishingManAnimation class has methods such as __init__() for initializing the fishing man animation, update() for updating the fishing man's position based on user input, and draw() for drawing the fishing man on the screen.

logging_setup.py: This file contains the function setup_logging() for setting up the logging configuration.

Image Files: The game may include additional image files such as "intro_screen.jpg" for the intro screen.

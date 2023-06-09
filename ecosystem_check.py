# ecosystem_check.py

import logging

# Configure logging
logger = logging.getLogger("FishingGame")

def check_ecosystem(fish_population):
    # Perform checks on the fish population and ecosystem
    for fish in fish_population:
        if fish.size < 10 or fish.size > 30:
            logger.error(f"Fish size ({fish.size}) out of range. Expected size between 10 and 30.")

        if fish.speed < 1 or fish.speed > 3:
            logger.error(f"Fish speed ({fish.speed}) out of range. Expected speed between 1 and 3.")

        if fish.behavior not in ["seek_food", "random_swim", "escape_predator"]:
            logger.error(f"Invalid fish behavior: {fish.behavior}. Expected 'seek_food', 'random_swim', or 'escape_predator'.")

    # Additional checks and rules for the ecosystem
    # ...

    # Return the result of the ecosystem check
    return True  # Or False if errors were found

# Usage in the Game class:

from ecosystem_check import check_ecosystem

class Game:
    # ...

    def update(self):
        for fish in self.fish:
            fish.update()

        if self.is_casting:
            self.hook_depth += 5
            if self.hook_depth >= SCREEN_HEIGHT:
                self.is_casting = False
                self.check_catch()

        # Check the ecosystem after each update
        if not check_ecosystem(self.fish):
            logger.warning("Errors found in the ecosystem. Check the detailed logging for more information.")

    # ...

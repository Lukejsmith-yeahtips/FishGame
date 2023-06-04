import pygame
import sys

# Import the necessary modules
from boat import Boat
from ecosystem import Ecosystem
from fisherman import Fisherman
from graphics import Graphics
from game_logging import configure_logging

class FishingGame:
    def __init__(self):
        # Initialize the game
        pygame.init()
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Fishing Game")
        self.clock = pygame.time.Clock()
        self.running = False
        self.ecosystem = None
        self.fisherman = None
        self.graphics = None

    def initialize(self):
        # Initialize the game components
        self.running = True
        self.ecosystem = Ecosystem(self.width, self.height)
        self.fisherman = Fisherman(Boat(self.width))
        self.graphics = Graphics(self.screen, self.width, self.height)

    def handle_events(self):
        # Handle game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.fisherman.move_left()
                elif event.key == pygame.K_RIGHT:
                    self.fisherman.move_right()
                elif event.key == pygame.K_SPACE:
                    self.fisherman.cast_line()

    def update(self):
        # Update the game state
        self.ecosystem.update()
        self.fisherman.update()
        self.check_collision()

    def check_collision(self):
        # Check for collisions between the fishing line and fish
        if self.fisherman.line_caught_fish():
            caught_fish = self.ecosystem.get_closest_fish(self.fisherman.line_position())
            if caught_fish:
                self.ecosystem.remove_fish(caught_fish)
                self.fisherman.catch_fish(caught_fish)

    def draw(self):
        # Draw the game elements
        self.graphics.draw_background()
        self.graphics.draw_water()
        self.graphics.draw_ecosystem(self.ecosystem)
        self.graphics.draw_fisherman(self.fisherman)
        self.graphics.draw_score(self.fisherman.score)
        pygame.display.flip()

    def start(self):
        # Start the game loop
        self.initialize()

        while self.running:
            self.handle_events()
            self.update()
            self.draw()

            self.clock.tick(60)

        pygame.quit()

def main():
    configure_logging()  # Configure logging
    game = FishingGame()
    game.start()

if __name__ == "__main__":
    main()

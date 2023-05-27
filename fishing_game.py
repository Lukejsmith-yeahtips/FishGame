import pygame
import random
import logging
from pygame.locals import *
from animations.fishing_man import FishingManAnimation
from animations.fish import FishAnimation
from logging_setup import setup_logging

# Setup logging
setup_logging()

# Game settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30
TIME_LIMIT = 30

# Initialize pygame
pygame.init()


class Game:
    def __init__(self):
        # Initialize game objects and variables
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Fishing Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)
        self.fishing_man = FishingManAnimation()
        self.fish_list = []
        self.score = 0
        self.level = 1
        self.time_left = TIME_LIMIT * FPS
        self.game_over = False
        self.running = True
        self.menu_selection = 1

    def show_intro_screen(self):
        # Display the intro screen
        intro_image = pygame.image.load("images/start.jpg")
        self.screen.blit(intro_image, (0, 0))
        pygame.display.flip()

        # Wait for a key press to continue
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()
                if event.type == pygame.KEYDOWN:
                    return

    def show_main_menu(self):
        # Display the main menu
        while True:
            self.render_menu()
            self.wait_for_menu_selection()

    def render_menu(self):
        # Render the menu options on the screen
        self.screen.fill((0, 0, 0))

        game_title = self.font.render("Fishing Game", True, (255, 255, 255))
        title_rect = game_title.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100)
        )
        self.screen.blit(game_title, title_rect)

        option1_color = (255, 255, 255) if self.menu_selection == 1 else (128, 128, 128)
        option2_color = (255, 255, 255) if self.menu_selection == 2 else (128, 128, 128)

        option1_text = self.font.render("1. Play The Game", True, option1_color)
        option1_rect = option1_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        )
        self.screen.blit(option1_text, option1_rect)

        option2_text = self.font.render("2. Exit", True, option2_color)
        option2_rect = option2_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
        )
        self.screen.blit(option2_text, option2_rect)

        pygame.display.flip()

    def wait_for_menu_selection(self):
        # Wait for menu option selection
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.start_game()
                    if event.key == pygame.K_2:
                        self.quit_game()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.menu_selection = max(self.menu_selection - 1, 1)
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.menu_selection = min(self.menu_selection + 1, 2)

            if keys[pygame.K_RETURN]:
                if self.menu_selection == 1:
                    self.start_game()
                elif self.menu_selection == 2:
                    self.quit_game()

            self.render_menu()

    def start_game(self):
        # Start the game
        self.show_intro_screen()
        self.game_loop()

    def game_loop(self):
        # Main game loop
        while self.running:
            self.handle_events()
            self.update()
            self.render()

            if self.game_over:
                self.show_game_over_screen()
                self.running = False

            self.clock.tick(FPS)

    def handle_events(self):
        # Handle game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.fishing_man.move_left()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.fishing_man.move_right()

    def update(self):
        # Update game state
        self.fishing_man.update()

    def render(self):
        # Render game objects on the screen
        self.screen.fill((0, 0, 0))
        self.fishing_man.draw(self.screen)
        pygame.display.flip()

    def show_game_over_screen(self):
        # Display the game over screen
        game_over_image = pygame.image.load("images/end.jpg")
        self.screen.blit(game_over_image, (0, 0))
        pygame.display.flip()
        pygame.time.wait(2000)

    def quit_game(self):
        # Quit the game
        pygame.quit()
        exit()


class FishingManAnimation:
    def __init__(self):
        logging.info("Initializing fishing man animation...")
        # Initialize fishing man animation variables

    def update(self):
        logging.debug("Updating fishing man position...")
        # Update fishing man animation logic

    def move_left(self):
        # Move fishing man to the left
        pass

    def move_right(self):
        # Move fishing man to the right
        pass

    def draw(self, screen):
        # Draw fishing man on the screen
        pass


def main():
    # Initialize pygame
    pygame.init()

    # Create game instance
    game = Game()

    # Show the main menu
    game.show_main_menu()


if __name__ == "__main__":
    main()

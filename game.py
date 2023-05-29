import pygame
import random
import math
import logging
import logging.config
import os
from renderer import Graphics
from fish_entity import Fish
from fisherman import Fisherman
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SKY_COLOR, WATER_COLOR, BOAT_COLOR, FISHERMAN_COLOR, FISH_COLOR, GAME_DURATION

# Set up logging configuration
LOG_CONFIG_PATH = "logging_config.ini"
if os.path.exists(LOG_CONFIG_PATH):
    logging.config.fileConfig(LOG_CONFIG_PATH)
else:
    logging.basicConfig(level=logging.DEBUG)

# Initialize logger
logger = logging.getLogger("FishingGame")


class Boat:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2 + 15

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def draw(self, screen):
        boat_rect = pygame.Rect(self.x - 50, self.y - 25, 100, 50)
        mast_rect = pygame.Rect(self.x - 5, self.y - 100, 10, 100)

        pygame.draw.rect(screen, BOAT_COLOR, boat_rect)
        pygame.draw.rect(screen, BOAT_COLOR, mast_rect)


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Fishing Game")
        self.clock = pygame.time.Clock()
        self.score = 0
        self.fish = []
        self.boat = Boat()
        self.fisherman = Fisherman(self.boat)
        self.is_casting = False
        self.remaining_time = GAME_DURATION * 1000  # in milliseconds

        self.renderer = Graphics(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Generate initial fish population
        for _ in range(10):
            self.fish.append(Fish())

    def run(self):
        try:
            running = True
            start_time = pygame.time.get_ticks()

            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.boat.move_left()
                        elif event.key == pygame.K_RIGHT:
                            self.boat.move_right()
                        elif event.key == pygame.K_UP:
                            self.fisherman.rotate_left()
                        elif event.key == pygame.K_DOWN:
                            self.fisherman.rotate_right()
                        elif event.key == pygame.K_SPACE:
                            self.cast_line()

                elapsed_time = pygame.time.get_ticks() - start_time
                self.remaining_time = max(GAME_DURATION * 1000 - elapsed_time, 0)

                self.update()
                self.draw()
                pygame.display.flip()
                self.clock.tick(60)

            return self.score

        except Exception as e:
            logger.exception("An error occurred during the game.")

        finally:
            pygame.quit()

    def cast_line(self):
        if not self.is_casting:
            self.is_casting = True

    def update(self):
        for fish in self.fish:
            fish.update()

        if self.is_casting:
            self.check_catch()

    def check_catch(self):
        if self.is_casting:
            for fish in self.fish:
                distance = math.sqrt((fish.x - self.boat.x) ** 2 + (fish.y - self.boat.y) ** 2)
                if distance <= fish.size:
                    self.score += 15
                    self.fish.remove(fish)

    def draw(self):
        self.screen.fill(SKY_COLOR)
        pygame.draw.rect(self.screen, WATER_COLOR, (0, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT // 2))

        self.renderer.draw_fish(self.screen, self.fish)

        self.boat.draw(self.screen)

        boat_x, boat_y = self.boat.x, self.boat.y
        rod_length = 100

        rod_x = boat_x + math.cos(math.radians(self.fisherman.angle)) * 50
        rod_y = boat_y - math.sin(math.radians(self.fisherman.angle)) * 50
        bait_x = rod_x + math.cos(math.radians(self.fisherman.angle)) * rod_length
        bait_y = rod_y - math.sin(math.radians(self.fisherman.angle)) * rod_length

        pygame.draw.line(self.screen, FISHERMAN_COLOR, (boat_x, boat_y), (rod_x, rod_y), 5)
        pygame.draw.line(self.screen, WATER_COLOR, (rod_x, rod_y), (bait_x, bait_y), 2)
        pygame.draw.circle(self.screen, (0, 0, 0), (int(bait_x), int(bait_y)), 5)
        pygame.draw.circle(self.screen, (255, 0, 0), (int(bait_x), int(bait_y)), 3)

        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        fish_caught_text = font.render(f"Fish Caught: {len(self.fish)}", True, (255, 255, 255))
        elapsed_time_text = font.render(f"Elapsed Time: {int(pygame.time.get_ticks() / 1000)}", True, (255, 255, 255))
        remaining_time_text = font.render(f"Remaining Time: {int(self.remaining_time / 1000)}", True, (255, 255, 255))

        self.screen.blit(score_text, (10, 10))
        self.screen.blit(fish_caught_text, (10, 50))
        self.screen.blit(elapsed_time_text, (10, 90))
        self.screen.blit(remaining_time_text, (10, 130))


if __name__ == "__main__":
    game = Game()
    game.run()

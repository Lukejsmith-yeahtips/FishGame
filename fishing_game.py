import pygame
import random
import math
import logging
import logging.config
import os

# Set up logging configuration
LOG_CONFIG_PATH = "logging_config.ini"
if os.path.exists(LOG_CONFIG_PATH):
    logging.config.fileConfig(LOG_CONFIG_PATH)
else:
    logging.basicConfig(level=logging.DEBUG)

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SKY_COLOR = (135, 206, 250)
WATER_COLOR = (0, 119, 190)
FISH_SIZE_RANGE = (10, 30)
FISH_SPEED_RANGE = (1, 3)
BOAT_COLOR = (139, 69, 19)
FISHERMAN_COLOR = (255, 228, 196)
FISH_COLOR = (0, 255, 0)
GAME_DURATION = 30  # in seconds

# Initialize logger
logger = logging.getLogger("FishingGame")

class Fish:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(SCREEN_HEIGHT // 2, SCREEN_HEIGHT)
        self.size = random.randint(*FISH_SIZE_RANGE)
        self.speed = random.uniform(*FISH_SPEED_RANGE)
        self.direction = random.uniform(0, 2 * math.pi)

    def update(self):
        self.move()
        self.wrap_around_screen()

    def move(self):
        self.x += math.cos(self.direction) * self.speed
        self.y += math.sin(self.direction) * self.speed

    def wrap_around_screen(self):
        if self.x < 0:
            self.x = SCREEN_WIDTH
        elif self.x > SCREEN_WIDTH:
            self.x = 0
        if self.y < 0:
            self.y = SCREEN_HEIGHT
        elif self.y > SCREEN_HEIGHT:
            self.y = 0

    def draw(self, screen):
        pygame.draw.circle(screen, FISH_COLOR, (int(self.x), int(self.y)), self.size)

class Boat:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2 + 15

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def draw(self, screen):
        pygame.draw.rect(screen, BOAT_COLOR, (self.x - 50, self.y - 25, 100, 50))

class Fisherman:
    def __init__(self, boat):
        self.boat = boat
        self.angle = 45

    def rotate_left(self):
        self.angle += 5

    def rotate_right(self):
        self.angle -= 5

    def draw(self, screen):
        boat_x, boat_y = self.boat.x, self.boat.y
        rod_length = 100

        rod_x = boat_x + math.cos(math.radians(self.angle)) * 50
        rod_y = boat_y - math.sin(math.radians(self.angle)) * 50
        bait_x = rod_x + math.cos(math.radians(self.angle)) * rod_length
        bait_y = rod_y - math.sin(math.radians(self.angle)) * rod_length

        pygame.draw.line(screen, FISHERMAN_COLOR, (boat_x, boat_y), (rod_x, rod_y), 5)
        pygame.draw.line(screen, WATER_COLOR, (rod_x, rod_y), (bait_x, bait_y), 2)
        pygame.draw.circle(screen, (0, 0, 0), (int(bait_x), int(bait_y)), 5)
        pygame.draw.circle(screen, (255, 0, 0), (int(bait_x), int(bait_y)), 3)

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
            if self.sound_enabled:
                self.fisherman.cast_line()

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

        for fish in self.fish:
            fish.draw(self.screen)

        self.boat.draw(self.screen)
        self.fisherman.draw(self.screen)

        # Display score, fish caught, elapsed time, and remaining time
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

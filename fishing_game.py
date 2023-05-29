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

# Sound effects
CAST_LINE_SOUND = pygame.mixer.Sound("cast_line.wav")
CATCH_FISH_SOUND = pygame.mixer.Sound("catch_fish.wav")

# Initialize logger
logger = logging.getLogger("FishingGame")

class Fish:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(SCREEN_HEIGHT // 2, SCREEN_HEIGHT)
        self.size = random.randint(*FISH_SIZE_RANGE)
        self.speed = random.uniform(*FISH_SPEED_RANGE)
        self.direction = random.uniform(0, 2 * math.pi)
        self.behavior = self.choose_behavior()

    def choose_behavior(self):
        behaviors = ["seek_food", "random_swim", "escape_predator"]
        probabilities = [0.6, 0.3, 0.1]
        return random.choices(behaviors, probabilities)[0]

    def update(self):
        if self.behavior == "seek_food":
            self.seek_food()
        elif self.behavior == "random_swim":
            self.random_swim()
        elif self.behavior == "escape_predator":
            self.escape_predator()

        self.wrap_around_screen()

    def seek_food(self):
        # Implement behavior to seek food based on real-world biology and math
        pass

    def random_swim(self):
        # Implement random swimming behavior
        self.direction += random.uniform(-0.1, 0.1)

    def escape_predator(self):
        # Implement behavior to escape predator based on real-world biology and math
        pass

    def wrap_around_screen(self):
        # Wrap fish around the screen if it goes off the edges
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
        self.y = SCREEN_HEIGHT - 100
        self.width = 100
        self.height = 50
        self.color = BOAT_COLOR

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x - self.width // 2, self.y, self.width, self.height))

class Fisherman:
    def __init__(self, boat):
        self.boat = boat
        self.color = FISHERMAN_COLOR

    def draw(self, screen):
        # Draw the fisherman and fishing rod based on boat position
        pygame.draw.line(screen, self.color, (self.boat.x, self.boat.y), (self.boat.x, self.boat.y - 50), 5)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Fishing Game")
        self.clock = pygame.time.Clock()
        self.fish = []
        self.boat = Boat()
        self.fisherman = Fisherman(self.boat)
        self.is_casting = False
        self.hook_depth = 0

        # Generate initial fish population
        for _ in range(10):
            self.fish.append(Fish())

    def run(self):
        try:
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.boat.move_left()
                        elif event.key == pygame.K_RIGHT:
                            self.boat.move_right()
                        elif event.key == pygame.K_SPACE:
                            self.cast_line()

                self.update()
                self.draw()
                pygame.display.flip()
                self.clock.tick(60)

        except Exception as e:
            logger.exception("An error occurred during the game.")

        finally:
            pygame.quit()

    def cast_line(self):
        if not self.is_casting:
            self.is_casting = True
            self.hook_depth = 0
            CAST_LINE_SOUND.play()

    def update(self):
        for fish in self.fish:
            fish.update()

        if self.is_casting:
            self.hook_depth += 5
            if self.hook_depth >= SCREEN_HEIGHT:
                self.is_casting = False
                self.check_catch()

    def check_catch(self):
        if self.is_casting:
            for fish in self.fish:
                distance = math.sqrt((fish.x - self.boat.x) ** 2 + (fish.y - self.hook_depth) ** 2)
                if distance <= fish.size:
                    self.fish.remove(fish)
                    CATCH_FISH_SOUND.play()

    def draw(self):
        self.screen.fill(SKY_COLOR)
        pygame.draw.rect(self.screen, WATER_COLOR, (0, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT // 2))

        for fish in self.fish:
            fish.draw(self.screen)

        self.boat.draw(self.screen)
        self.fisherman.draw(self.screen)

if __name__ == "__main__":
    game = Game()
    game.run()

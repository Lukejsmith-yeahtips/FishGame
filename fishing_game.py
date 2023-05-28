import pygame
import random
import math
from enum import Enum

# Game settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30
TIME_LIMIT = 30
WATER_HEIGHT = SCREEN_HEIGHT // 2 - 25
BLOCK_SIZE = 40
BLOCK_COLOR = (139, 69, 19)
BLUE_COLOR = (65, 105, 225)
FISH_COLOR = (255, 215, 0)
SCOREBOARD_HEIGHT = 40
FONT_SIZE = 24

# Define the Behavior enum
class Behavior(Enum):
    SEEK_FOOD = 1
    RANDOM_SWIM = 2
    ESCAPE_PREDATOR = 3
    REST = 4

class Game:
    def __init__(self):
        # Initialize game objects and variables
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Fishing Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, FONT_SIZE)
        self.scoreboard_font = pygame.font.SysFont(None, FONT_SIZE + 4)
        self.player = Player()
        self.fish_list = []
        self.score = 0
        self.level = 1
        self.time_left = TIME_LIMIT * FPS
        self.game_over = False
        self.running = True

    def render_scoreboard(self):
        # Display the scoreboard
        scoreboard_text = self.scoreboard_font.render(
            f"Score: {self.score}  Level: {self.level}  Time: {self.time_left // FPS}",
            True,
            (255, 255, 255),
        )
        scoreboard_rect = scoreboard_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCOREBOARD_HEIGHT // 2)
        )
        pygame.draw.rect(
            self.screen, BLOCK_COLOR, (0, 0, SCREEN_WIDTH, SCOREBOARD_HEIGHT)
        )
        self.screen.blit(scoreboard_text, scoreboard_rect)

    def spawn_fish(self):
        if len(self.fish_list) >= 10:
            return

        if random.random() < self.get_fish_spawn_rate():
            fish = Fish()
            self.fish_list.append(fish)

    def get_fish_spawn_rate(self):
        return 0.1 * self.level

    def update_fish(self):
        for fish in self.fish_list:
            fish.update()

            if fish.rect.colliderect(self.player.rect):
                self.fish_list.remove(fish)
                self.score += 1
                self.update_level()

    def update_level(self):
        self.level = min(self.score // 10 + 1, 10)

    def update(self):
        self.player.update()
        self.update_fish()
        self.spawn_fish()

        self.time_left -= 1
        if self.time_left == 0:
            self.game_over = True

    def render(self):
        self.screen.fill(BLOCK_COLOR)

        # Draw water
        pygame.draw.rect(
            self.screen,
            BLUE_COLOR,
            (0, SCOREBOARD_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT - SCOREBOARD_HEIGHT),
        )

        self.player.draw(self.screen)

        for fish in self.fish_list:
            fish.draw(self.screen)

        self.render_scoreboard()

        pygame.display.flip()

    def game_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.update()
            self.render()

            if self.game_over:
                self.running = False

            self.clock.tick(FPS)

        self.show_game_over_screen()

    def show_game_over_screen(self):
        game_over_text = self.font.render("Game Over", True, (255, 255, 255))
        game_over_rect = game_over_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        )
        self.screen.blit(game_over_text, game_over_rect)
        pygame.display.flip()
        pygame.time.wait(2000)

        self.quit_game()

    def quit_game(self):
        pygame.quit()
        exit()


class Player:
    def __init__(self):
        self.rect = pygame.Rect(
            (SCREEN_WIDTH - BLOCK_SIZE) // 2,
            SCREEN_HEIGHT - BLOCK_SIZE - SCOREBOARD_HEIGHT,
            BLOCK_SIZE,
            BLOCK_SIZE,
        )
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed

        # Keep the player within the screen bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)


class Fish:
    def __init__(self):
        self.rect = pygame.Rect(
            random.randint(0, SCREEN_WIDTH - BLOCK_SIZE),
            random.randint(SCOREBOARD_HEIGHT, SCREEN_HEIGHT - BLOCK_SIZE),
            BLOCK_SIZE,
            BLOCK_SIZE,
        )
        self.speed = random.uniform(1, 3)
        self.behavior = Behavior.RANDOM_SWIM
        self.hunger = 0
        self.hunger_threshold = random.randint(50, 100)

    def update(self):
        self.hunger += 1

        if self.hunger > self.hunger_threshold:
            self.behavior = Behavior.SEEK_FOOD
        elif random.random() < 0.01:  # Occasionally decide to rest
            self.behavior = Behavior.REST
        else:
            self.behavior = Behavior.RANDOM_SWIM

        if self.behavior == Behavior.SEEK_FOOD:
            self.seek_food()
        elif self.behavior == Behavior.RANDOM_SWIM:
            self.random_swim()

        self.rect.y += self.speed

        if self.rect.top > SCREEN_HEIGHT:
            self.reset()

    def seek_food(self):
        # Logic to seek food
        pass

    def random_swim(self):
        # Logic for random swimming
        pass

    def reset(self):
        self.rect.y = -self.rect.height
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.speed = random.uniform(1, 3)
        self.hunger = 0
        self.hunger_threshold = random.randint(50, 100)

    def draw(self, screen):
        pygame.draw.rect(screen, FISH_COLOR, self.rect)


def main():
    game = Game()
    game.game_loop()


if __name__ == "__main__":
    main()

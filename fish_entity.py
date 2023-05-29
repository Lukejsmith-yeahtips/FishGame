import random
import math
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FISH_SIZE_RANGE, FISH_SPEED_RANGE, FISH_COLOR

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

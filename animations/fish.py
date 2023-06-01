import pygame
import random
from animations.fish_animation import FishAnimation

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Fish sprites
FISH_SPRITES = [
    """
   ><{{('>
    """,
    """
   ><((('>
    """,
    """
   ><((('>>
    """,
    """
   ><((('>
    """,
]

# Fish speed settings
FISH_MIN_SPEED = 1
FISH_MAX_SPEED = 5
FISH_PAUSE_DURATION = 0.5


class Fish:
    def __init__(self, x, y, size, color, screen_width=800, screen_height=600):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.direction = random.choice([-1, 1])
        self.vx = self.direction * random.uniform(FISH_MIN_SPEED, FISH_MAX_SPEED)
        self.animation = FishAnimation()  # Initialize FishAnimation object

    def update(self):
        self.x += self.vx
        self.y += 0

        self.wrap_around_screen()

        self.animation.update()  # Update fish's animation

    def wrap_around_screen(self):
        if self.x < 0:
            self.x = self.screen_width
        elif self.x > self.screen_width:
            self.x = 0

        if self.y < 0:
            self.y = self.screen_height
        elif self.y > self.screen_height:
            self.y = 0


class FishAnimation:
    def __init__(self):
        self.sprite = random.choice(FISH_SPRITES)
        self.rect = pygame.Rect(
            random.randint(0, SCREEN_WIDTH),
            random.randint(0, SCREEN_HEIGHT),
            5,
            5,
        )
        self.speed = random.uniform(FISH_MIN_SPEED, FISH_MAX_SPEED)

    def update(self):
        self.rect.y += self.speed

        if self.rect.top > SCREEN_HEIGHT:
            self.rect.y = -self.rect.height
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.speed = random.uniform(FISH_MIN_SPEED, FISH_MAX_SPEED)
            pygame.time.delay(int(FISH_PAUSE_DURATION * 1000))

    def draw(self, screen):
        screen.blit(self.sprite, self.rect)

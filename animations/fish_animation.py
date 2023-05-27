import pygame
import random

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

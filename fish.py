import pygame
import random

FISH_COLOR = (0, 255, 0)

class Fish(pygame.sprite.Sprite):
    def __init__(self, x, y, size, speed):
        super().__init__()
        self.size = size
        self.speed = speed
        self.image = pygame.Surface([size, size])
        self.image.fill(FISH_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vx = random.uniform(-speed, speed)
        self.vy = random.uniform(-speed, speed)

    def update(self):
        self.move()

    def move(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

        # Wrap around the screen
        if self.rect.x > SCREEN_WIDTH:
            self.rect.x = 0
        elif self.rect.x < 0:
            self.rect.x = SCREEN_WIDTH
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = 0
        elif self.rect.y < 0:
            self.rect.y = SCREEN_HEIGHT

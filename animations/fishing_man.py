import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Fishing man sprite
FISHING_MAN_SPRITE = """
            ,-.
       O  /   `.
       <\/      `.
        |*        `.
       / \          `.
      /  /            `>')3s,
 --------.                 ,'
"""


class FishingManAnimation:
    def __init__(self):
        self.sprite = FISHING_MAN_SPRITE
        self.rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50, 5, 5)
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def draw(self, screen):
        x = self.rect.centerx - 3
        y = self.rect.centery - 3
        screen.blit(self.sprite, (x, y))

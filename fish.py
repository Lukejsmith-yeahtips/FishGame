import pygame

class Fish:
    def __init__(self, x, y, size, speed):
        self.position = [x, y]
        self.size = size
        self.speed = speed

    def update(self):
        self.position[1] += self.speed

        if self.position[1] > HEIGHT:
            self.position[1] = 0

    def draw(self, screen):
        pygame.draw.circle(screen, FISH_COLOR, self.position, self.size)

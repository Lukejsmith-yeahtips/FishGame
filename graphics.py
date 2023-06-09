import pygame
import os
import logging
import math
import random

# Get the root logger
logger = logging.getLogger()

class Graphics:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.clock = pygame.time.Clock()
        self.start_image = pygame.image.load(os.path.join("images", "start.jpg"))
        self.water_height = int(self.height * 0.6)
        self.boat_image = pygame.image.load(os.path.join("images", "boat.png"))
        self.boat_image = pygame.transform.scale(self.boat_image, (200, 100))
        self.fish_image = pygame.image.load(os.path.join("images", "fish.png"))
        self.fish_image = pygame.transform.scale(self.fish_image, (100, 100))
        self.fisherman_image = pygame.image.load(os.path.join("images", "fisherman.png"))
        self.fisherman_image = pygame.transform.scale(self.fisherman_image, (100, 100))
        self.end_image = pygame.image.load(os.path.join("images", "end.jpg"))

        self.sky_color = (135, 206, 250)
        self.cloud_spacing = 200
        self.water_color = (0, 0, 255)

    def draw_score(self, score, time_remaining):
         font = pygame.font.Font(None, 36)
         score_text = font.render("Score: " + str(score), True, (255, 255, 255))
         time_text = font.render("Time: " + str(time_remaining), True, (255, 255, 255))
         self.screen.blit(score_text, (10, 10))
         self.screen.blit(time_text, (10, 50))

    def draw_background(self):
        self.screen.fill(self.sky_color)  # Fill the screen with the sky color
        self.draw_clouds()  # Draw clouds

    def draw_water(self):
        pygame.draw.rect(self.screen, self.water_color, (0, self.water_height, self.width, self.height - self.water_height))

    def draw_clouds(self):
        cloud_image = pygame.image.load(os.path.join("images", "cloud.png"))
        cloud_image = pygame.transform.scale(cloud_image, (100, 50))
        num_clouds = self.width // self.cloud_spacing

        for i in range(num_clouds):
            x = i * self.cloud_spacing
            y = self.height // 4
            self.screen.blit(cloud_image, (x, y))

    def draw_ecosystem(self, ecosystem):
        for fish in ecosystem.fish_list:
            self.screen.blit(self.fish_image, (fish.x, fish.y))

    def draw_fisherman(self, fisherman):
        self.screen.blit(self.fisherman_image, (fisherman.x, fisherman.y))

    def draw_boat(self, boat):
        self.screen.blit(self.boat_image, (boat.x, boat.y))

    # Add logging for errors in the graphics module
    def log_error(self, message):
        logger.error(message)


class Fish:
    def __init__(self, x, y, size, speed):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.direction = random.uniform(0, 2 * math.pi)

    def update(self):
        self.move()
        self.wrap_around_screen()

    def move(self):
        self.x += math.cos(self.direction) * self.speed
        self.y += math.sin(self.direction) * self.speed

    def wrap_around_screen(self):
        if self.x < 0:
            self.x = self.width
        elif self.x > self.width:
            self.x = 0
        if self.y < 0:
            self.y = self.height
        elif self.y > self.height:
            self.y = 0

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), self.size)


class Ecosystem:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.fish_list = []

    def update(self):
        for fish in self.fish_list:
            fish.update()

    def add_fish(self):
        fish = Fish(self.width, self.height, 10, 1)
        self.fish_list.append(fish)

    def remove_fish(self, fish):
        self.fish_list.remove(fish)

    def get_closest_fish(self, position):
        closest_fish = None
        closest_distance = float("inf")

        for fish in self.fish_list:
            distance = math.dist((fish.x, fish.y), position)
            if distance < closest_distance:
                closest_fish = fish
                closest_distance = distance

        return closest_fish

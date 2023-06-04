import pygame
from constants import FISH_COLOR

class Graphics:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

    def draw_background(self, screen):
        screen.fill((0, 0, 0))  # Set the background color
        
    def draw_water(self, screen):
        water_color = (0, 0, 255)  # Set the water color
        water_rect = pygame.Rect(0, self.screen_height // 2, self.screen_width, self.screen_height // 2)
        pygame.draw.rect(screen, water_color, water_rect)  # Draw the water rectangle
    
    def draw_ecosystem(self, screen, ecosystem):
        # Implement the logic to draw the ecosystem
        # You can use the ecosystem object to access fish positions, sizes, etc.
        pass
    
    def draw_fisherman(self, screen, fisherman):
        # Implement the logic to draw the fisherman
        # You can use the fisherman object to access its position, boat, etc.
        pass
    
    def draw_score(self, screen, score):
        # Implement the logic to draw the score
        # You can use the score value to display the current score on the screen
        pass

    def draw_fish(self, screen, fish_list):
        for fish in fish_list:
            fish.draw(screen)


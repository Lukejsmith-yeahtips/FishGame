import pygame
import logging
from constants import WIDTH, HEIGHT, BOAT_COLOR, FISH_COLOR, SCORE_COLOR

logger = logging.getLogger(__name__)

class Graphics:
    def __init__(self, screen, width):
        self.screen = screen
        self.width = width

        self.water_image = pygame.image.load("images/water.jpg")
        self.water_image = pygame.transform.scale(self.water_image, (int(self.width), int(HEIGHT * 0.6)))

        self.boat_image = pygame.image.load("images/boat.jpg")
        self.boat_image = pygame.transform.scale(self.boat_image, (200, 200))

    def draw_background(self):
        """
        Draw the background with the water image.
        """
        self.screen.blit(self.water_image, (0, HEIGHT * 0.4))

    def draw_water(self):
        """
        Draw the water.
        """
        # Implement this function
        pass

    def draw_ecosystem(self, ecosystem):
        """
        Draw the ecosystem.
        """
        # Implement this function
        pass

    def draw_fisherman(self, fisherman):
        """
        Draw the fisherman with the boat image and fishing pole.
        """
        self.screen.blit(self.boat_image, (fisherman.boat.position[0] - 100, fisherman.boat.position[1] - 100))

        # Draw the fishing pole
        pole_length = 100
        pole_thickness = 10
        pole_color = (255, 255, 255)  # White color
        pole_start_pos = (fisherman.boat.position[0], fisherman.boat.position[1] - 50)  # Position at the center of the boat

        # Calculate the angle based on up and down arrow keys
        angle = fisherman.angle * 45  # Example: Multiply by 45 to get a reasonable range of angles (0 to 45 degrees)
        pole_end_pos = (
            pole_start_pos[0] + int(pole_length * pygame.math.cos(pygame.math.radians(angle))),
            pole_start_pos[1] - int(pole_length * pygame.math.sin(pygame.math.radians(angle)))
        )

        pygame.draw.line(self.screen, pole_color, pole_start_pos, pole_end_pos, pole_thickness)

    def draw_fish(self, fish_list):
        """
        Draw the fish using the fish.jpg image.
        """
        # Implement this function
        pass

    def draw_score(self, score):
        """
        Draw the score.
        """
        font = pygame.font.Font(None, 36)
        score_text = font.render("Score: " + str(score), True, SCORE_COLOR)
        self.screen.blit(score_text, (self.width - 150, 20))

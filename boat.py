import pygame

class Boat:
    SCREEN_WIDTH = 800  # Set the desired screen width
    SCREEN_HEIGHT = 600  # Set the desired screen height

    def __init__(self, width):
        self.x = width // 2
        self.y = Boat.SCREEN_HEIGHT // 2 + 15
        self.length = int(0.75 * 400)  # Adjust the length as desired
        self.color = (39, 119, 20)  # Dark green color

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def draw(self, screen):
        # Draw the boat
        # ...
        pass

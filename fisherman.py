import math
from constants import BOAT_COLOR, FISHERMAN_COLOR, WATER_COLOR

class Fisherman:
    def __init__(self, boat):
        self.boat = boat
        self.angle = 45

    def rotate_left(self):
        self.angle += 5

    def rotate_right(self):
        self.angle -= 5

    def draw(self, screen):
        boat_x, boat_y = self.boat.x, self.boat.y
        rod_length = 100

        rod_x = boat_x + math.cos(math.radians(self.angle)) * 50
        rod_y = boat_y - math.sin(math.radians(self.angle)) * 50
        bait_x = rod_x + math.cos(math.radians(self.angle)) * rod_length
        bait_y = rod_y - math.sin(math.radians(self.angle)) * rod_length

        pygame.draw.line(screen, FISHERMAN_COLOR, (boat_x, boat_y), (rod_x, rod_y), 5)
        pygame.draw.line(screen, WATER_COLOR, (rod_x, rod_y), (bait_x, bait_y), 2)
        pygame.draw.circle(screen, (0, 0, 0), (int(bait_x), int(bait_y)), 5)
        pygame.draw.circle(screen, (255, 0, 0), (int(bait_x), int(bait_y)), 3)

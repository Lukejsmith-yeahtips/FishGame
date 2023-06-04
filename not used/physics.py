import math

class Physics:
    def __init__(self):
        self.gravity = 9.8  # Acceleration due to gravity (m/s^2)

    def update(self, organisms):
        self.apply_gravity(organisms)

    def apply_gravity(self, organisms):
        for organism in organisms:
            organism.apply_force(0, self.gravity)

    def calculate_distance(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def calculate_angle(self, x1, y1, x2, y2):
        return math.atan2(y2 - y1, x2 - x1)

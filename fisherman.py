import logging

logger = logging.getLogger(__name__)

class Fisherman:
    def __init__(self, boat):
        self.boat = boat
        self.line_position = (boat.position[0], boat.position[1] - 20)
        self.score = 0

    def move_left(self):
        self.boat.move_left()

    def move_right(self):
        self.boat.move_right()

    def cast_line(self):
        # Implement casting line logic
        pass

    def line_caught_fish(self):
        # Implement line caught fish logic
        pass

    def line_position(self):
        return self.line_position

    def catch_fish(self, fish):
        # Implement fish catching logic
        pass

    def update(self):
        # Implement fisherman update logic
        pass

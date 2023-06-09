class Boat:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.width = 300
        self.height = 300
        self.x = (self.screen_width - self.width) // 2
        self.y = self.screen_height - self.height
        self.stability = 100  # Initial stability of the boat

    def move_left(self):
        if self.x > 0:
            self.x -= 10
            self.stability -= 5  # Decrease stability when boat moves

    def move_right(self):
        if self.x < self.screen_width - self.width:
            self.x += 10
            self.stability -= 5  # Decrease stability when boat moves

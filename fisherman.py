class Fisherman:
    def __init__(self, boat):
        self.x = boat.x
        self.y = boat.y - 100
        self.balance = 100
        self.line_length = 200
        self.fish_caught = []
        self.score = 0

    def move_left(self):
        self.x -= 10

    def move_right(self):
        self.x += 10

    def cast_line(self):
        # Logic for casting the fishing line
        pass

    def update(self):
        # Logic for updating the fisherman's position and state
        pass

    def line_caught_fish(self, fish):
        # Logic for checking if the fishing line has caught a fish
        pass

    def line_position(self):
        # Logic for getting the position of the fishing line
        pass

    def catch_fish(self, fish):
        # Logic for catching a fish and updating score
        pass

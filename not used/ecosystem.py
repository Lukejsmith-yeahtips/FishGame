from random import randint
from fish import Fish

FISH_SIZE_RANGE = (10, 20)  # Replace with your desired range of fish sizes
FISH_SPEED_RANGE = (1, 5)  # Replace with your desired range of fish speeds

class Ecosystem:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.fish_list = []

    def generate_fish(self):
        size = randint(*FISH_SIZE_RANGE)
        speed = randint(*FISH_SPEED_RANGE)
        x = randint(0, self.width)
        y = randint(0, self.height)
        fish = Fish(x, y, size, speed)
        self.fish_list.append(fish)

    def update(self):
        for fish in self.fish_list:
            fish.update()

    def remove_fish(self, fish):
        self.fish_list.remove(fish)

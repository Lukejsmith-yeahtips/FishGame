from random import randint
from fish import Fish

class Ecosystem:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.fish_list = []

    def generate_fish(self, size_range, speed_range):
        size = randint(*size_range)
        speed = randint(*speed_range)
        x = randint(0, self.width)
        y = randint(0, self.height)
        fish = Fish(x, y, size, speed)
        self.fish_list.append(fish)

    def update(self):
        for fish in self.fish_list:
            fish.update()

    def remove_fish(self, fish):
        self.fish_list.remove(fish)

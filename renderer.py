from constants import FISH_COLOR

class Graphics:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

    def draw_fish(self, screen, fish_list):
        for fish in fish_list:
            fish.draw(screen)

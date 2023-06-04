import pygame
from graphics import Graphics
from fisherman import Fisherman
from ecosystem import Ecosystem
from boat import Boat

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = self.screen.get_size()

        # Create the Graphics object with the appropriate width argument
        self.graphics = Graphics(self.screen, self.width)

        # Create other game objects as needed
        self.ecosystem = Ecosystem(self.width, self.height)  # Pass the width and height arguments to the Ecosystem constructor
        self.boat = Boat()  # Create a Boat object
        self.fisherman = Fisherman(self.boat)  # Pass the boat object to the Fisherman constructor

    def start(self):
        # Game loop
        while True:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def update(self):
        self.fisherman.update()

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.graphics.draw_background()
        self.graphics.draw_water()
        self.graphics.draw_ecosystem(self.ecosystem)
        self.graphics.draw_fisherman(self.fisherman)
        self.graphics.draw_fish(self.ecosystem.fish_list)
        self.graphics.draw_score(self.fisherman.score)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Fishing Game")
    game = Game(screen)
    game.start()

if __name__ == "__main__":
    main()

import pygame
import random
import noise

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SKY_COLOR = (135, 206, 250)
FISH_SIZE_RANGE = (10, 30)
FISH_SPEED_RANGE = (1, 3)

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fishing Game")

# Set up some variables for the Perlin noise
scale = 50.0
octaves = 6
persistence = 0.5
lacunarity = 2.0

# Create the water surface
def create_water_surface():
    water_surface = []
    for x in range(SCREEN_WIDTH):
        noise_value = noise.pnoise1(x/scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity)
        y = noise_value * SCREEN_HEIGHT/2 + SCREEN_HEIGHT/2
        water_surface.append(int(y))
    return water_surface

water_surface = create_water_surface()

# Define the Boat class
class Boat:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2 + 15
        self.length = int(0.75 * 400)  # Adjust the length as desired
        self.color = (39, 119, 20)  # Dark green color

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def draw(self):
        # Draw the main hull
        hull_points = [
            (self.x - self.length // 2, self.y),
            (self.x + self.length // 2, self.y),
            (self.x + self.length // 2 + 50, self.y + 100),
            (self.x - self.length // 2 - 50, self.y + 100)
        ]
        pygame.draw.polygon(screen, self.color, hull_points)

# Define the Fish class
class Fish:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.vx = random.uniform(*FISH_SPEED_RANGE)

    def update(self):
        self.x += self.vx

        # Wrap around screen
        if self.x > SCREEN_WIDTH:
            self.x = 0
        elif self.x < 0:
            self.x = SCREEN_WIDTH

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

# Create the Boat object
boat = Boat()

# Create a list to store the Fish objects
fish_list = []

# Generate initial fish population
for _ in range(10):
    x = random.randint(0, SCREEN_WIDTH)
    y = random.randint(0, SCREEN_HEIGHT)
    size = random.randint(*FISH_SIZE_RANGE)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    fish = Fish(x, y, size, color)
    fish_list.append(fish)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                boat.move_left()
            elif event.key == pygame.K_RIGHT:
                boat.move_right()

    # Update fish positions
    for fish in fish_list:
        fish.update()

    # Clear the screen
    screen.fill(SKY_COLOR)

    # Draw the water surface
    for x in range(SCREEN_WIDTH):
        pygame.draw.line(screen, (0, 0, 255), (x, water_surface[x]), (x, SCREEN_HEIGHT))

    # Draw the boat
    boat.draw()

    # Draw the fish
    for fish in fish_list:
        fish.draw()

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()

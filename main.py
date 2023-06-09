class Game:
    def __init__(self):
        self.graphics = Graphics()
        self.ecosystem = Ecosystem(self.graphics.width, self.graphics.height)
        self.boat = Boat(self.graphics.width // 2, self.graphics.height)
        self.fisherman = Fisherman(self.boat)
        self.running = False
        self.clock = pygame.time.Clock()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.fisherman.move_left()
                elif event.key == pygame.K_RIGHT:
                    self.fisherman.move_right()
                elif event.key == pygame.K_SPACE:
                    self.fisherman.cast_line()

    def update(self):
        self.ecosystem.update()
        # Additional game state update logic

    def draw(self):
        self.graphics.draw_background()
        self.graphics.draw_water()
        self.graphics.draw_ecosystem(self.ecosystem)
        self.graphics.draw_fisherman(self.fisherman)
        self.graphics.draw_score(self.fisherman.score, 0)  # Update time_remaining value
        pygame.display.flip()

    def start(self):
        self.running = True
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
        pygame.quit()

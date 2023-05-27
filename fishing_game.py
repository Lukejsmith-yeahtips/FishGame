import pygame
import random
import math

# Game settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30
TIME_LIMIT = 30

class Game:
    def __init__(self):
        # Initialize game objects and variables
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Fishing Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)
        self.fishing_man = FishingManAnimation(self.font)
        self.fish_list = []
        self.score = 0
        self.level = 1
        self.time_left = TIME_LIMIT * FPS
        self.game_over = False
        self.running = True
        self.menu_selection = 1


    def show_intro_screen(self):
        # Display the intro screen
        intro_image = pygame.image.load("images/start.jpg")
        self.screen.blit(intro_image, (0, 0))
        pygame.display.flip()

        # Wait for a key press to continue
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()
                if event.type == pygame.KEYDOWN:
                    return

    def show_main_menu(self):
        # Display the main menu
        while True:
            self.render_menu()
            self.wait_for_menu_selection()

    def render_menu(self):
        # Render the menu options on the screen
        self.screen.fill((0, 0, 0))

        game_title = self.font.render("Fishing Game", True, (255, 255, 255))
        title_rect = game_title.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100)
        )
        self.screen.blit(game_title, title_rect)

        option1_color = (255, 255, 255) if self.menu_selection == 1 else (128, 128, 128)
        option2_color = (255, 255, 255) if self.menu_selection == 2 else (128, 128, 128)

        option1_text = self.font.render("1. Play The Game", True, option1_color)
        option1_rect = option1_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        )
        self.screen.blit(option1_text, option1_rect)

        option2_text = self.font.render("2. Exit", True, option2_color)
        option2_rect = option2_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
        )
        self.screen.blit(option2_text, option2_rect)

        pygame.display.flip()

    def wait_for_menu_selection(self):
        # Wait for menu option selection
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.start_game()
                    if event.key == pygame.K_2:
                        self.quit_game()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.menu_selection = max(self.menu_selection - 1, 1)
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.menu_selection = min(self.menu_selection + 1, 2)

            if keys[pygame.K_RETURN]:
                if self.menu_selection == 1:
                    self.start_game()
                elif self.menu_selection == 2:
                    self.quit_game()

            self.render_menu()

    def start_game(self):
        # Start the game
        self.show_intro_screen()
        self.game_loop()

    def game_loop(self):
        # Main game loop
        while self.running:
            self.handle_events()
            self.update()
            self.render()

            if self.game_over:
                self.show_game_over_screen()
                self.running = False

            self.clock.tick(FPS)

    def handle_events(self):
        # Handle game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()

        keys = pygame.key.get_pressed()
        self.fishing_man.update(keys)

    def update(self):
        # Update game state
        keys = pygame.key.get_pressed()
        self.fishing_man.update(keys)
        self.update_fish()

    def update_fish(self):
        for fish in self.fish_list:
            fish.update()

            if fish.rect.colliderect(self.fishing_man.rect):
                self.fish_list.remove(fish)
                self.score += 1
                self.update_level()

        self.spawn_fish()

        self.time_left -= 1
        if self.time_left == 0:
            self.game_over = True

    def spawn_fish(self):
        if random.random() < self.get_fish_spawn_rate():
            fish = FishAnimation(self.get_fish_speed(), self.font)
            self.fish_list.append(fish)

    def get_fish_spawn_rate(self):
        return 0.1 * self.level

    def get_fish_speed(self):
        base_speed = random.uniform(1, 3)
        difficulty_factor = 1 + (self.level - 1) / 10
        return base_speed * difficulty_factor

    def update_level(self):
        self.level = min(self.score // 10 + 1, 10)

    def render(self):
        # Render game objects on the screen
        self.screen.fill((0, 0, 0))
        self.fishing_man.draw(self.screen)
        self.render_fish()
        self.render_score()
        self.render_time()
        pygame.display.flip()

    def render_fish(self):
        for fish in self.fish_list:
            fish.draw(self.screen)

    def render_score(self):
        score_text = self.font.render(
            "Score: " + str(self.score), True, (255, 255, 255)
        )
        score_rect = score_text.get_rect(topright=(SCREEN_WIDTH - 10, 10))
        self.screen.blit(score_text, score_rect)

    def render_time(self):
        time_text = self.font.render(
            "Time: " + str(self.time_left // FPS), True, (255, 255, 255)
        )
        time_rect = time_text.get_rect(topleft=(10, 10))
        self.screen.blit(time_text, time_rect)

    def show_game_over_screen(self):
        # Display the game over screen
        game_over_image = pygame.image.load("images/end.jpg")
        self.screen.blit(game_over_image, (0, 0))
        pygame.display.flip()
        pygame.time.wait(2000)

    def quit_game(self):
        # Quit the game
        pygame.quit()
        exit()


class FishingManAnimation:
    def __init__(self, font):
        self.sprite = [
            "            ,-.",
            "       O  /   `.",
            "       <\\/      `.",
            "        |*        `.",
            "       / \\          `.",
            "      /  /            `>')3s,",
            " --------.                 ,'",
        ]
        self.rect = pygame.Rect(SCREEN_WIDTH // 2, 0, 5, 5)
        self.speed = 5
        self.font = font
        self.casting = False
        self.casting_progress = 0
        self.casting_angle = 0

    def update(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        if keys[pygame.K_SPACE]:
            self.start_casting()
        elif self.casting:
            self.stop_casting()

    def start_casting(self):
        self.casting = True
        self.casting_progress += 1

        if self.casting_progress == 1:
            self.casting_angle = -math.pi / 2

        if self.casting_progress >= 1 and self.casting_progress <= 60:
            self.casting_angle += math.pi / 60

        if self.casting_progress == 61:
            self.casting = False
            self.casting_progress = 0

    def stop_casting(self):
        self.casting = False
        self.casting_progress = 0

    def draw(self, screen):
        x = self.rect.centerx - 3
        y = self.rect.centery - 3

        for line in self.sprite:
            text_surface = self.font.render(line, True, (255, 255, 255))
            screen.blit(text_surface, (x, y))
            y += self.font.get_linesize()


class FishAnimation:
    def __init__(self, speed, font):
        self.sprite = "<><"
        self.rect = pygame.Rect(
            random.randint(0, SCREEN_WIDTH),
            random.randint(0, SCREEN_HEIGHT),
            5,
            5,
        )
        self.speed = speed
        self.font = font

    def update(self):
        self.rect.y += self.speed

        if self.rect.top > SCREEN_HEIGHT:
            self.rect.y = -self.rect.height
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.speed = random.uniform(1, 3)

    def draw(self, screen):
        text_surface = self.font.render(self.sprite, True, (255, 255, 255))
        screen.blit(text_surface, self.rect)


def main():
    # Create game instance
    game = Game()

    # Show the main menu
    game.show_main_menu()


if __name__ == "__main__":
    main()

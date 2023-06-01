import pygame
import sys
from fishing_game import Game

def check_dependencies():
    try:
        import pygame
    except ImportError:
        print("Pygame is not installed. Please install Pygame using 'pip install pygame'.")
        sys.exit(1)

def main_menu():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Fishing Game")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    menu_items = ["Play Fishing Game", "Exit"]

    selected_item = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_item = (selected_item - 1) % len(menu_items)
                elif event.key == pygame.K_DOWN:
                    selected_item = (selected_item + 1) % len(menu_items)
                elif event.key == pygame.K_RETURN:
                    if selected_item == 0:
                        return "play"
                    elif selected_item == 1:
                        pygame.quit()
                        sys.exit()

        screen.fill((0, 0, 0))
        for i, item in enumerate(menu_items):
            if i == selected_item:
                text = font.render(item, True, (255, 255, 255))
            else:
                text = font.render(item, True, (128, 128, 128))
            screen.blit(text, (400 - text.get_width() // 2, 300 + 50 * i))

        pygame.display.flip()
        clock.tick(60)

def main():
    check_dependencies()
    choice = main_menu()
    if choice == "play":
        game = Game()
        game.start()

if __name__ == "__main__":
    main()

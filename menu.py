import logging
import pygame
import os
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fishing Game")

# Set up colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set up fonts
title_font = pygame.font.Font(None, 60)
rules_font = pygame.font.Font(None, 30)
button_font = pygame.font.Font(None, 40)

# Set up text
title_text = title_font.render("Fishing Game", True, WHITE)
rules_text = rules_font.render("Game rules go here...", True, WHITE)
play_text = button_font.render("Play Game", True, WHITE)
exit_text = button_font.render("Exit", True, WHITE)

# Set up button rectangles
play_button_rect = pygame.Rect(screen_width // 2 - 100, screen_height // 2, 200, 50)
exit_button_rect = pygame.Rect(screen_width // 2 - 100, screen_height // 2 + 70, 200, 50)

# Game loop
def start_game():
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if exit_button_rect.collidepoint(mouse_pos):
                        # Exit the game
                        pygame.quit()
                        sys.exit()

        # Draw the main menu screen
        screen.fill(BLUE)
        screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 100))
        screen.blit(rules_text, (screen_width // 2 - rules_text.get_width() // 2, 200))
        pygame.draw.rect(screen, WHITE, play_button_rect)
        pygame.draw.rect(screen, WHITE, exit_button_rect)
        screen.blit(play_text, (screen_width // 2 - play_text.get_width() // 2, screen_height // 2 + 10))
        screen.blit(exit_text, (screen_width // 2 - exit_text.get_width() // 2, screen_height // 2 + 80))

        # Update the display
        pygame.display.flip()

    # Game starts here
    # ...

# Cleanup
pygame.quit()

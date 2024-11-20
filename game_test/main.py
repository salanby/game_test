import sys
import os
import pygame
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'game_test')))
from core.state_manager import StateManager
from states.player_move import Player

# Initialize Pygame
pygame.init()

# Create the game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load the player and wall sprites
player_sprite = pygame.image.load('assets/sprites/spr_player.png')
wall_sprite = pygame.image.load('assets/sprites/spr_wall.png')

# Define the wall (for example, at the top of the screen)
wall_rect = pygame.Rect(300, 100, 32, 32)  # Example wall position and size

# Initialize the Player with walls for collision detection
player = Player(player_sprite, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, move_speed=2, walls=[wall_rect])

# Create the StateManager
state_manager = StateManager()

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the keys pressed
    keys = pygame.key.get_pressed()

    # Update the player's movement
    player.move(keys)

    # Fill the screen
    screen.fill((0, 0, 0))

    # Draw the player
    player.draw(screen)

    # Draw the wall sprite
    screen.blit(wall_sprite, wall_rect.topleft)  # Use the sprite for the wall

    # Update the display
    pygame.display.flip()

    # Set the game frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
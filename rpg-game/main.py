import pygame
import sys
from player import Player
from map import Map

# Constants
WIDTH, HEIGHT = 640, 480
FPS = 60

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mark's RPG")
clock = pygame.time.Clock()

# Load Game Objects
player = Player(100, 100)
game_map = Map()

# Main Game Loop
running = True
while running:
    clock.tick(FPS)
    screen.fill((0, 0, 0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle movement input with collision
    keys = pygame.key.get_pressed()
    player.move(keys, game_map.map_data, game_map.get_building_rects())

    # Draw everything
    game_map.draw(screen)
    player.draw(screen)

    pygame.display.flip()

# Quit the game
pygame.quit()
sys.exit()


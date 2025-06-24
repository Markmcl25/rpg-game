import pygame
import sys
from player import Player
from map import Map
from npc import NPC

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

# Load an NPC with a basic routine
npc_routine = [
    (1, 0, 60),   # move right for 60 frames
    (0, 1, 60),   # move down
    (-1, 0, 60),  # move left
    (0, -1, 60),  # move up
]
npc = NPC(200, 200, "assets/npc1.png", npc_routine)

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

    # Update NPC movement
    npc.update(game_map.map_data, game_map.get_building_rects())

    # Draw everything
    game_map.draw(screen)
    npc.draw(screen)  # ✅ Draw the NPC before or after player
    player.draw(screen)

    pygame.display.flip()

# Quit the game
pygame.quit()
sys.exit()

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

# Load an NPC with a basic routine (move in a square loop)
npc_routine = [
    (1, 0, 60),   # right for 60 frames
    (0, 1, 60),   # down
    (-1, 0, 60),  # left
    (0, -1, 60),  # up
]
npc = NPC(200, 200, "assets/npc1.png", npc_routine)

# Main Game Loop
running = True
while running:
    clock.tick(FPS)
    screen.fill((0, 0, 0))  # Black background (optional since map draws over this)

    # Handle quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement input + collision
    keys = pygame.key.get_pressed()
    player.move(keys, game_map.map_data, game_map.get_building_rects())

    # NPC routine movement update
    npc.update()

    # Draw everything in correct order
    game_map.draw(screen)  # Draw background and buildings
    npc.draw(screen)       # Draw NPC on top of the map
    player.draw(screen)    # Draw player on top

    pygame.display.flip()  # Refresh screen

# Clean exit
pygame.quit()
sys.exit()

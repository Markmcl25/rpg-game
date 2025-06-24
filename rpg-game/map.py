import pygame

TILE_SIZE = 32
ROWS = 15
COLS = 20

class Map:
    def __init__(self):
        grass_img = pygame.image.load("assets/grass.png")
        wall_img = pygame.image.load("assets/wall.png")
        b1 = pygame.image.load("assets/building1.png")
        b2 = pygame.image.load("assets/building2.png")
        b3 = pygame.image.load("assets/building3.png")

        self.tile = pygame.transform.scale(grass_img, (TILE_SIZE, TILE_SIZE))
        self.wall = pygame.transform.scale(wall_img, (TILE_SIZE, TILE_SIZE))

        # Scale buildings larger (5x5 tiles = 160x160 pixels)
        self.buildings = [
            (pygame.transform.scale(b1, (TILE_SIZE * 4, TILE_SIZE * 4)), (2 * TILE_SIZE, 3 * TILE_SIZE)),
            (pygame.transform.scale(b2, (TILE_SIZE * 4, TILE_SIZE * 4)), (10 * TILE_SIZE, 3 * TILE_SIZE)),
            (pygame.transform.scale(b3, (TILE_SIZE * 4, TILE_SIZE * 4)), (6 * TILE_SIZE, 8 * TILE_SIZE)),
        ]

        # 0 = grass, 1 = wall
        self.map_data = []
        self.map_data.append([1] * COLS)  # Top wall
        for _ in range(ROWS - 2):
            self.map_data.append([1] + [0] * (COLS - 2) + [1])  # Side walls with grass inside
        self.map_data.append([1] * COLS)  # Bottom wall

    def draw(self, screen):
        # Draw grass and walls
        for row in range(ROWS):
            for col in range(COLS):
                tile = self.map_data[row][col]
                x = col * TILE_SIZE
                y = row * TILE_SIZE

                if tile == 0:
                    screen.blit(self.tile, (x, y))
                elif tile == 1:
                    screen.blit(self.wall, (x, y))

        # Draw buildings (not tied to tile grid)
        for building, (x, y) in self.buildings:
            screen.blit(building, (x, y))

    def get_building_rects(self):
        return [pygame.Rect(pos[0], pos[1], building.get_width(), building.get_height()) for building, pos in
                self.buildings]
import pygame

TILE_SIZE = 32

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/player.png")
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 3

    def move(self, keys, map_data, building_rects):
        dx, dy = 0, 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx = -self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx = self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy = -self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy = self.speed

        # New position
        new_rect = self.rect.move(dx, dy)

        # Check for collisions with map walls and buildings
        if not self.collides_with_map(new_rect, map_data) and not self.collides_with_buildings(new_rect, building_rects):
            self.rect = new_rect

    def collides_with_map(self, rect, map_data):
        col = rect.x // TILE_SIZE
        row = rect.y // TILE_SIZE
        if row < 0 or row >= len(map_data) or col < 0 or col >= len(map_data[0]):
            return True
        return map_data[row][col] == 1

    def collides_with_buildings(self, rect, building_rects):
        return any(rect.colliderect(b_rect) for b_rect in building_rects)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

import pygame

TILE_SIZE = 32

class NPC:
    def __init__(self, x, y, sprite, routine):
        self.image = pygame.image.load(sprite)
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.routine = routine  # List of (dx, dy, duration)
        self.current_step = 0
        self.step_timer = 0
        self.speed = 1

    def update(self, map_data, building_rects):
        if self.current_step < len(self.routine):
            dx, dy, duration = self.routine[self.current_step]
            if self.step_timer < duration:
                move_x = dx * self.speed
                move_y = dy * self.speed
                new_rect = self.rect.move(move_x, move_y)

                if not self.collides_with_map(new_rect, map_data) and not self.collides_with_buildings(new_rect, building_rects):
                    self.rect = new_rect
                    self.step_timer += 1
                else:
                    # If blocked, skip this routine step
                    self.current_step += 1
                    self.step_timer = 0
            else:
                self.current_step += 1
                self.step_timer = 0

        # Loop routine
        if self.current_step >= len(self.routine):
            self.current_step = 0

    def collides_with_map(self, rect, map_data):
        col = rect.x // TILE_SIZE
        row = rect.y // TILE_SIZE
        if row < 0 or row >= len(map_data) or col < 0 or col >= len(map_data[0]):
            return True
        return map_data[row][col] == 1

    def collides_with_buildings(self, rect, building_rects):
        for b in building_rects:
            if rect.colliderect(b):
                return True
        return False

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

import pygame

class NPC:
    def __init__(self, x, y, sprite, routine):
        self.image = pygame.image.load(sprite)
        self.image = pygame.transform.scale(self.image, (32, 32))  # Adjust size if needed
        self.rect = self.image.get_rect(topleft=(x, y))
        self.routine = routine  # List of (dx, dy, duration) steps
        self.current_step = 0
        self.step_timer = 0
        self.speed = 1

    def update(self):
        if self.current_step < len(self.routine):
            dx, dy, duration = self.routine[self.current_step]
            if self.step_timer < duration:
                self.rect.x += dx * self.speed
                self.rect.y += dy * self.speed
                self.step_timer += 1
            else:
                self.current_step += 1
                self.step_timer = 0  # Reset timer

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

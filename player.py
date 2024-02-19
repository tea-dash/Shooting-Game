import pygame
from settings import black

class Player:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = 5

    def update(self): # Removed move_sound parameter as sound effects are disabled
        keys = pygame.key.get_pressed()
        moved = False
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
            moved = True
        if keys[pygame.K_RIGHT] and self.rect.x < self.screen.get_width() - self.width:
            self.rect.x += self.speed
            moved = True
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
            moved = True
        if keys[pygame.K_DOWN] and self.rect.y < self.screen.get_height() - self.height:
            self.rect.y += self.speed
            moved = True
        # Sound effect play call removed as sound effects are disabled

    def draw(self):
        # Update x and y to match the rectangle's position for accurate drawing
        self.x, self.y = self.rect.topleft
        # Airplane shape points
        points = [(self.x, self.y - 20), (self.x - 20, self.y + 20), (self.x + 20, self.y + 20)]
        pygame.draw.polygon(self.screen, black, points)
        pygame.draw.polygon(self.screen, black, points)
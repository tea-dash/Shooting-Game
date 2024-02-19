import pygame
from settings import red

class Boss:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = 100
        self.height = 100
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.health = 100

    def update(self):
        # TODO: Implement boss movement and attack patterns
        pass

    def draw(self):
        pygame.draw.rect(self.screen, red, self.rect)
        # TODO: Add more detailed boss drawing
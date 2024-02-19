import pygame
import random
from settings import red

class Enemy:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = 2

    def update(self):
        self.rect.y += self.speed

    def draw(self):
        pygame.draw.rect(self.screen, red, self.rect)

def spawn_enemy(enemies, screen, width, height):
    x = random.randint(0, width - 30)
    y = -30
    enemies.append(Enemy(screen, x, y))
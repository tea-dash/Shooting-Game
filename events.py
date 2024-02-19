
import pygame

def handle_events(player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True
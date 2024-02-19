import pygame
import random
import os
from settings import initialize_screen, gray, black, red
from events import handle_events
from player import Player
from enemy import Enemy, spawn_enemy

# Sound effects have been removed as per the builder's request

def main():
    # pygame.mixer.init() # Sound system initialization removed
    # move_sound = load_sound() # Sound loading removed
    # Initialize Pygame and screen
    screen, width, height = initialize_screen()
    clock = pygame.time.Clock()

    level = 1
    player = Player(screen, width // 2, height - 30)
    enemies = []
    bosses = []
    score = 0
    enemy_count = 10 * level  # Number of enemies increases with level
    boss_active = False
    # Main game loop
    running = True
    while running:
        running = handle_events(player)

        screen.fill(gray)

        # Player actions
        player.update() # Removed move_sound parameter as sound effects are disabled
        player.draw()

        # Enemy actions
        if not boss_active and len(enemies) < enemy_count:
            if random.randint(1, 20) == 1:
                spawn_enemy(enemies, screen, width, height)
        for enemy in enemies[:]:
            enemy.update()
            if enemy.rect.y > height:
                enemies.remove(enemy)
                score += 10  # Increment score for avoiding an enemy
            enemy.draw()

            # Check for collision
            if player.rect.colliderect(enemy.rect):
                running = False

        # Display score and level
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score} Level: {level}", 1, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
    main()
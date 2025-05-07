import pygame
from helper import set_random_position

def init_enemy(screen_width, screen_height):
    """Initialize the enemy graphics

    @param screen_width Width of the screen
    @param screen_height Height of the screen
    
    @return (enemy_image, enemy_rect): The enemy image and the corresponding rectangle
    """
    enemy_image = pygame.image.load("assets/images/king.png")
    enemy_rect = enemy_image.get_rect()
    enemy_rect = set_random_position(enemy_rect, screen_width, screen_height)

    return enemy_image, enemy_rect

def update_enemy(enemy_rect, direction, speed, screen_width, screen_height):
    """Update the enemy position

    @param enemy_rect The enemy rectangle
    @param direction Direction of the enemy
    @param speed Speed of the enemy
    @param screen_width Width of the screen
    @param screen_height Height of the screen
        
    @return The updated enemy rectangle
    """
    enemy_rect.x += direction[0] * speed
    enemy_rect.y += direction[1] * speed

    if enemy_rect.x < 0 or enemy_rect.x > screen_width - enemy_rect.width:
        direction[0] = -direction[0]
    if enemy_rect.y < 0 or enemy_rect.y > screen_height - enemy_rect.height:
        direction[1] = -direction[1]

    return enemy_rect
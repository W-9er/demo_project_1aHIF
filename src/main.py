"""! @brief Little clicking game"""
##
# @file main.py
#
# @brief Little clicking game
import pygame
from enemy import init_enemy, update_enemy
from helper import set_random_position, random_direction

# Initialzing 
pygame.init()


def display_title(screen, font, screen_width, screen_height):
    """Display the game title

    @param screen The pygame screen
    @param font The font object to use
    """
    title = font.render(f"K(l)ick the King", True, 'orange')
    title_rect = title.get_rect(center=(screen_width/2, screen_height/2))
    screen.blit(title, title_rect)


def display_score(screen, score, font):
    """Display the actual score

    @param screen The pygame screen
    @param score Actual score
    @param font The font object to use
    """
    scores = font.render(f"Score: {score}", True, 'black')
    screen.blit(scores, (10, 10))


def load_sounds():
    """Load all sounds and return them as a dictionary

    @return dict: The dictionary with the loaded sounds
    """
    # dictionary mit sound effects
    # sfx ... sound effect
    sounds = { 
        'sfx_hit': pygame.mixer.Sound('assets\sounds\sfx_hit.wav'),
        'music_bg': pygame.mixer.music.load('assets/sounds/background01.ogg')
    }

    return sounds


def check_click(enemy_rect, mouse_click_pos, sounds, score, direction, speed, screen_width, screen_height):
    """Check if the mouse clicked the enemy rectangle

    If the click is within the rect, the following actions are executed:
    - Play a sound effect
    - Update the score
    - Update the enemy speed
    - Create a new random direction
    
    
    @param enemy_rect The enemy rectangle
    @param mouse_click_pos Position of the mouse click
    @param sounds Sounds dictionary
    @param score Actual score
    @param direction Direction of the enemy
    @param speed Speed of the enemy
    @param screen_width Width of the screen
    @param screen_height Height of the screen
    
    @return (score, direction, speed): Returns the updated score, direction and speed
    """
    if enemy_rect.collidepoint(mouse_click_pos):
        score += 1
        speed += 0.2
        direction = random_direction()
        set_random_position(enemy_rect, screen_width, screen_height)
        sounds['sfx_hit'].play()
        
    return score, direction, speed


def game_loop(): 
    """The main game loop
    """
     # Setup
    FPS = 60
    clock = pygame.time.Clock()

    # Screen settings
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    score = 0
    speed = 0.5
    direction = random_direction()

    font = pygame.font.SysFont(None, 30)
    font_bg = pygame.font.SysFont(None, 80)
    
    # Load resources
    sounds = load_sounds()
    enemy_image, enemy_rect = init_enemy(screen_width, screen_height)

    # play the background music
    pygame.mixer.music.play(-1)

    # set the timer 
    start_time = pygame.time.get_ticks()
    game_duration = 10000  

    # The Game Loop
    running = True
    while running:
        # cycle through all events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_click_pos = pygame.mouse.get_pos()
                score, direction, speed  = check_click(enemy_rect, mouse_click_pos, sounds, score, direction, speed, screen_width, screen_height)
        
        # Update
        enemy_rect = update_enemy(enemy_rect, direction, speed, screen_width, screen_height)

        # check if time is up
        if pygame.time.get_ticks() - start_time > game_duration:
            running = False  # End the game

        # Redraw
        screen.fill('white')
        display_title(screen, font_bg, screen_width, screen_height)
        display_score(screen, score, font)
        screen.blit(enemy_image, enemy_rect)
            
        pygame.display.update()
        clock.tick(FPS)


    screen.fill('white')
    final_score_text = font.render(f'Final Score: {score}', True, (0, 0, 0))
    screen.blit(final_score_text, (screen_width // 2 - 100, screen_height // 2 - 20))
    pygame.display.update()
    pygame.time.delay(5000)


if __name__ == "__main__":
    game_loop()

    
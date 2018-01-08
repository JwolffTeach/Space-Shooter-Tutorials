"""
Lesson 8 - Moving the Enemy

Changes to this file:
  1. call the function gf.update_enemies(enemy) after updating the bullets.
  2. refactor the bullets.update() to be a function inside game_functions.
    a. rewrite that line to be gf.update_bullets(bullets)

"""

import pygame
from pygame.sprite import Group
from ship import Ship
from enemy import Enemy
from settings import Settings
import game_functions as gf
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
# Initialize pygame, settings, and screen object.
pygame.init()
settings = Settings()
screen = pygame.display.set_mode( (settings.screen_width, settings.screen_height) )

player = Ship(screen, settings) # Create the player; Player is a ship; Draw the ship on the screen

# Make a group to store bullets in.
bullets = Group()

# Make an enemy.
enemy = Enemy(settings, screen)

pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    
    # --- Check events; If user quits, exit main program loop
    done = gf.check_events(settings, screen, player, bullets)
    
    # --- Game logic should go here
    player.update_location()
    gf.update_bullets(bullets)
    gf.update_enemies(enemy)
    gf.check_bullets_pos(bullets)
    
    # --- Draw all objects to the screen
    gf.update_screen(screen, player, enemy, bullets)
    
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
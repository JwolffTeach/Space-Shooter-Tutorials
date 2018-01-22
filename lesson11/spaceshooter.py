"""
Lesson 11 - Waves of enemies

Changes to this file:

  1. Remove the lines that add enemy to enemies group. Call gf.spawn_enemies() instead.
  2. Add screen to the gf.check_collisions() functions.

"""

import pygame
from pygame.sprite import Group
from ship import Ship
from enemy import Enemy
from settings import Settings
from scoreboard import Scoreboard
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

sb = Scoreboard(settings, screen)

player = Ship(screen, settings) # Create the player; Player is a ship; Draw the ship on the screen

# Make a group to store bullets in.
bullets = Group()

# Make a group to store enemies in.
enemies = Group()

# Make an enemy.
gf.spawn_enemies(settings, screen, enemies)

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
    gf.update_everything(player, bullets, enemies)
    gf.check_collisions(settings, screen, sb, bullets, enemies)
    gf.check_bullets_pos(bullets)
    
    # --- Draw all objects to the screen
    gf.update_screen(screen, sb, player, enemies, bullets)
    
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
"""
Lesson 12 - Extended

Changes to this file:

  No Changes to this file.

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

# Make a group to store bullets in.
bullets = Group()

# Make a group to store enemies in.
enemies = Group()

# Make a group to store enemy bullets in
enemy_bullets = Group()

player = Ship(screen, settings, bullets) # Create the player; Player is a ship; Draw the ship on the screen

# Make an enemy.
gf.spawn_enemies(settings, screen, enemies, enemy_bullets)

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
    gf.update_everything(player, bullets, enemies, enemy_bullets)
    gf.check_collisions(settings, screen, sb, player, bullets, enemies, enemy_bullets)
    gf.check_bullets_pos(bullets)
    gf.check_enemy_bullets_pos(enemy_bullets, settings)
    
    # --- Draw all objects to the screen
    gf.update_screen(screen, sb, player, enemies, bullets, enemy_bullets)
    
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
"""
Lesson 9 - Bullet Collision and Enemy Group

Changes to this file:

  1. Added enemy as a parameter to gf.udpate_bullets() function call.
  2. Make a group of enemies.
  3. Change all parameter uses of "enemy" to "enemies"
    a. gf.update_bullets()
    b. gf.update_enemies()
    c. gf.update_screen()

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

# Make a group to store enemies in.
enemies = Group()

# Make an enemy.
enemy = Enemy(settings, screen)

enemies.add(enemy)

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
    gf.update_bullets(bullets, enemies)
    gf.update_enemies(enemies)
    gf.check_bullets_pos(bullets)
    
    # --- Draw all objects to the screen
    gf.update_screen(screen, player, enemies, bullets)
    
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
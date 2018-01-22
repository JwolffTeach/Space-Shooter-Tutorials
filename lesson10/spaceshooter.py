"""
Lesson 10 - Multiple Enemies and Keeping Track of Score

Changes to this file:

  1. Start with 2 more enemies for a total of 3.
  2. Import scoreboard
  3. Create a scoreboard object as "sb".
  4. Add "sb" as a parameter to gf.update_screen() call.
  5. Add "sb" as a parameter to gf.check_collisions() call.

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
enemy = Enemy(settings, screen)
enemy2 = Enemy(settings, screen)
enemy3 = Enemy(settings, screen)

enemies.add(enemy)
enemies.add(enemy2)
enemies.add(enemy3)

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
    gf.check_collisions(settings, sb, bullets, enemies)
    gf.check_bullets_pos(bullets)
    
    # --- Draw all objects to the screen
    gf.update_screen(screen, sb, player, enemies, bullets)
    
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
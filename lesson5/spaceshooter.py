"""
Lesson 5 - Shooting Bullets

Changes to this file:
  1. Import the Group class from pygame.sprite
  2. Make a group to store bullets in.
  3. Add bullets as a parameter to gf.check_events() method call.
  4. call update() method for each bullet in bullets group.
  5. Add bullets as a parameter to the gf.update_screen() method.

"""

import pygame
from pygame.sprite import Group
from ship import Ship
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
    bullets.update()
    
    # --- Draw all objects to the screen
    gf.update_screen(screen, player, bullets)
    
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
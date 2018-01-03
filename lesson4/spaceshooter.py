"""
Lesson 4 - Refactor screen updating to game_functions. Restrict the ship's movement so it doesn't go off screen.
  Changes to this file:
    1. screen.fill, screen.blit, player.blitme and display.flip code was moved to the game_functions.py file.
    2. Add settings as a parameter to pass to player when we instantiate player.
    3. Cleaned up comments in Main Program Loop.
"""

import pygame
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

pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    
    # --- Check events; If user quits, exit main program loop
    done = gf.check_events(player)
    
    # --- Game logic should go here
    player.update_location(settings)
    
    # --- Draw all objects to the screen
    gf.update_screen(screen, player)
    
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
"""
Lesson 4 - Refactor screen updating to game_functions. Restrict the ship's movement so it doesn't go off screen.
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

background_image = pygame.image.load("Backgrounds/blue2.png").convert()

# Load the sounds
lazer = pygame.mixer.Sound("Bonus/sfx_laser1.ogg")

player = Ship(screen) # Create the player; Player is a ship; Draw the ship on the screen

pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    # set done to whatever gf.check_events returns. If check_events returns 
    # True, that means the user is quitting the application.
    done = gf.check_events(player)
    
    # Check quit event
    
    # --- Game logic should go here
    player.update_location()
    
    gf.update_screen(screen, player)
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
"""
Lesson 3 - Refactor sound effects and add game_functions file.
  Changes to this file:
    1. Removed lazer sound effect loading. This goes into ship.py
    
    2. onMouseDown Event: Changed lazer.play() to be player.fire_weapon().
    
    3. Moved all events into a new file, game_functions.py
    
    4. import the game_functions file as gf so we can call functions from this 
         file later.
         
    5. Call the main event loop from game_functions, gf.check_events(). Player 
         is a parameter so we can call the fire_weapon() function of our player.
         
    6. Set the result of the check_events function to the variable done. If the 
         user is quitting, then done should be set to True.
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
    
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    screen.blit(background_image, [0,0])
    player.blitme()
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
"""
Lesson name: Lesson 2 - Create a class for spaceship and settings
Changes to this file:
  1. imported Ship class.
  2. removed the shaceship image loading, colorkey, and spaceship_rect.
  3. created an instance of the Ship() class as player with screen as a parameter.
  4. replace the screen.blit() call with the player.blitme() function.
  5. imported Settings class.
  6. replaced size = (700, 500) with settings = Settings()
  7. change the set_mode to use the settings.screen_width and settings.screen_height
"""

import pygame
from ship import Ship
from settings import Settings
 
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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            lazer.play()
 
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
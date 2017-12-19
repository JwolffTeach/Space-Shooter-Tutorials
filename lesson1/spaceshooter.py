"""
Lesson name: Lesson 1 - Create a ship_rect to control ship location
Changes to this file:
  Set the center of spacesihp to be the mouse location
    1. spaceship_rect = spaceship.get_rect()
    2. spaceship_rect.centerx = spaceship_position[0] and
    3. spaceship_rect.centery = spaceship.position[1]
    4. screen.blit(spaceship, spaceship_rect)
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

# Add background image to program
background_image = pygame.image.load("Backgrounds/blue2.png").convert()

# Add the spaceship image to program
spaceship = pygame.image.load("PNG/playerShip1_blue.png").convert()
spaceship.set_colorkey(BLACK)

spaceship_rect = spaceship.get_rect()

# Load the sounds
lazer = pygame.mixer.Sound("Bonus/sfx_laser1.ogg")

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
    spaceship_position = pygame.mouse.get_pos()
    spaceship_rect.centerx = spaceship_position[0]
    spaceship_rect.centery = spaceship_position[1]
    
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    screen.blit(background_image, [0,0])
    screen.blit(spaceship, spaceship_rect)
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
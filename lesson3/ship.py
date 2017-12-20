"""
Lesson 3 - Refactor sound effects and add game_functions file.
  Changes to this file:
    1. Loading the laser sound on init(). changed the name to be sfx.
    
    2. Create the fire_weapon() function. For now, this just plays the sfx sound.
"""

import pygame

# Define some colors
BLACK = (0, 0, 0)

""" A class used to represent the spaceship that the player controls in our game. """

class Ship():
    
    def __init__(self, screen):
        """ Initialize the ship. """
        self.screen = screen
        
        # Add the spaceship image to program
        self.image = pygame.image.load("PNG/playerShip1_blue.png").convert()
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        
        # Load the lazer sound
        self.sfx = pygame.mixer.Sound("Bonus/sfx_laser1.ogg")        
        
    def update_location(self):
        """ Update the position of our ship to be the mouse position. """
        mouse_pos = pygame.mouse.get_pos()
        self.rect.centerx = mouse_pos[0]
        self.rect.centery = mouse_pos[1]        
    
    def blitme(self):
        """ Draw the ship at its current location to the screen. """
        self.screen.blit(self.image, self.rect)
        
    def fire_weapon(self):
        """ Make a sound effect to represent weapon firing. """
        self.sfx.play()
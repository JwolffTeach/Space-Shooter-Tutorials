"""
Lesson name: Lesson 2 - Create a class for spaceship and settings
Changes to this file:
  1. Created the ship class
    a. import pygame
    b. create __init__(screen) function to include the screen as a parameter
    c. update_location() function to set the sprites location to the mouse position.
    d. blitme() function to draw the sprite to the screen.
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
        
    def update_location(self):
        """ Update the position of our ship to be the mouse position. """
        mouse_pos = pygame.mouse.get_pos()
        self.rect.centerx = mouse_pos[0]
        self.rect.centery = mouse_pos[1]        
    
    def blitme(self):
        """ Draw the ship at its current location to the screen. """
        self.screen.blit(self.image, self.rect)
"""
Lesson 14 - Game Over Screen

Changes to this file:

  No Changes to this file.

"""

import pygame
from weapon import Weapon
from player_health import Player_Health

# Define some colors
BLACK = (0, 0, 0)

""" A class used to represent the spaceship that the player controls in our game. """

class Ship():
    
    def __init__(self, screen, settings, bullets):
        """ Initialize the ship. """
        self.screen = screen
        self.settings = settings
        self.gun = Weapon(settings, screen, self, bullets, "single")
        self.health = Player_Health(screen, settings)
        
        # Add the spaceship image to program
        self.image = pygame.image.load("PNG/playerShip1_blue.png").convert()
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
               
        
    def update_location(self):
        """ Update the position of our ship to be the mouse position, but don't go off the screen. """
        mouse_pos = pygame.mouse.get_pos()
        
        self.rect.centerx = mouse_pos[0]
        self.rect.centery = mouse_pos[1]   
        
        # Check if the ship is off the screen to the left
        if self.rect.centerx < self.rect.width/2: # If this is true, then the ship should not go off the screen.
            self.rect.centerx = self.rect.width/2 # Reset position to the left side of the screen.
        # Check if the ship is off the screen to the right
        if self.rect.centerx > self.settings.screen_width - self.rect.width/2: # If this is true, then the ship should not go off the screen.
            self.rect.centerx = self.settings.screen_width - self.rect.width/2 # Reset position to the right side of the screen.
        
        # Check if the ship is off the screen to the top
        if self.rect.centery < self.rect.height/2: # If this is true, then the ship should not go off the screen.
            self.rect.centery = self.rect.height/2 # Reset position to the top of the screen.
        
        # Check if the ship is off the screen to the bottom  
        if self.rect.centery > self.settings.screen_height - self.rect.height/2: # If this is true, then the ship should not go off the screen.
            self.rect.centery = self.settings.screen_height - self.rect.height/2 # Reset position to the bottom of the screen.
    
    def blitme(self):
        """ Draw the ship at its current location to the screen. """
        self.health.update_healthbar()
        self.health.draw_healthbar()
        self.screen.blit(self.image, self.rect)
        
    def fire_weapon(self):
        """ Make a sound effect to represent weapon firing. """
        self.sfx.play()
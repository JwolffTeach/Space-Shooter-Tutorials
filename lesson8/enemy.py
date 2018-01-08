"""
Lesson 8 - Moving the Enemy

Changes to this file:

  1. Added the update() function to change the y value of the enemy.

"""

import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    """ A class to represent an enemy UFO. """
    
    def __init__(self, settings, screen):
        """ Initialize the alien and set its starting position. """
        self.screen = screen
        self.settings = settings
        
        # Load the enemy image and set its rect attribute.
        self.image = pygame.image.load('PNG/Enemies/enemyBlack1.png')
        self.rect = self.image.get_rect()
        
        # Start each new enemy in the top center of the screen.
        self.rect.centerx = settings.screen_width / 2
        self.rect.y = 0
        
        # Store the enemy's exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
    def blitme(self):
        """ Draw the enemy at its current location. """
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        """ Move the alien down. """
        self.y += self.settings.enemy_speed_factor
        self.rect.y = self.y
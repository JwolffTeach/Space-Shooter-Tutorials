"""
Lesson 11 - Waves of enemies

Changes to this file:

  No Changes to this file.

"""

import pygame
from pygame.sprite import Sprite
import random

class Enemy(Sprite):
    """ A class to represent an enemy UFO. """
    
    def __init__(self, settings, screen):
        """ Initialize the alien and set its starting position. """
        super().__init__() #adding super call to make Bullet a pygame Sprite
        self.screen = screen
        self.settings = settings
        
        # Load the enemy image and set its rect attribute.
        self.image = pygame.image.load('PNG/Enemies/enemyBlack1.png')
        self.rect = self.image.get_rect()
        
        # Start each new enemy off the screen, but centered.
        self.rect.centerx = random.randint(self.rect.width, self.settings.screen_width-self.rect.width)
        self.rect.y = random.randint(-500, -200)
        
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
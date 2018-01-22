"""
Lesson 10 - Bullet Collision and Enemy Group

Changes to this file:

  No changes to this file

"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ A class to manage bullets fired from the ship. """
    
    def __init__(self, settings, screen, ship):
        """ Create a bullet object at the ship's current position. """
        super().__init__() # Inherit properites of Sprite class.
        self.screen = screen
        self.settings = settings
        
        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)
        
        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor
        
    def update(self):
        """ Move the bullet up the screen. """
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect position.
        self.rect.y = self.y
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        
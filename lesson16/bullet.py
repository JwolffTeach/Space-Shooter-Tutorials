"""
Lesson 14 - Game Over Screen

Changes to this file:

  No Changes to this file.

"""

import pygame
from pygame.sprite import Sprite
import time
import math


class Bullet(Sprite):
    """ A class to manage bullets fired from the ship. """
    
    def __init__(self, settings, screen, ship, bulletType="none", direction=0):
        """ Create a bullet object at the ship's current position. """
        super().__init__() # Inherit properites of Sprite class.
        self.screen = screen
        self.settings = settings 
        self.bulletType = bulletType
        
        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # Store the bullet's position as a decimal value
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        # Set default values for color, speed_factor, and acceleration
        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor
        self.acceleration = 1
        self.direction = direction
        
        # Create a clock for this bullet
        self.startTime = time.time()
        self.timeElapsed = 0.0
        
        if(self.bulletType == "single"):
            self.make_single() 
        elif(self.bulletType == "double"):
            self.make_double()
        elif(self.bulletType == "snake"):
            self.make_snake()
        
    def update(self):
        """ Move the bullet up the screen. """
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        self.rect.y = self.y
        self.speed_factor *= self.acceleration
        # Update the rect position.
        
        if(self.bulletType == "snake"):
            self.timeElapsed = time.time() - self.startTime
            xChange = self.amplitude * math.cos((math.pi * self.direction) + self.frequency*((self.speed * self.timeElapsed)))
            self.x += xChange
            self.rect.x = self.x
            
    def onCollision(self, other):
        print(type(self), 'Collided with ', type(other))
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        
    def make_single(self):            
        self.speed_factor = 5
        self.acceleration = 1.05
        self.color = (255, 0, 0)
        
    def make_double(self):
        self.speed_factor = 1
        self.acceleration = 1
        self.color = (0, 0, 255)
        
    def make_snake(self):
        self.speed_factor = 2
        self.acceleration = 1
        self.color = (0, 255, 0)
        self.frequency = 5 # Controls how far to the left or right bullet travels
        self.amplitude = 10 # Controls how quickly the bullet will perform its full circle
        self.speed = -1
        self.rect.height = 10
        self.rect.width = 10
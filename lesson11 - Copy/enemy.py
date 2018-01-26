"""
Lesson 12 - Extended

Changes to this file:

  No Changes to this file.

"""

import pygame
from pygame.sprite import Sprite
import random
from bullet import Bullet

class Enemy(Sprite):
    """ A class to represent an enemy UFO. """
    
    def __init__(self, settings, screen, bullets_group):
        """ Initialize the alien and set its starting position. """
        super().__init__() #adding super call to make Bullet a pygame Sprite
        self.screen = screen
        self.settings = settings
        self.bullets_group = bullets_group
        
        # Load the enemy image and set its rect attribute.
        self.image = pygame.image.load('PNG/Enemies/enemyBlack1.png')
        self.rect = self.image.get_rect()
        
        # Start each new enemy off the screen, but centered.
        self.rect.centerx = random.randint(self.rect.width, self.settings.screen_width-self.rect.width)
        self.rect.y = random.randint(-500, -200)
        
        # Store the enemy's exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        # Store the enemy's direction.
        self.direction = 1
        
        # Store the weapon timer
        self.clock = pygame.time.Clock()
        self.timer = 0
        
    def blitme(self):
        """ Draw the enemy at its current location. """
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        """ Move the alien down. """
        self.y += self.settings.enemy_v_speed_factor
        self.x += self.settings.enemy_h_speed_factor * self.direction
        self.rect.y = self.y
        self.rect.x = self.x   
        
        # Check if we should create a bullet.
        self.clock.tick(60)        
        self.timer = self.timer + self.clock.get_time()
        
        if self.timer > 1000: # in milliseconds
            self.fire_bullet()
            self.timer = 0
        print(self.timer)        
        
    def fire_bullet(self):
        """ Fire a bullet that will move down. """
        new_bullet = Bullet(self.settings, self.screen, self)
        new_bullet.speed_factor *= -1
        self.bullets_group.add(new_bullet)
        print("Test if a bullet spawned!")
        print(len(self.bullets_group))
"""
Lesson 14 - Game Over Screen

Changes to this file:

  No Changes to this file.

"""

import pygame
from bullet import Bullet

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


""" A class for different weapons the ship can have. """
class Weapon():
    
    def __init__(self, settings, screen, player, bullets, bulletType=0.0):
        """ Initialize the weapon. """
        self.settings = settings
        self.screen = screen
        self.player = player
        self.bullets = bullets
        self.bulletType = bulletType # 1 is Single, 2 is Double, 3 is Snake
        

        # Load the lazer sounds
        self.sfx_laser1 = pygame.mixer.Sound("Bonus/sfx_laser1.ogg")
        self.sfx_laser2 = pygame.mixer.Sound("Bonus/sfx_laser2.ogg")
        self.sfx = self.sfx_laser1
    
    def fire_weapon(self):
        """ Make a sound effect to represent weapon firing. """
        # Shoot a single bullet from the center.
        if self.bulletType < 1.0: # Single Bullet
            new_bullet = Bullet(self.settings, self.screen, self.player, 1)
            self.bullets.add(new_bullet)
            
        # Shoot two bullets, one on each side.
        elif self.bulletType < 2.0: # Double Bullet
            new_bullet1 = Bullet(self.settings, self.screen, self.player, 2)
            new_bullet1.rect.centerx = self.player.rect.left
            new_bullet1.y += 20
            new_bullet2 = Bullet(self.settings, self.screen, self.player, 2)
            new_bullet2.rect.centerx = self.player.rect.right
            new_bullet2.y += 20
            self.bullets.add(new_bullet1)
            self.bullets.add(new_bullet2)
        
        # Shoot a snake bullet.
        elif self.bulletType < 3.0: # Snake Bullet
            new_bullet = Bullet(self.settings, self.screen, self.player, 3, 0)
            self.bullets.add(new_bullet)
            new_bullet = Bullet(self.settings, self.screen, self.player, 3, 1)
            self.bullets.add(new_bullet)
            
        self.sfx.play()
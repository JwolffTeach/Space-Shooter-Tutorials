"""
Lesson 8 - Moving the Enemy

Changes to this file:

  1. Added Alien settings, specifically alien_speed_factor
    
"""

import pygame

""" A class to store all settings for Spaceshooter. """

class Settings():
    
    def __init__(self):
        """ Initialize the game's settings. """
        # Screen settings
        self.screen_width = 700
        self.screen_height = 500
        
        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        
        # Enemy settings
        self.enemy_speed_factor = 1
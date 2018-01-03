"""
Lesson 5  - Shooting Bullets

Changes to this file:
    1. Add bullet settings for speed, width, height, and color
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
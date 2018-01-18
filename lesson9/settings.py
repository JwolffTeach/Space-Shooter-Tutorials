"""
Lesson 9 - Bullet Collision and Enemy Group

Changes to this file:

  No changes to this file
    
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
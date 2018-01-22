"""
Lesson 11 - Waves of enemies

Changes to this file:

  1. Added current_level to keep track of the level

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
        
        # Score Settings
        self.score = 0
        self.enemy_points = 50
        
        # Level settings
        self.current_level = 1
        
    def increase_score(self, amount):
        self.score += amount
        print(self.score)
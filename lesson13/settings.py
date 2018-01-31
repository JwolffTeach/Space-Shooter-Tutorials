"""
Lesson 12 - Extended

Changes to this file:

  No Changes to this file.

"""

import pygame

""" A class to store all settings for Spaceshooter. """

class Settings():
    
    def __init__(self):
        """ Initialize the game's settings. """
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 800
        
        # Bullet settings
        self.bullet_speed_factor = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        
        # Enemy settings
        self.enemy_v_speed_factor = 4
        self.enemy_h_speed_factor = 1
        self.enemy_firespeed_factor = 1000
        self.enemy_bullet_speed = 5
        
        # Score Settings
        self.score = 0
        self.enemy_points = 50
        
        # Level settings
        self.current_level = 1
        
    def increase_score(self, amount):
        self.score += amount
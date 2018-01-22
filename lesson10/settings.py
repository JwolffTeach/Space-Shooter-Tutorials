"""
Lesson 10 - Multiple Enemies and Keeping Track of Score

Changes to this file:

  1. Added Score variable as self.score
  2. Created a function to increase score, increase_score(self, amount)
  3. Add enemy_points variable as self.enemy_points

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
        
    def increase_score(self, amount):
        self.score += amount
        print(self.score)
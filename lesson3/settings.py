"""
Lesson name: Lesson 2 - Create a class for spaceship and settings
Changes to this file:
  1. Created the Settings class to initialize the screen_width and screen_height
"""

import pygame

""" A class to store all settings for Spaceshooter. """

class Settings():
    
    def __init__(self):
        """ Initialize the game's settings. """
        # Screen settings
        self.screen_width = 700
        self.screen_height = 500
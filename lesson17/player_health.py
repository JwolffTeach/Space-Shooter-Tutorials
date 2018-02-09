"""
Lesson 14 - Game Over Screen

Changes to this file:

  No Changes to this file.

"""

import pygame

GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

""" A class to store health and draw healthbar. """
class Player_Health():
    
    def __init__(self, screen, settings):
        """ Initialize the health settings. """
        self.screen = screen
        self.settings = settings
        self.max_hp = 100
        self.hp = self.max_hp
        self.color = (0, 255, 0)
        self.width = self.hp * 5 # 5 pixels per health point
        self.height = 20
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.offset = -20
        
    def resetHealth(self):
        self.hp = self.max_hp
        self.rect.width = self.hp * 5
        self.update_healthbar()
        
    def decrease_hp(self, amt):
        self.hp -= amt
        self.rect.width = self.hp * 5
        if(self.hp <= 0):
            return True
        
    def update_healthbar(self):
        self.rect.centerx = self.settings.screen_width/2
        self.rect.bottom = self.settings.screen_height -50
        
    def draw_healthbar(self):
        if self.hp <= 100:
            self.color = GREEN
        if self.hp <= 50:
            self.color = YELLOW
        if self.hp <= 25:
            self.color = RED
        pygame.draw.rect(self.screen, self.color, self.rect)
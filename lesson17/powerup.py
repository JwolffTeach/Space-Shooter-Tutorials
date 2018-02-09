import pygame
from pygame.sprite import Sprite

""" A class that can powerup the player's weapon. """
class Powerup(Sprite):
    
    def __init__(self, screen, settings, start_rect, powerup_level):
        super().__init__()
        
        self.screen = screen
        self.settings = settings
        self.powerup_level = powerup_level
    
        # Load the powerup image and set its rect attribute.
        self.image = pygame.image.load('PNG/Power-ups/bolt_gold.png')
        self.rect = self.image.get_rect()
        
        # Start each new enemy off the screen, but centered.
        self.rect.centerx = start_rect.centerx
        self.rect.centery = start_rect.centery
        
        # Store the enemy's exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)    
        
    def blitme(self):
        """ Draw the powerup at its current location. """
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        """ Move the powerup down. """
        self.y += self.settings.powerup_speed
        self.rect.y = self.y
        self.rect.x = self.x
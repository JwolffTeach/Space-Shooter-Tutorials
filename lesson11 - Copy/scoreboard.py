"""
Lesson 12 - Extended

Changes to this file:

  No Changes to this file.

"""

import pygame.font

class Scoreboard():
    """ A class to report scoring information """
    
    def __init__(self, settings, screen):
        """ Initialize scorekeeping attributes. """
        self.settings = settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        # Prepare the initial score image.
        self.prep_score()
        
    def prep_score(self):
        """ Turn the score into a rendered image. """
        score_str = str(self.settings.score)
        self.score_image = self.font.render(score_str, True, self.text_color, (255, 255, 255))
        
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def show_score(self):
        """ Draw score to the screen. """
        self.screen.blit(self.score_image, self.score_rect)
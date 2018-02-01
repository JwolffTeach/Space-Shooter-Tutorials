"""
Lesson 14 - Game Over Screen

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
        self.smallfont = pygame.font.SysFont(None, 32)
        
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
        
    def prep_GameOver(self):
        """ Turn the score counter into a game over text. """
        gameOver_str = "Game Over!"
        self.gameOver_image = self.font.render(gameOver_str, True, self.text_color, (255, 255, 255))
        
        # Display the gameover in the center of the screen.
        self.gameOver_rect = self.gameOver_image.get_rect()
        self.gameOver_rect.centerx = self.screen_rect.centerx
        self.gameOver_rect.centery = self.screen_rect.centery
        
        # Display the click to play again text
        playAgain_str = "Click to play again!"
        self.playAgain_image = self.smallfont.render(playAgain_str, True, self.text_color, (255, 255, 255))
        
        # Display the play again text below the gameover text.
        self.playAgain_rect = self.playAgain_image.get_rect()
        self.playAgain_rect.y = self.gameOver_rect.y + 100
        self.playAgain_rect.x = self.gameOver_rect.x
        
    def show_score(self):
        """ Draw score to the screen. """
        self.screen.blit(self.score_image, self.score_rect)
        
    def show_GameOver(self):
        """ Draw the gameover text and playagain text to the screen. """
        self.screen.blit(self.gameOver_image, self.gameOver_rect)
        self.screen.blit(self.playAgain_image, self.playAgain_rect)
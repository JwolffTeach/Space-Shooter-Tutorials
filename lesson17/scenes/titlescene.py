import pygame
from pygame.sprite import Group
from ship import Ship
from enemy import Enemy
from settings import Settings
from scoreboard import Scoreboard
import game_functions as gf

from scene import Scene

class TitleScene(Scene):
    def __init__(self, settings, screen, scoreboard):
        Scene.__init__(self)
        self.settings = settings
        self.screen = screen
        self.sb = scoreboard
        
    def ProcessInput(self):
        return gf.pause_events()
    
    def Update(self):
        self.sb.prep_GameOver()
    
    def Render(self):
        self.sb.show_GameOver()
        pygame.display.flip()  
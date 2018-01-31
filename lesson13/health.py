import pygame

GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

""" A class to store health and draw healthbar. """
class Health():
    
    def __init__(self, screen):
        """ Initialize the health settings. """
        self.screen = screen
        self.hp = 4
        self.color = (0, 255, 0)
        self.width = self.hp * 25 # 25 pixels per health point
        self.height = 20
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.offset = -20
        
    def decrease_hp(self):
        self.hp -= 1
        self.rect.width = self.hp * 25
        
    def update_position(self, rect):
        self.rect.x = rect.x
        self.rect.y = rect.y + self.offset
        
    def draw_healthbar(self):
        if self.hp == 2:
            self.color = YELLOW
        elif self.hp == 1:
            self.color = RED
        pygame.draw.rect(self.screen, self.color, self.rect)
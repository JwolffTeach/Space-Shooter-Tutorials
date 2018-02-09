import pygame
from pygame.sprite import Group
from ship import Ship
from enemy import Enemy
from settings import Settings
from scoreboard import Scoreboard
import game_functions as gf

from scene import Scene

class GameScene(Scene):
    def __init__(self, settings, screen, scoreboard):
        Scene.__init__(self)
        
        self.settings = settings
        self.screen = screen
        self.sb = scoreboard
        self.gamePaused = False
        
        # Make a group to store bullets in.
        self.bullets = Group()
        
        # Make a group to store enemies in.
        self.enemies = Group()
        
        # Make a group to store enemy bullets in
        self.enemy_bullets = Group()
        
        self.player = Ship(self.screen, self.settings, self.bullets) # Create the player; Player is a ship; Draw the ship on the screen
        
        # Make an enemy.
        gf.spawn_enemies(self.settings, self.screen, self.enemies, self.enemy_bullets)
        
        # Make a group to store powerups in
        self.powerups = Group()
        
        gf.startGame(self.player, self.bullets, self.enemy_bullets, self.enemies, self.settings)

        
    def ProcessInput(self):
        # --- Check events; If user quits, exit main program loop
        gf.check_events(self.settings, self.screen, self.player, self.bullets, self.powerups, False)
    
    def Update(self):
        # --- Game logic should go here
        gf.update_everything(self.player, self.bullets, self.enemies, self.enemy_bullets, self.powerups)
        gf.check_bullets_pos(self.bullets)
        gf.check_enemy_bullets_pos(self.enemy_bullets, self.settings)
        # if the player is dead, then game is over.
        return gf.check_collisions(self.settings, self.screen, self.sb, self.player, self.bullets, self.enemies, self.enemy_bullets, self.powerups)
    
    def Render(self):
        # The game scene is just a blank blue screen
        #screen.fill((0, 0, 255))

        # --- Draw all objects to the screen
        gf.update_screen(self.screen, self.sb, self.player, self.enemies, self.bullets, self.enemy_bullets, self.powerups)        
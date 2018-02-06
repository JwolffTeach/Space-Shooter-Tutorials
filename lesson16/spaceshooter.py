"""
Lesson 14 - Game Over Screen

Changes to this file:

  1. If check_collisions() returns true, then the player is dead, so we stop drawing and moving things.

"""

import pygame
from pygame.sprite import Group
from ship import Ship
from enemy import Enemy
from settings import Settings
from scoreboard import Scoreboard
import game_functions as gf
from scene_manager import SceneManager
from scenes.gamescene import GameScene
from scenes.titlescene import TitleScene
 
# Initialize pygame, settings, and screen object.
pygame.init()

pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
gamePaused = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

settings = Settings()
screen = pygame.display.set_mode( (settings.screen_width, settings.screen_height) )

sb = Scoreboard(settings, screen)

SM = SceneManager()
title_scene = TitleScene(settings, screen, sb)
game_scene = GameScene(settings, screen, sb)

SM.add_scene("title", title_scene)
SM.add_scene("game", game_scene)

# Start on the title_scene
SM.change_scene(game_scene)
# -------- Main Program Loop -----------
while not done:
    
    if gamePaused == True:
        # First, make sure we're in the title scene.
        if(SM.scene!=title_scene):
            SM.change_scene(title_scene)
            
        # Check if we the user wants to start again.
        gamePaused = SM.scene.ProcessInput()
        
        # Update the logic of the menu.
        SM.scene.Update()
        
        # Draw everything to the screen.
        SM.scene.Render()
        
        # Lastly, check if the game is no longer paused. If not, continue to game_scene.
        if(gamePaused == False):
            SM.change_scene(game_scene)
            gf.startGame(SM.scene.player, SM.scene.bullets, SM.scene.enemy_bullets, SM.scene.enemies, SM.scene.settings)
    else:
        # Game_Scene logic.
        SM.scene.ProcessInput()
        gamePaused = SM.scene.Update()
        SM.scene.Render()
    
    
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
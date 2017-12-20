"""
Lesson 3 - Refactor sound effects and add game_functions file.
  Changes to this file:
    1. import pygame
    
    2. Create check_events() function. Right now we only have two events to look 
         for, quit, and mouse button down
         
    3. QUIT - we will return True, meaning the main loop will now be done and 
         the application will close.
         
    4. MOUSEBUTTONDOWN - we want to fire the player weapon, so we must use the 
         player parameter so the program knows to make the weapon sound for the 
         player.
"""

import pygame

def check_events(player):
    """ Respond to keypresses and mouse events. """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True # Close the application.
        elif event.type == pygame.MOUSEBUTTONDOWN:
            player.fire_weapon()
    return False # Do NOT close the application.
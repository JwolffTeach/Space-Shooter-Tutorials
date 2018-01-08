"""
Lesson 6 - Deleting Bullets Off Screen

Changes to this file:

  1. new function: check_bullets_pos()
    a. bullets is a parameter because we want to check the y position of each bullet.
    b. loop through each bullet, check if the rect.bottom is less than 0. if it is, remove it from the group!

"""

import pygame
from bullet import Bullet


WHITE = (255, 255, 255)

def check_events(settings, screen, player, bullets):
    """ Respond to keypresses and mouse events. """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True # Close the application.
        elif event.type == pygame.MOUSEBUTTONDOWN:
            player.fire_weapon()
            new_bullet = Bullet(settings, screen, player)
            bullets.add(new_bullet)
    return False # Do NOT close the application.

def update_screen(screen, player, bullets):
    """ Update images on the screen and flip to the new screen. """
    # --- Screen-clearing code goes here
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    
    # Redraw all bullets behind player and aliens
    for bullet in bullets:
        bullet.draw_bullet()
    
    player.blitme()
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()    

def check_bullets_pos(bullets):
    """ Check if a bullet has gone off the screen. If it has, remove it. """
    for bullet in bullets:
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
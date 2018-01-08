"""
Lesson 7 - Creating an Enemy

Changes to this file:

  1. Add a parameter for enemy in update_screen() function.
  2. call the enemy.blitme() function after player.blitme() to draw the enemy.

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

def update_screen(screen, player, enemy, bullets):
    """ Update images on the screen and flip to the new screen. """
    # --- Screen-clearing code goes here
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    
    # Redraw all bullets behind player and aliens
    for bullet in bullets:
        bullet.draw_bullet()
    
    player.blitme()
    enemy.blitme()
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()    

def check_bullets_pos(bullets):
    """ Check if a bullet has gone off the screen. If it has, remove it. """
    for bullet in bullets:
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
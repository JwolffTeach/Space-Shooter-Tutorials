"""
Lesson 5 - Shooting Bullets

Changes to this file:

  1. check_events(): When the user clicks mousedown, we want to fire_weapon, and create a bullet.
    a. Create a new_bullet after we call fire_bullet() function.
      i. A Bullet class requires the following parameters: settings, screen, and player
    b. Add bullets as a parameter to check_events() function.
    c. Add this bullet to our bullets Group.
    
  2. update_screen(): Draw bullets when we update the screen.
    a. Add bullets as a parameter to the update_screen() function.
    b. Loop through bullets and call the draw_bullet() function for each bullet.

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
"""
Lesson 9 - Bullet Collision and Enemy Group

Changes to this file:

  1. Added enemy as a parameter to update_bullets() function so we can check for collisions between bullets and enemy.
  2. Added collision checking line in update_bullets()
  3. Change references from enemy to enemies
    a. update_screen() parameter enemy --> enemies
         - change enemy.blitme() to loop through all enemies and blit them.
    b. update_bullets() parameter enemy --> enemies
         - change spritecollide to be groupcollide
    c. update_enemies() parameter enemy --> enemies
         - enemy.update() --> enemies.update()
  
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

def update_screen(screen, player, enemies, bullets):
    """ Update images on the screen and flip to the new screen. """
    # --- Screen-clearing code goes here
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    
    # Redraw all bullets behind player and aliens
    for bullet in bullets:
        bullet.draw_bullet()
    
    for enemy in enemies:
        enemy.blitme()
    
    player.blitme()
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()    

def check_bullets_pos(bullets):
    """ Check if a bullet has gone off the screen. If it has, remove it. """
    for bullet in bullets:
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
            
def update_bullets(bullets, enemies):
    """ Update the position of all bullets in the game. """
    bullets.update()
    
    # Check for any bullets that have hit enemies.
    # If so, get rid of the bullet and the alien.
    collisions = pygame.sprite.groupcollide(enemies, bullets, True, True)
            
def update_enemies(enemies):
    """ Update the position of all enemies in the game. """
    enemies.update()
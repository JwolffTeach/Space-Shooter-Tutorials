"""
Lesson 10 - Multiple Enemies and Keeping Track of Score

Changes to this file:

  1. Increase score on a collision by calling the function settings.increase_score(50)
  2. Added "sb", the scoreboard as a parameter to the update_screen() function definition.
  3. Draw the score information, sb.show_score().
  4. Added "sb", the scoreboard as a parameter to the check_collisions() function definition.
  5. Added sb.prepscore() function call when an enemy is hit.

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

def update_screen(screen, sb, player, enemies, bullets):
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
    
    # Draw the score information.
    sb.show_score()
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()    

def check_bullets_pos(bullets):
    """ Check if a bullet has gone off the screen. If it has, remove it. """
    for bullet in bullets:
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
            
def check_collisions(settings, sb, bullets, enemies):    
    # Check for any bullets that have hit enemies.
    # If so, get rid of the bullet and the alien.
    collisions = pygame.sprite.groupcollide(enemies, bullets, True, True)
    if collisions:
        print(collisions)
        settings.increase_score(settings.enemy_points)
        sb.prep_score()
    
def update_everything(player, bullets, enemies):
    player.update_location()
    bullets.update()
    enemies.update()
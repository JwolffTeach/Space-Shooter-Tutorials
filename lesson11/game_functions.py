"""
Lesson 11 - Waves of enemies

Changes to this file:

  1. import enemy so we can spawn enemies in this file.
  2. import Group from pygame.sprite so we can add enemies to enemies group.
  3. add screen as a parameter to check_collisions
  4. In check_collisions, check the length of enemies. If its <= 0, increase level and call spawn_enemies()

"""

import pygame
from bullet import Bullet
from enemy import Enemy
from pygame.sprite import Group


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
            
def check_collisions(settings, screen, sb, bullets, enemies):    
    # Check for any bullets that have hit enemies.
    # If so, get rid of the bullet and the alien.
    collisions = pygame.sprite.groupcollide(enemies, bullets, True, True)
    if collisions:
        print(collisions)
        settings.increase_score(settings.enemy_points)
        sb.prep_score()
    
    if len(enemies) <= 0:
        # Check the length of enemies. If there are no enemies, increase level by 1 and then call spawn_enemies
        settings.current_level+=1
        spawn_enemies(settings, screen, enemies)
        
def update_everything(player, bullets, enemies):
    player.update_location()
    bullets.update()
    enemies.update()
    
def spawn_enemies(settings, screen, enemies):
    """ Spawn enemies. This should be called for every new level. """
    for i in range(settings.current_level+2):
        enemy = Enemy(settings, screen)
        enemies.add(enemy)
"""
Lesson 14 - Game Over Screen

Changes to this file:

  1. Return True from check_collisions if the player is dead.

"""

import pygame
from bullet import Bullet
from enemy import Enemy
from pygame.sprite import Group


WHITE = (255, 255, 255)

def check_events(settings, screen, player, bullets, gamePaused):
    """ Respond to keypresses and mouse events. """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True # Close the application.
        elif event.type == pygame.MOUSEBUTTONDOWN:
            player.gun.fire_weapon()
    return False # Do NOT close the application.

def pause_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True, False # Close the application.
        elif event.type == pygame.MOUSEBUTTONDOWN:
            return False, False #Game no longer paused.
    return False, True     

def update_screen(screen, sb, player, enemies, bullets, enemy_bullets):
    """ Update images on the screen and flip to the new screen. """
    # --- Screen-clearing code goes here
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    
    # Redraw all bullets behind player and aliens
    for bullet in bullets:
        bullet.draw_bullet()
        
    for bullet in enemy_bullets:
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
            
def check_enemy_bullets_pos(enemy_bullets, settings):    
    """ Check if a bullet has gone off the screen. If it has, remove it. """
    for enemy_bullet in enemy_bullets:
        if enemy_bullet.rect.top > settings.screen_height:
            enemy_bullets.remove(enemy_bullet)
            
def check_collisions(settings, screen, sb, player, bullets, enemies, enemy_bullets):    
    # Check for any bullets that have hit enemies.
    # If so, get rid of the bullet and the alien.
    collisions = pygame.sprite.groupcollide(enemies, bullets, False, True)
    if collisions:
        settings.increase_score(settings.enemy_points)
        for enemy in collisions:
            enemy.healthbar.decrease_hp()
            if enemy.healthbar.hp <= 0:
                enemies.remove(enemy)
                
    player_collisions = pygame.sprite.spritecollide(player, enemy_bullets, True)
    if player_collisions:
        if player.health.decrease_hp(50) == True:
            return True
        
    
    sb.prep_score()
    
    for enemy in enemies:
        # If enemies reach bottom of screen, destroy and subtract 100 from score.
        if enemy.rect.top > settings.screen_height:
            enemies.remove(enemy)
            settings.score -= 100
        if enemy.rect.right >= settings.screen_width or enemy.rect.left <= 0:
            enemy.direction *= -1
    
    if len(enemies) <= 0:
        # Check the length of enemies. If there are no enemies, increase level by 1 and then call spawn_enemies
        settings.current_level+=1
        spawn_enemies(settings, screen, enemies, enemy_bullets)
        
def update_everything(player, bullets, enemies, enemy_bullets):
    player.update_location()
    bullets.update()
    enemy_bullets.update()
    enemies.update()
    
def spawn_enemies(settings, screen, enemies, enemy_bullets):
    """ Spawn enemies. This should be called for every new level. """
    for i in range(settings.current_level+2):
        enemy = Enemy(settings, screen, enemy_bullets)
        enemies.add(enemy)
        


def startGame(player, bullets, enemy_bullets, enemies, settings):
    # This function is used to set values at the beginning of a game, or after restarting.
    player.health.resetHealth()
    bullets.empty()
    enemy_bullets.empty()
    enemies.empty()
    settings.current_level = 1
    settings.score = 0
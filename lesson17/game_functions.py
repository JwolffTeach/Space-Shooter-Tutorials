"""
Lesson 14 - Game Over Screen

Changes to this file:

  1. Return True from check_collisions if the player is dead.

"""

import pygame
from bullet import Bullet
from enemy import Enemy
from powerup import Powerup
from pygame.sprite import Group


WHITE = (255, 255, 255)

def check_events(settings, screen, player, bullets, powerups, gamePaused):
    """ Respond to keypresses and mouse events. """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit  # Close the application.
        elif event.type == pygame.MOUSEBUTTONDOWN:
            player.gun.fire_weapon()
    return False # Do NOT close the application.

def pause_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit  # Close the application.
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Clicked Mouse")
            return False # Game is no longer paused.
    return True # Game is still paused

def update_screen(screen, sb, player, enemies, bullets, enemy_bullets, powerups):
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
        
    for powerup in powerups:
        powerup.blitme()
    
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
            
def check_collisions(settings, screen, sb, player, bullets, enemies, enemy_bullets, powerups):    
    # Check for any bullets that have hit enemies.
    # If so, get rid of the bullet and the alien.
    collisions = pygame.sprite.groupcollide(enemies, bullets, False, False)
    if collisions:
        #for key, value in collisions.items():
            #key.onCollision(value)
            #value.onCollision(key)
        settings.increase_score(settings.enemy_points)
        for enemy in collisions:
            enemy.healthbar.decrease_hp()
            if enemy.healthbar.hp <= 0:
                powerup = Powerup(screen, settings, enemy.rect, 1)
                powerups.add(powerup)
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
        
    # Check if player touches powerup.
    powerup_collisions = pygame.sprite.spritecollide(player, powerups, True)
    if powerup_collisions:
        for powerup in powerup_collisions:
            if player.gun.bulletType < 3.0:
                player.gun.bulletType+=0.1
                print(player.gun.bulletType)
        
def update_everything(player, bullets, enemies, enemy_bullets, powerups):
    player.update_location()
    bullets.update()
    enemy_bullets.update()
    enemies.update()
    powerups.update()
    
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
Lesson name: Lesson 9 - Bullet Collision and Enemy Group

Plan - Check for bullets colliding with enemy. Then make enemies a group, and 
check for bullet scolliding with enemies!


----- Bullet Collision -----

 game_functions
  1. Add enemy as a parameter to update_bullets() function so we can check for collisions between bullets and enemy.
  2. Add collision checking line in update_bullets()

 spaceshooter
  3. Added enemy as a parameter to gf.udpate_bullets() function call.
  

----- Enemy Group -----

 spaceshooter
  4. Make a group of enemies.
  5. Change all parameter uses of "enemy" to "enemies"
    a. gf.update_bullets()
    b. gf.update_enemies()
    c. gf.update_screen()

 game_functions
  6.  Change references from enemy to enemies
    a. update_screen() parameter enemy --> enemies
         - change enemy.blitme() to loop through all enemies and blit them.
    b. update_bullets() parameter enemy --> enemies
         - change spritecollide to be groupcollide
    c. update_enemies() parameter enemy --> enemies
         - enemy.update() --> enemies.update()
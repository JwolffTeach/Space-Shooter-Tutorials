Lesson name: Lesson 8 - Moving the Enemy

Plan - slowly move the enemies down toward the bottom of the screen.

  1. change settings.py
    a. keep track of enemy_speed_factor
  
  2. change enemy.py file
    a. new update() function which moves enemy based on enemy_speed_factor.
    
  3. change spaceshooter.py
    a. call gf.update_enemies() function after update_bullets().
    
  4. change game_functions.py
    a. new function called gf_update_enemies() which will call the enemy.update() function to update position of enemy
    
  5. refactor the bullets.update() to be a function inside game_functions file.
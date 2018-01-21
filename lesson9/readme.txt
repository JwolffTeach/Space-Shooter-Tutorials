Lesson name: Lesson 9 - Bullet Collision and Enemy Group

Plan - Check for bullets colliding with enemy. Then make enemies a group, and 
check for bullet scolliding with enemies!


----- Bullet Collision -----

 game_functions
  1. Added check_collisions() function to check for bullet/enemy collisions.
  2. Refactor: update_everything() function will execute all update functions.

 spaceshooter
  3. Added enemy as a parameter to gf.udpate_bullets() function call.
  

----- Enemy Group -----

 spaceshooter
  4. Make a group of enemies.
  5. Change all parameter uses of "enemy" to "enemies"
    a. gf.update_bullets()
    b. gf.update_enemies()
    c. gf.update_screen()
  6. Refactor: update_[thing] changed to gf.update_everything() call.

 game_functions
  7.  Change references from enemy to enemies
Lesson name: Lesson 11 - Waves of Enemies

Plan - Keep track of the level and spawn new waves of enemies. Every new wave has 1 more enemy. 


----- Waves of Enemies -----

 settings
  1. Added current_level to keep track of the level

 spaceshooter  
  1. Remove the lines that add enemy to enemies group. Call gf.spawn_enemies() instead.
  2. Add screen to the gf.check_collisions() functions.
  
 game_functions
  1. import enemy so we can spawn enemies in this file.
  2. import Group from pygame.sprite so we can add enemies to enemies group.
  3. add screen as a parameter to check_collisions
  4. In check_collisions, check the length of enemies. If its <= 0, increase level and call spawn_enemies()
  
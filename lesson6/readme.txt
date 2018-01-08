Lesson name: Lesson 6 - Deleting Bullets Off Screen

Plan - When a bullet is off the screen ( bullet.y < 0 ), remove it from the group.

  1. Make a new function in game_functions called check_bullets_pos().
    a. bullets is a parameter because we want to check the y position of each bullet.
    b. loop through each bullet, check if the rect.bottom is less than 0. if it is, remove it from the group!
  
  2. In spaceshooter file, call the check_bullets_pos() function after we update it's position.
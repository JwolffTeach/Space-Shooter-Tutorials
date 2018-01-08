Lesson name: Lesson 7 - Creating an Enemy

Plan - Create an enemy class that can be displayed on the screen.

  1. Create the enemy class. 
    a. Enemy class has an image, a rect, and we keep track of it's x and y position as a float value.
    b. Enemy class has a blitme() function to draw it to the screen.
    
  2. spaceshooter.py file is updated:
    a. create an enemy
    b. add it to list of parameters for gf.update_screen() function call.
    
  3. game_functions.py file is updated:
    a. add enemy as a parameter to update_screen() function definition
    b. call the enemy.blitme() function after we blit the player.
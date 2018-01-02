Lesson name: Lesson 4 - Refactor screen updating to game_functions. Restrict the ship's movement so it doesn't go off screen.

  Refactor screen updating to game functions
    1. Add a new function, update_screen(),  to game_functions.py file. 
    2. our update_screen() function needs the following parameters: settings, screen, and player)
      a. player - needed for the player.blitme() function
      b. screen - needed for filling the background of the screen to WHITE.
    3. Move the screen.fill, screen.blit, player.blitme, and display.flip code from spaceshooter.py to game_functions.py update_screen() function.
    4. Get rid of background_image blitting. We will add this back in later, for now, we will just use screen.fill(WHITE)
    5. Add the color WHITE to our game_functions.py file. It should be (255, 255, 255)
  
  Restrict the ship's movement so it doesn't go off screen.
    1. Open ship.py file.
    2. Edit the update_location function:
      a. Check the x position validity. If we've gone outside the screen boundary, then reset position.
      b. Check the y position validity. If we've gone outside the screen boundary, then reset position.
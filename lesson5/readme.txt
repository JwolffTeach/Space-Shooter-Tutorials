Lesson name: Lesson 5 - Shooting Bullets

Plan - Bullet will shoot from the top of the player's ship and will move vertically.

  1. Adding the bullet settings
    a. Update settings.py to include the bullet values we want the game to use.
      i. These include bullet_speed_factor, bullet_width, bullet_height, and bullet_color

  2. Create the Bullet class
        i. Bullet class inherits the properties of pygame's Sprite class.
          - by making a bullet a sprite, we can use the properties of a sprite class, including specificaly the collision property.
          
      a. __init__(self, settings, screen, ship) method
        i. We need the following information to properly spawn, draw, and move a bullet:
          - screen
          - settings ( for screen width/height, bullet width/height, and bullet_speed )
          - bullet's rect
          - bullet's y position ( this is where the bullet will be drawn on the y axis )
          - bullet's color
          - bullet's speed_factor ( how quickly it will move up in our game.
      
      b. update(self) method
        i. Adjust the y position of this bullet, then update the rect's y position.
        
      c. draw_bullet(self) method
        i. Draws the bullet to the screen.
  
  3. The game needs to keep track of all bullets. We will make a group of bullets in spaceshooter.py file.
    a. import Group class from pygame.sprite
    b. after player is defined, make a group to store bullets in. When bullets are created, we will add them to this group.
        
  4. check_events() method in game_functions will create an instance of bullet after fire_weapon() method is executed. Then we need to add this new bullet to our bullets group.
    a. After we fire_weapon(), create a new_bullet with settings, screen, and player parameters.
    b. Then add this new_bullet to our bullets group.
    c. Make sure to pass the bullets group as a parameter into the check_events() function.
    d. Go back to spaceshooter.py file and add bullets as a parameter to the  check_events() function call.
  
  5. Next we need to update the bullet position of every bullet in our bullets group.
    a. Under game logic, after the player's location is updated, we will call bullets.update() to execute the update() function for each bullet.
  
  6. update_screen() function needs to also draw bullets.
    a. Loop through each bullet in bullets and call the draw_bullets() function.
Lesson name: Lesson 10 - Multiple Enemies and Keeping Track of Score

Plan - Start the game with multiple(3) enemies taht are randomly placed above the screen.
Then keep track of a score and display it on the screen. Add points when enemies die.


----- Multiple Enemies -----

 enemy
  1. import random
  2. get a random value for centerx, between the rect width and the screen width.
  3. get a random value for y. Somewhere above the screen, -200 to -500.

 spaceshooter
  1. Start with 2 more enemies for a total of 3. Add enemies to enemies group.
  

----- Keeping track of score -----

 scoreboard
  1. Create a scoreboard class in a new file, scoreboard.py
  2. prep_score() function will set the score to the current score.
  3. show_score() function will draw the score to the screen.

 settings
  1. Added Score variable as self.score
  2. Created a function to increase score, increase_score(self, amount)
  3. Add enemy_points variable as self.enemy_points
  
 game_functions
  1. Increase score on a collision by calling the function settings.increase_score(50)
  2. Added "sb", the scoreboard as a parameter to the update_screen() function definition.
  3. Draw the score information, sb.show_score().
  4. Added "sb", the scoreboard as a parameter to the check_collisions() function definition.
  5. Added sb.prepscore() function call when an enemy is hit.
  
 spaceshooter
  1. Import scoreboard
  2. Create a scoreboard object as "sb".
  3. Add "sb" as a parameter to gf.update_screen() call.
  4. Add "sb" as a parameter to gf.check_collisions() call.
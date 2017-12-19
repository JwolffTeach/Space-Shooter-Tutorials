Lesson name: Lesson 2 - Create a class for spaceship and settings
Changes to this file:
  1. imported Ship class.
  2. removed the shaceship image loading, colorkey, and spaceship_rect.
  3. created an instance of the Ship() class as player with screen as a parameter.
  4. replace the screen.blit() call with the player.blitme() function.
  5. imported Settings class.
  6. replaced size = (700, 500) with settings = Settings()
  7. change the set_mode to use the settings.screen_width and settings.screen_height
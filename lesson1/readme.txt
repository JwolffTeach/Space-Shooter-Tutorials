Lesson name: Lesson 1 - Create a ship_rect to control ship location

Changes to this file:
  - Set the center of spacesihp to be the mouse location
    1. spaceship_rect = spaceship.get_rect()
    2. spaceship_rect.centerx = spaceship_position[0] and
    3. spaceship_rect.centery = spaceship.position[1]
    4. screen.blit(spaceship, spaceship_rect)
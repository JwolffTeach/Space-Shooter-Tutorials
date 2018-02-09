import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (0, 0, 0)

# Initialize pygame, settings, and screen object.
pygame.init()

pygame.display.set_caption("My Game")
screen1 = pygame.display.set_mode( (700, 700) )
screen2 = pygame.display.set_mode( (500, 500) )
screen1.fill(BLACK) 
screen2.fill(WHITE)
screen = screen1

done = False
clock = pygame.time.Clock()

while not done: 
    
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Mousedown works")
            screen = screen2
            screen.fill(WHITE)
            
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)    

# Close the window and quit.
pygame.quit()
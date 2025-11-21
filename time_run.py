# Testing time display

import pygame, time
from display_time import Timing

pygame.init()

# SCREEN
screen = pygame.display.set_mode((500, 250))
pygame.display.set_caption("Testing Time Display")

# Time
timeLimit = 10
startTime = time.time()

# Screen Loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("white")

    # RENDER CODE HERE
    endTime = time.time()
    elapsedTime = round((endTime - startTime), 2)

    timer = timeLimit - int(elapsedTime)

    key = pygame.key.get_pressed()
    if key[pygame.K_RETURN]:
        timer += 5
        showTime = Timing(f"{timer}").displayTime(screen)
    else:
        showTime = Timing(f"{timer}").displayTime(screen)
        
    pygame.display.flip()

pygame.quit()

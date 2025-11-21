# Testing time display

import pygame, time
from display_time import displayTiming

pygame.init()

# CLOCK
clock = pygame.time.Clock()

# SCREEN
screen = pygame.display.set_mode((500, 250))
pygame.display.set_caption("Testing Time Display")

# TIME
timeLimit = 60

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

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RETURN]:
        timeLimit += 5

    timer = timeLimit - int(elapsedTime)
    
    showTime = displayTiming(timer).displayTimeFont(screen)

    pygame.display.flip()

    clock.tick(20)

pygame.quit()

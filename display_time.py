import pygame, time

pygame.init()

class displayTiming:
    def __init__(self, text, x_pos, y_pos):
        self.text = str(text)
        self.x_pos = x_pos
        self.y_pos = y_pos

    def displayTimeFont(self, screen):
        createFont = pygame.font.SysFont("Arial", 30)

        renderFont = createFont.render(self.text, False, "black")

        screen.blit(renderFont, (self.x_pos, self.y_pos))

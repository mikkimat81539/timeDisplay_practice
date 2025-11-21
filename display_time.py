import pygame, time

pygame.init()

class displayTiming:
    def __init__(self, text):
        self.text = str(text)

    def displayTimeFont(self, screen):
        createFont = pygame.font.SysFont("Arial", 30)

        renderFont = createFont.render(self.text, False, "black")

        screen.blit(renderFont, (200, 100))

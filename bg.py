import pygame
from screen import screen


class Background:
    def __init__(self, x, y):
        self.background = pygame.image.load("bg.gif")
        self.x = x
        self.y = y

    def draw(self):
        screen.canvas.blit(self.background, (self.x, self.y))

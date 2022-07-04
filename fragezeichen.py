import pygame
from screen import screen


class Fragezeichen:
    def __init__(self, x, y):
        self.img_on = pygame.image.load("fragezeichen.gif")
        self.img_off = pygame.image.load("fragezeichen_aus.gif")
        self.current_state = self.img_on
        self.rect = self.current_state.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

    def draw(self, velocityx, velocityy):
        screen.canvas2.blit(self.current_state, (self.x, self.y))
        self.x += velocityx
        self.y += velocityy

    def drawrect(self):
        pygame.draw.rect(screen.canvas2, (100, 100, 100), self.rect)

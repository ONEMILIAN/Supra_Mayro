import pygame
from screen import screen


class Player:
    def __init__(self, x, y):
        self.right = pygame.image.load("player_right.gif")
        self.left = pygame.image.load("player_left.gif")
        self.current_img = self.right
        self.rect = self.current_img.get_rect()
        self.life = 5
        self.x = x
        self.y = y

    def draw(self):
        screen.screen.blit(self.current_img, (self.x, self.y))

    def movement(self, playerxchange, playerychange):
        self.x += playerxchange
        self.y += playerychange
        self.rect.x = self.x
        self.rect.y = self.y

    def drawhitbox(self):
        pygame.draw.rect(screen.screen, (100, 100, 100), self.rect)

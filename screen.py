import pygame


class Screen:
    def __init__(self, width, height,  x, y):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.canvas = pygame.surface.Surface((width, height))
        self.canvas2 = pygame.surface.Surface((width, height))
        pygame.display.set_caption("SUPRA MAYRO")
        self.clock.tick(60)
        self.x = x
        self.y = y

    def drawcanvas(self):
        screen.screen.blit(screen.canvas, (self.x, self.y))

    def drawcanvas2(self):
        screen.screen.blit(screen.canvas2, (self.x, self.y))


screen = Screen( 800, 400, 0, 0)

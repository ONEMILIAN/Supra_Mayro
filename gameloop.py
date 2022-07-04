import pygame
import sys
from screen import screen
from bg import Background
from fragezeichen import Fragezeichen
from player import Player


class Gameloop:

    def __init__(self):
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            player.drawhitbox()

            screen.drawcanvas()
            screen.drawcanvas2()
            bg.draw()

            player.draw()
            fragezeichen1.drawrect()
            fragezeichen1.draw(0, 0)

            pygame.display.update()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_a]:
                player.movement(-0.1, 0)
                player.current_img = player.left


            if keys[pygame.K_d]:
                player.movement(0.1, 0)
                player.current_img = player.right


gameloop = Gameloop()
fragezeichen1 = Fragezeichen(300, 200)
bg = Background(0, 0)
player = Player(200, 250)

gameloop.run()

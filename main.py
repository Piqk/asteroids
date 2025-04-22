
import pygame # type: ignore
from constants import *
from player import Player

def main():
    pygame.init()
    print(f'Starting Asteroids! \n Screen width: {SCREEN_WIDTH} \n Screen height: {SCREEN_HEIGHT}')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    dt = 0
    x_cor = SCREEN_WIDTH/2
    y_cor = SCREEN_HEIGHT/2
    triangle = Player(x_cor, y_cor)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('#000000', rect=None, special_flags=0)
        triangle.draw(screen)
        pygame.display.flip()
        fps.tick(60)
        dt = fps.tick(60) / 1000
        

if __name__ == "__main__":
    main()

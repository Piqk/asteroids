
import pygame # type: ignore
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
import sys

def main():
    pygame.init()
    print(f'Starting Asteroids! \n Screen width: {SCREEN_WIDTH} \n Screen height: {SCREEN_HEIGHT}')
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    triangle = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('#000000')
        for draw in drawable:
            draw.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(triangle) is True:
                sys.exit("Game Over!")
        pygame.display.flip()
        dt = fps.tick(60) / 1000
        

if __name__ == "__main__":
    main()

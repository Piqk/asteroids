
import pygame # type: ignore
from constants import *
from player import Player # type: ignore
from asteroids import Asteroid # type: ignore
from asteroidfield import AsteroidField # type: ignore
from shot import Shot # type: ignore
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
    shots = pygame.sprite.Group()
    Shot.containers = (updatable, drawable, shots)
    Player.containers = (updatable, drawable, shots)
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
            for shot in shots:
                if shot.collision(asteroid) is True:
                    asteroid.split()
                    shot.kill()
        pygame.display.flip()
        dt = fps.tick(60) / 1000
        

if __name__ == "__main__":
    main()

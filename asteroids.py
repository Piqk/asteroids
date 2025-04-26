from circleshape import CircleShape # type: ignore
import pygame  # type: ignore
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            split_angle = random.uniform(20, 50)
            angle_1 = self.velocity.rotate(split_angle)
            angle_2 = self.velocity.rotate(-split_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            aster_1 = Asteroid(self.position.x, self.position.y, new_radius)
            aster_2 = Asteroid(self.position.x, self.position.y, new_radius)
            aster_1.velocity = angle_1 * 1.2
            aster_2.velocity = angle_2 * 1.2
            return aster_2, aster_1

            




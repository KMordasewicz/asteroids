from constants import ASTEROID_MIN_RADIUS
import pygame
import random
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color=(255, 255, 255),
            center=self.position,
            radius=self.radius,
            width=2
        )


    def update(self, dt):
        self.position += self.velocity * dt


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20., 50.)
        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(-angle)
        aster1 = Asteroid(
            self.position.x,
            self.position.y,
            self.radius - ASTEROID_MIN_RADIUS
        )
        aster1.velocity = v1 * 1.2
        aster2 = Asteroid(
            self.position.x,
            self.position.y,
            self.radius - ASTEROID_MIN_RADIUS
        )
        aster2.velocity = v2 * 1.2

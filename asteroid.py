import pygame
import random

from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "pink", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            newAngle = random.uniform(20, 50)
            newRadius = self.radius - ASTEROID_MIN_RADIUS

            firstSplit = self.velocity.rotate(newAngle)
            secondSplit = self.velocity.rotate(-newAngle)

            firstAsteroid = Asteroid(self.position.x, self.position.y, newRadius)
            secondAsteroid = Asteroid(self.position.x, self.position.y, newRadius)

            firstAsteroid.velocity = firstSplit * 1.2
            secondAsteroid.velocity = secondSplit * 1.2
            


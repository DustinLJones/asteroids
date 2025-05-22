import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        return pygame.draw.circle(screen, (255, 255, 255), ((self.position.x), (self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # Remove the original asteroid
        self.kill()

        # If the asteroid is too small, do not split
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Create two smaller asteroids
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_vectors = [
            self.velocity.rotate(random_angle),
            self.velocity.rotate(-random_angle)
        ]
        
        for vector in new_vectors:
            new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid.velocity = vector * 1.2
            #new_asteroid.add(self.containers)

        
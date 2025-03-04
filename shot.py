from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, SHOT_RADIUS)

	def update(self, dt):
		self.move(dt)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, 2)

	def move(self, dt):
		self.position += self.velocity * dt

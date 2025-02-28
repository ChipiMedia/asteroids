from circleshape import CircleShape
import pygame
import random
from constants import *

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, (255,255,255), (int(self.position.x), int(self.position.y)), self.radius, 2)

	def update(self, dt):
		self.position += self.velocity * dt

	def split(self):
		old_radius = self.radius
		new_radius = old_radius - ASTEROID_MIN_RADIUS
		position_x = self.position.x
		position_y = self.position.y
		self.kill()

		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		else:
			random_angle = random.uniform(20, 50)
			vector_pos = self.velocity.rotate(random_angle)
			vector_neg = self.velocity.rotate(-random_angle)

			asteroid_pos = Asteroid(position_x, position_y, new_radius)
			asteroid_neg = Asteroid(position_x, position_y, new_radius)
			asteroid_pos.velocity = vector_pos * 1.2
			asteroid_neg.velocity = vector_neg * 1.2 

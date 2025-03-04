import pygame
from pygame.locals import *
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from pygame.math import Vector2
from shot import Shot

def main():
	pygame.init()
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable,)
	asteroid_field = AsteroidField()
	Shot.containers = (shots, drawable, updatable)


	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill("black")
		updatable.update(dt)
		for asteroid in asteroids:
			if player.is_colliding(asteroid):
				print("Game over!")
				sys.exit()
		for asteroid in asteroids:
			for shot in shots:
				if shot.is_colliding(asteroid):
					asteroid.split()
					shot.kill()
		for shot in shots:
			shot.move(dt)
		for d in drawable:
			d.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()

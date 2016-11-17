import sys
import pygame

def check_events(hero):
	"""Respond to kepyresses and mouse events."""
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				hero.move_flags["up"] = True
			elif event.key == pygame.K_DOWN:
				hero.move_flags["down"] = True
			elif event.key == pygame.K_LEFT:
				hero.move_flags["left"] = True
			elif event.key == pygame.K_RIGHT:
				hero.move_flags["right"] = True
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				hero.move_flags["up"] = False 
			elif event.key == pygame.K_DOWN:
				hero.move_flags["down"] = False
			elif event.key == pygame.K_LEFT:
				hero.move_flags["left"] = False
			elif event.key == pygame.K_RIGHT:
				hero.move_flags["right"] = False
		elif event.type == pygame.QUIT:
			sys.exit()

def update_screen(settings, screen, hero):
	"""Update sprites and flip to new screen."""

	hero.blitme()
	pygame.display.flip()

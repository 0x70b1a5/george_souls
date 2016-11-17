import pygame
import pdb

from settings import Settings
from hero import Hero
import game_functions as gf

def run():
	"""Init game and create screen object."""
	pygame.init()
	sets = Settings()
	screen = pygame.display.set_mode(
		(sets.screen_width, sets.screen_height))
	pygame.display.set_caption("George Souls")

	# Create hero
	hero = Hero(sets, screen)

	# Main game loop
	while True:
		gf.check_events(hero)
		hero.update()
		gf.update_screen(sets, screen, hero)

run()

import sys
import pygame
import pdb
from settings import Settings
from hero import Hero

def run():
	"""Init game and create screen object."""
	pygame.init()
	sets = Settings()
	screen = pygame.display.set_mode(
		(sets.screen_width, sets.screen_height))
	pygame.display.set_caption("George Souls")

	# Create hero
	hero = Hero(screen)

	# Main game loop
	while True:
		# Listen kb, mouse
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		# Redraw screen
		hero.blitme()

		# Render(?) screen
		pygame.display.flip()

run()

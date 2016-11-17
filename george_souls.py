import sys
import pygame

def run():
	"""Init game and create screen object."""
	pygame.init()
	screen = pygame.display.set_mode((1200,800))
	pygame.display.set_caption("George Souls")
	# Main game loop
	while True:
		# Listen kb, mouse
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		# Make msot recently drawn screen visible
		pygame.display.flip()

run()

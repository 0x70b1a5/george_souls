import pygame

class Hero():

	def __init__(self, sets, screen):
		"""Initialize the hero and set starting position."""
		self.screen = screen
		self.sets = sets

		# Load hero image.
		# thank you Redshrike. http://opengameart.org/content/16x16-16x24-32x32-rpg-enemies-updated
		self.image = pygame.image.load('images/sprat.gif')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# Hero begins at bottom-center of screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# Decimal value for position
		self.x = self.rect.centerx
		self.y = self.rect.centery

		# Movement flags
		self.move_flags = {"up":False,"down":False,"left":False,"right":False}

	def update(self):
		"""Moves hero if move flags are on."""
		for direction in self.move_flags:
			if self.move_flags[direction]:
				px = self.sets.speed
				if direction == "up" and self.rect.top > self.screen_rect.top:
					self.y -= px
				elif direction == "down" and self.rect.bottom < self.screen_rect.bottom:
					self.y += px
				elif direction == "left" and self.rect.left > self.screen_rect.left:
					self.x -= px
				elif direction == "right" and self.rect.right < self.screen_rect.right:
					self.x += px

		self.rect.centerx = self.x
		self.rect.centery = self.y

	def blitme(self):
		"""Draw the hero at its current location."""
		self.screen.blit(self.image, self.rect)

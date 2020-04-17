import pygame
import os

class Card():

	def __init__(self, rank, suit, surface):
		self.rank = rank
		self.suit = suit
		self.surface = surface
		if self.rank == "j" or self.rank == "q" or self.rank == "k":
			self.value = 10
		else:
			self.value = self.rank
		self.name = self.rank + self.suit
		folder = "PNG"
		try:
			self.sprite = pygame.image.load(os.path.join(folder, self.name + ".png"))
		except:
			msg = "Unfortunately we could load one of the files."
			raise Exception(UserWarning, msg)

	def render(self, posX, posY):
		self.surface.blit(self.sprite, (posX, posY))

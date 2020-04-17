import pygame
import os
from Card import Card
from Deck import Deck
from Helpers import write
from Helpers import color
from PlayGame import playGame

class Game():

	money = 1000
	playtime = 0
	playing = False
	betting = True
	bet = 0

	def __init__(self, width, height, fps):
		pygame.init()
		self.width = width
		self.height = height
		self.fps = fps
		self.clock = pygame.time.Clock()
		self.display = pygame.display.set_mode((self.width, self.height), pygame.HWSURFACE | pygame.DOUBLEBUF)
		self.running = True
		self.load()

	def load(self):
		folder = "PNG"
		try:
			self.backCard = pygame.image.load(os.path.join(folder, "yellow_back.png"))
		except:
			msg = "Unfortunately we could load one of the files."
			raise Exception(UserWarning, msg)

	def clear_screen(self):
		self.screen.fill(color("green"))

	def starting_screen(self):
		self.screen = pygame.Surface(self.display.get_size())
		self.clear_screen()
		self.screen = self.screen.convert()
		write(self.screen, "BLACKJACK", 64, color("black"), (self.width/2, self.height/2 - self.height/4))
		pygame.draw.rect(self.screen, color("white"), (self.width/2, self.height/2, 120, 60))
		write(self.screen, "PLAY", 48, color("black"), (self.width/2 + 10, self.height/2 + 10))

	def display_stats(self):
		write(self.screen, str(self.money) + "$", 32, color("black"), (10, 10))

	def reset(self):
		self.playtime = 0
		self.money = 1000
		self.betting = True
		self.bet = 0
		self.distributing = True

	def play(self):
		playGame(self)

	def run(self):
		milliseconds = self.clock.tick(self.fps)
		self.seconds = milliseconds / 1000.0
		self.playtime += self.seconds
		self.starting_screen()
		self.deck = Deck(self.width/2 - self.width/4, self.height/2 - self.height/4, self.screen)
		self.deck.generate(self.backCard)
		self.dealer = Deck(self.width/2 - self.width/4, self.height/2 - self.height/4, self.screen)
		self.deck.draw(2, self.dealer)
		self.player = Deck(self.width/2 - self.width/4, self.height/2 - self.height/4, self.screen)
		self.deck.draw(2, self.player)
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
					break
				elif event.type == pygame.K_ESCAPE:
					self.running = False
					break
			# get user input
			self.pressedKeys = pygame.key.get_pressed()
			if self.playing is True:
				self.play()
			else:
				if self.pressedKeys[pygame.K_RETURN]:
					self.playing = True
					self.reset()
			self.display.blit(self.screen, (0,0))
			pygame.display.set_caption("FPS: %s" % (self.clock.get_fps()))
			pygame.display.update()	
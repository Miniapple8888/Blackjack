import pygame
from Helpers import write
from Helpers import color

def playGame(game):
	game.clear_screen()
	game.display_stats()

	# Bet
	# Money input from user
	if game.betting:
		write(game.screen, "BET", 54, color("black"), (game.width/2 - 20, game.height/2 - 54))
		write(game.screen, str(game.bet), 48, color("black"), (game.width/2 - 20, game.height/2+10))
		write(game.screen, "Press a to increase and d to decrease, Press b to bet!", 32, color("black"), (game.width/8, game.height/2+64))
		if game.pressedKeys[pygame.K_b]:
			if game.bet > game.money or game.bet <= 0:
				write(game.screen, "Not enough money", 32, color("black"), (game.width/3, game.height/2+90))
			else:
				game.betting = False
				game.money -= game.bet
		elif game.pressedKeys[pygame.K_a]:
			game.bet += 10
		elif game.pressedKeys[pygame.K_d]:
			if game.bet > 0:
				game.bet -= 10
	else:
		# Distribute cards
		if game.distributing:
			# display user cards
			cardY = game.height * 3/4
			cardX = game.width/2 - 100
			for card in game.player.cards:
				card.render(cardX, cardY)
				cardX += 25
		# Actions of user

		# Determine who wins

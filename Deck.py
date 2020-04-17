from Card import Card
from random import *

class Deck():

  def __init__(self, pos_x, pos_y, surface):
    self.cards = []
    self.pos_x = pos_x
    self.pos_y = pos_y
    self.surface = surface

  def generate(self, sprite):
    # Heart, diamond, clover ,spade
    suits = ["h", "d", "c", "s"]
    ranks = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k"]
    for suit in suits:
      for rank in ranks:
        c = Card(rank, suit, self.surface)
        self.cards.append(c)
    # animation generate stack
    self.surface.blit(sprite, (self.pos_x, self.pos_y))

  # Draws a card from the deck and transfers it to another deck
  def draw(self, number, deck):
    for x in range(number):
      index = randrange(len(self.cards))
      card = self.cards[index]
      deck.cards.append(card)
      self.cards.remove(card)



  
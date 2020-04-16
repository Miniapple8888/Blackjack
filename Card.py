class Card():

  def __init__(self, rank, suit):
    self.rank = rank
    self.suit = suit
    if self.rank == "j" or self.rank == "q" or self.rank == "k":
      self.value = 10
    else:
      self.value = self.rank
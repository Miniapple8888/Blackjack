# in python, we have what we call modules and we can import them like this:
import pygame
import os
from Card import Card
from Deck import Deck
from Helpers import write
from Helpers import color

# then we need to initialize pygame
pygame.init()

# then we need a surface to work on, a displayable one, arg: width, height (in a tuple)
width = 640
height = 480
display = pygame.display.set_mode((width, height), pygame.HWSURFACE | pygame.DOUBLEBUF)
# these are constants we don't have to worry about that

# Loading assets
folder = "PNG"
backcard = pygame.image.load(os.path.join(folder, "yellow_back.png"))

# title on top
pygame.display.set_caption("Blackjack!")

# we need a surface (Surface class)
green = (30, 245, 45)
screen = pygame.Surface(display.get_size())
screen.convert()
screen.fill(green)

# Starting screen
write(screen, "BLACKJACK", 64, color("black"), (width/2, height/2 - height/4))
pygame.draw.rect(screen, color("white"), (width/2, height/2, 120, 60))
write(screen, "PLAY", 48, color("black"), (width/2 + 10, height/2 + 10))

# Game variables and stuff
number_of_chips = 1000
deck = Deck(width/2 - width/4, height/2 - height/4, screen)
deck.generate(backcard)
dealer = Deck(width/2 - width/4, height/2 - height/4, screen)
deck.draw(2, dealer)
player = Deck(width/2 - width/4, height/2 - height/4, screen)
deck.draw(2, player)

while True:
  # to escape
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      break
    elif event.type == pygame.K_ESCAPE:
      break
  
  mouse = pygame.mouse.get_pos()
  if mouse[0] 
  
  # Update screen
  display.blit(screen, (0,0))
  pygame.display.update()
# im going to go for a moment, search up the pygame documentation
# alright are you lost?
# Alright so, I'll explain some concepts
# First of all, motion is part of your perception
# Frames create the illusion of motion
# We'll be reliant on that (fps) to make the game
# then there's the screen position
# 0,0 means top left corner
# let's say we have a square of 360
# 360,360 would be the coords/position to the bottom right corner
# I*-
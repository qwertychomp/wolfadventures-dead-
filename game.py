import pygame 
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((700, 700))
run = True
px = 0
py = 0
bg = pygame.image.load("assets/canvas.png")
class Player(pygame.sprite.Sprite):
	def  __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("assets/wolf.jpeg")	
player1 = Player()
while run:
	screen.fill((0,0,0))
	for event in pygame.event.get():
		keypress = pygame.key.get_pressed()
		if keypress[pygame.K_RIGHT]:
			px = px + 5
		if keypress[pygame.K_LEFT]:
			px = px - 5
		if keypress[pygame.K_DOWN]:
			py = py + 5
		if keypress[pygame.K_UP]:
			py = py - 5
	screen.blit(bg, (0, 0))
	screen.blit(player1.image, (px, py))
	pygame.display.update()

	

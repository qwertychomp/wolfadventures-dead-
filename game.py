import pygame 
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((700, 700))
run = True
px = 0
py = 0
bg = pygame.image.load("assets/canvas.png")
unscaledfloorimg = pygame.image.load("assets/floor.png")
floorimg = pygame.transform.scale(unscaledfloorimg, (1400, 10)) 
class Player(pygame.sprite.Sprite):
	def  __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("assets/wolf.jpeg")
class Ground(pygame.sprite.Sprite):
	def  __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = floorimg	
player1 = Player()
floor = Ground()
while run:
	screen.fill((0,0,0))
	for event in pygame.event.get():
		keypress = pygame.key.get_pressed()
		if keypress[pygame.K_RIGHT]:
			px = px + 5
		if keypress[pygame.K_LEFT]:
			px = px - 5
		if keypress[pygame.K_DOWN] and py != 325:
			py = py + 5
		if keypress[pygame.K_UP]:
			py = py - 5
	screen.blit(bg, (0, 0))
	screen.blit(player1.image, (px, py))
	screen.blit(floor.image, (0, 450))
	pygame.display.update()

	

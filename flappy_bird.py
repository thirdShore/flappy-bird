

import pygame, sys

class Bird():
	def __init__(self):
		self.birdStatus = [
			pygame.image.load("bird0_0.png"),
			pygame.image.load("bird0_1.png"),
			pygame.image.load("bird0_2.png"),
			pygame.image.load("dead.png")
		]
		self.status = 0
		self.birdx = 50
		self.birdy = 250
		self.jump = False
		self.jumpHeight = 10
		self.downHeight = 1
		self.dead = False
	#to move bird	
	def birdMove(self):
		if self.jump:
			self.jumpHeight = self.jumpHeight - 1
			self.birdy = self.birdy - self.jumpHeight
		else:
			self.downHeight += 0.1
			self.birdy += self.downHeight


class Pipe():
	def __init__(self):
		pass
	#to move pipe
	def pipeMove(self):
		pass

def createMap():
	screen.blit(background, (0, 0))
	#show bird
	if Bird.dead:
		Bird.status = 3
	elif Bird.jump:
		Bird.status = 0
	else:
		Bird.status = 2

	screen.blit(Bird.birdStatus[Bird.status], (int(Bird.birdx), int(Bird.birdy)))
	Bird.birdMove()
	pygame.display.update()

if __name__ == '__main__':
	pygame.init()
	size = (288, 512)
	screen = pygame.display.set_mode(size)
	clock = pygame.time.Clock()
	Bird = Bird()
	
	while True:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					Bird.jump = True
					Bird.jumpHeight = 10
					Bird.downHeight = 1
		background = pygame.image.load("bg_day.png")
		createMap()
	pygame.QUIT()


import pygame, sys

class Bird():
	def __init__(self):
		self.birdRect = pygame.Rect(40, 250, 40, 30)
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
		self.downHeight = 0.5
		self.dead = False
	#to move bird	
	def birdMove(self):
		if self.jump:
			self.jumpHeight = self.jumpHeight - 1
			self.birdy = self.birdy - self.jumpHeight
		else:
			self.downHeight += 0.1
			self.birdy += self.downHeight
			self.birdRect[1] = int(self.birdy)


class Pipe():
	def __init__(self):
		self.wallx = 180
		self.pipeUp = pygame.image.load("pipe_up.png")
		self.pipeDown = pygame.image.load("pipe_down.png")
	#to move pipe
	def pipeMove(self):
		self.wallx -= 2
		if self.wallx < -42:
			global score
			score += 10
			scoreSound.play()
			self.wallx = 300

# def checkDead():
# 	rectUp = pygame.Rect(Pipe.wallx, 362, Pipe.pipeUp.get_width(), Pipe.pipeUp.get_height())
# 	rectDown = pygame.Rect(Pipe.wallx, -150, Pipe.pipeUp.get_width(), Pipe.pipeUp.get_height())
# 	if rectUp.colliderect(Bird.birdRect) or rectDown.colliderect(Bird.birdRect):
# 		Bird.dead = True
# 	if 0 < Bird.birdRect[1] < 512:
# 		Bird.dead = True
# 		return True
# 	else:
# 		return False

def createMap():
	screen.blit(background, (0, 0))
	#show pipe
	screen.blit(Pipe.pipeDown, (int(Pipe.wallx), -150))
	screen.blit(Pipe.pipeUp, (int(Pipe.wallx), 362))
	#show bird
	if Bird.dead:
		Bird.status = 3
	elif Bird.jump:
		Bird.status = 0
	else:
		Bird.status = 2

	screen.blit(Bird.birdStatus[Bird.status], (int(Bird.birdx), int(Bird.birdy)))
	Bird.birdMove()
	Pipe.pipeMove()
	#show font
	screen.blit(font.render('Score:'+ str(score), 1, (255, 255, 255)), (80, 20))
	pygame.display.update()

#setup sound
pygame.mixer.init()
pygame.mixer.music.load('music.ogg')
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True
jumpSound = pygame.mixer.Sound('jump.ogg')
scoreSound = pygame.mixer.Sound('score.ogg')

if __name__ == '__main__':
	pygame.init()
	pygame.mixer.init()
	pygame.font.init()
	font = pygame.font.SysFont(None, 40)
	size = (288, 512)
	screen = pygame.display.set_mode(size)
	clock = pygame.time.Clock()
	Bird = Bird()
	Pipe = Pipe()
	score = 0
	while True:
		#pygame.mixer.music.play()
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					jumpSound.play()
					Bird.jump = True
					Bird.jumpHeight = 10
					Bird.downHeight = 1

		background = pygame.image.load("bg_day.png")
		# if checkDead():
		# 	#getResult()
		# 	pass
		# else:
		createMap()
	pygame.QUIT()
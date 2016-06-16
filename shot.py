import pygame,  game, sys, math, tank

class Shot():
	def __init__(self,x,y,richtung):
		#wichtigste variablen
		self.life = 120
		self.richtung = richtung
		self.x = x + 9
		self.y = y + 16
		self.speed = 7
		if self.richtung == 2 or self.richtung == 3:
			self.x = x + 16
			self.y = y + 9
		self.rect = pygame.Rect(self.x, self.y, 4, 6)
		self.shotimage = pygame.image.load('images/shot.bmp').convert_alpha()
		
		if self.richtung == 2 or self.richtung == 3:
			self.shotimage = pygame.transform.rotate(self.shotimage,90)
	
	def update(self):
		self.rect = pygame.Rect(self.x, self.y, 4, 6)
		self.life -= 1
		if self.richtung == 0:
			self.move_up()
		elif self.richtung == 1:	
			self.move_down()
		elif self.richtung == 2:	
			self.move_right()
		elif self.richtung == 3:	
			self.move_left()
			
	def draw(self):
		game.display.blit(self.shotimage, self.rect)
		
	def move_down(self):
		self.y = self.y + self.speed
		
		
	def move_up(self):
		self.y = self.y - self.speed
		
		
	def move_right(self):
		self.x = self.x + self.speed
		
		
	def move_left(self):
		self.x = self.x - self.speed
		
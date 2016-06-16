import pygame, game, sys, math, shot

class Tank():
	def __init__(self,name,x,y,keyset):
		#alle wichtigen variablen werden definiert
		self.speed = 2 #geschwindigkeit mit der sich der panzer bewegt
		self.shotsfired = 0 #gibt an ob der Panzer bereits geschossen 
		self.life = 10
		self.dmg = 2
		self.keyset = keyset
		self.x = x
		self.y = y
		self.richtung = 1 # 0 = up 1 = down 2 = right 3 = left 
		self.shots = []
		self.name = name
		self.points = 0
		self.rect = pygame.Rect(self.x, self.y, 20, 32)
		self.maxlife = 10
		
		#hier werden die verschiedenen bilder geladen und in alle richtungen gedreht
		self.bodyimage = pygame.image.load('images/'+ name+'Tank.bmp').convert_alpha()
		self.bodyup = pygame.transform.rotate(self.bodyimage,180)
		self.bodydown = pygame.image.load('images/'+ name+'Tank.bmp').convert_alpha()
		self.bodyleft =  pygame.transform.rotate(self.bodyimage,270)
		self.bodyright	=  pygame.transform.rotate(self.bodyimage,90)
		
		
		
		
		
		
		
		
	def draw(self):
		self.rect = pygame.Rect(self.x, self.y, 20, 32)
		game.display.blit(self.bodyimage, self.rect)
		self.shots = [shot for shot in self.shots if shot.life > 0]
		
		for shot in self.shots:
			shot.update()
			shot.draw()
		
		
	def update(self):
		if self.shotsfired > 0: 
			self.shotsfired = self.shotsfired -1
		pressed_keys = pygame.key.get_pressed()
		if self.keyset == 0:
			if pressed_keys[pygame.K_SPACE] and self.shotsfired == 0: 
				self.shot()
			elif pressed_keys[pygame.K_s]:
				self.move_down()
			elif pressed_keys[pygame.K_w]:
				self.move_up()
			elif pressed_keys[pygame.K_a]:
				self.move_left()
			elif pressed_keys[pygame.K_d]:
				self.move_right()
			elif pressed_keys[pygame.K_ESCAPE]:
				pygame.quit()
				sys.exit()
			
		elif self.keyset == 1:		
			if pressed_keys[pygame.K_RETURN] and self.shotsfired == 0: 
				self.shot()
				
			elif pressed_keys[pygame.K_DOWN]:
				self.move_down()
			elif pressed_keys[pygame.K_UP]:
				self.move_up()
			elif pressed_keys[pygame.K_LEFT]:
				self.move_left()
			elif pressed_keys[pygame.K_RIGHT]:
				self.move_right()
			elif pressed_keys[pygame.K_ESCAPE]:
				pygame.quit()
				sys.exit()
		if self.richtung == 1:
			self.y = self.y + self.speed
		elif self.richtung == 0:
			self.y = self.y - self.speed
		elif self.richtung == 2:
			self.x = self.x + self.speed
		elif self.richtung == 3:
			self.x = self.x - self.speed
				
	def shot(self):
		self.shotsfired = 15
		self.shots.append(shot.Shot(self.x, self.y, self.richtung))
		print(self.name + "shot")
		
	def move_down(self):
		
		self.bodyimage = self.bodydown
		self.richtung = 1
		
	def move_up(self):
		
		self.bodyimage = self.bodyup
		self.richtung = 0
		
	def move_right(self):
		
		self.bodyimage = self.bodyright
		self.richtung = 2
		
	def move_left(self):
		
		self.bodyimage = self.bodyleft
		self.richtung = 3
		
		
		
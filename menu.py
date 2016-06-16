import pygame, game, sys, math, tank 

class Menu():
	def __init__(self):
		self.status = 0 # 0 = menu 1 = start 2 = options
		self.font = pygame.font.Font(None, 36)
		self.fontunderline = pygame.font.Font(None, 36)
		self.fontunderline.set_underline(True)
		self.selectedoption = 0 #0 = start 1 = options 2 = quit
		self.wait = 0
		self.waitselect = 0
	def draw(self):
		game.display.fill((0,0,0))
		if self.selectedoption == 0:
			start = self.fontunderline.render("Start", 1, (255, 255, 255))
		else:
			start = self.font.render("Start", 1, (255, 255, 255))
		if self.selectedoption == 1:
			options = self.fontunderline.render("Options", 1, (255, 255, 255))
		else:
			options = self.font.render("Options", 1, (255, 255, 255))
		if self.selectedoption == 2:
			quit = self.fontunderline.render("Quit", 1, (255, 255, 255))
		else:	
			quit = self.font.render("Quit", 1, (255, 255, 255))
		
		
		game.display.blit(quit, pygame.Rect(280, 300, 20, 20))
		game.display.blit(options, pygame.Rect(280, 200, 20, 20))
		game.display.blit(start, pygame.Rect(280, 100, 20, 20))
		
	def update(self):
		pressed_keys = pygame.key.get_pressed()
		if pressed_keys[pygame.K_SPACE] or pressed_keys[pygame.K_RETURN]: 
			if self.selectedoption == 0:
				self.status = 1 
				game.greentank.life = game.greentank.maxlife
				game.redtank.life = game.redtank.maxlife
				game.greentank.points = 0
				game.redtank.points = 0
				game.greentank.x = 580
				game.greentank.y = 421
				game.redtank.x = 20
				game.redtank.y = 40
			elif self.selectedoption == 1:
				self.status = 2
			elif self.selectedoption == 2:
				pygame.quit()
				sys.exit()
			self.waitselect = 5	
		elif pressed_keys[pygame.K_DOWN] and self.wait == 0:
			self.wait = 10
			if self.selectedoption == 2:
				self.selectedoption = 0
			else:
				self.selectedoption = self.selectedoption + 1
		elif pressed_keys[pygame.K_UP] and self.wait == 0:
			self.wait = 10
			if self.selectedoption == 0:
				self.selectedoption = 2
			else:
				self.selectedoption = self.selectedoption - 1
		elif pressed_keys[pygame.K_ESCAPE]:
			pygame.quit()
			sys.exit()
		if self.wait > 0:
			self.wait = self.wait -1 
		if self.waitselect > 0:
			self.waitselect = self.waitselect -1 
import pygame, game, sys, math, menu

class Options():
	def __init__(self):
		
		self.font = pygame.font.Font(None, 36)
		self.fontunderline = pygame.font.Font(None, 36)
		self.fontunderline.set_underline(True)
		self.selectedoption = 0 #0 = player1 1 = player2 2 = back
		self.wait = 0
		self.statsetp1 = 0 #0 default h10 s2 d2 1 speed h8 s4 d2 2 tank h12 s1 d3 
		self.statsetp2 = 0 
		self.waitselect = 0
	def draw(self):
		game.display.fill((0,0,0))
		#hier werden die Stats der spieler angezeigt
		statsp1life = self.font.render("life: " + str(game.redtank.maxlife)    , 1, (255, 255, 255))
		statsp1dmg = self.font.render("DMG: " + str(game.redtank.dmg)    , 1, (255, 255, 255))
		statsp1speed = self.font.render("Speed: " + str(game.redtank.speed)    , 1, (255, 255, 255))
		
		statsp2life = self.font.render("life: " + str(game.greentank.maxlife)    , 1, (255, 255, 255))
		statsp2dmg = self.font.render("DMG: " + str(game.greentank.dmg)    , 1, (255, 255, 255))
		statsp2speed = self.font.render("Speed: " + str(game.greentank.speed)    , 1, (255, 255, 255))
		
		
		
		if self.selectedoption == 0:
			player1 = self.fontunderline.render("player1", 1, (255, 255, 255))
		else:
			player1 = self.font.render("player1", 1, (255, 255, 255))
		if self.selectedoption == 1:
			player2 = self.fontunderline.render("player2", 1, (255, 255, 255))
		else:
			player2 = self.font.render("player2", 1, (255, 255, 255))
		if self.selectedoption == 2:
			back = self.fontunderline.render("back", 1, (255, 255, 255))
		else:	
			back = self.font.render("back", 1, (255, 255, 255))
		
		
		
		game.display.blit(statsp2life, pygame.Rect(400, 150, 20, 20))
		game.display.blit(statsp2dmg, pygame.Rect(400, 200, 20, 20))
		game.display.blit(statsp2speed, pygame.Rect(400, 250, 20, 20))
		game.display.blit(statsp1life, pygame.Rect(100, 150, 20, 20))
		game.display.blit(statsp1dmg, pygame.Rect(100, 200, 20, 20))
		game.display.blit(statsp1speed, pygame.Rect(100, 250, 20, 20))
		game.display.blit(back, pygame.Rect(280, 300, 20, 20))
		game.display.blit(player2, pygame.Rect(280, 200, 20, 20))
		game.display.blit(player1, pygame.Rect(280, 100, 20, 20))
		
	def update(self):
		pressed_keys = pygame.key.get_pressed()
		if pressed_keys[pygame.K_SPACE] or pressed_keys[pygame.K_RETURN]  and self.waitselect == 0: 
			if self.selectedoption == 0:
				if self.statsetp1 == 2:
					self.statsetp1 = 0
				else:	
					self.statsetp1 = self.statsetp1 + 1
				self.waitselect = 5
			elif self.selectedoption == 1:
				if self.statsetp2 == 2:
					self.statsetp2 = 0
				else:	
					self.statsetp2 = self.statsetp2 + 1
				self.waitselect = 5
			elif self.selectedoption == 2:
				return 0 
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
		if self.statsetp1 == 0:
			game.redtank.maxlife = 10
			game.redtank.dmg = 2
			game.redtank.speed = 2
		elif self.statsetp1 == 1:
			game.redtank.maxlife = 8
			game.redtank.dmg = 2
			game.redtank.speed = 4	
		elif self.statsetp1 == 2:
			game.redtank.maxlife = 12
			game.redtank.dmg = 3
			game.redtank.speed = 1	
			
		if self.statsetp2 == 0:
			game.greentank.maxlife = 10
			game.greentank.dmg = 2
			game.greentank.speed = 2
		elif self.statsetp2 == 1:
			game.greentank.maxlife = 8
			game.greentank.dmg = 2
			game.greentank.speed = 4	
		elif self.statsetp2 == 2:
			game.greentank.maxlife = 12
			game.greentank.dmg = 3
			game.greentank.speed = 1		
		return 2	
			
			
		
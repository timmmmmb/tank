import pygame, tank, shot

def init():
	
	pygame.init()
	#die oberfläche wird erstellt
	global display
	display = pygame.display.set_mode((640, 480))
	#der Panzer des ersten spielers wird erstellt
	global redtank
	redtank = tank.Tank('red', 20, 40,0)
	#der Panzer des zweiten spielers wird erstellt
	global greentank
	greentank = tank.Tank('green', 580, 421,1)
	#das hintergrundbild wird geladen
	global background
	background = pygame.image.load('images/background.bmp').convert_alpha()
	
	global font
	font = pygame.font.Font(None, 36)
	pygame.display.set_caption('Tank by Tim Frey')
	
	
	
	
	
def draw():	
	#hier werden alle verschiedene objekte gezeichnet
	global redtank
	global greentank
	global background
	global font
	
	
	display.blit(background, pygame.Rect(0, 0, 20, 20))
	redtank.draw()
	greentank.draw()
	# Display some text
	redlife = font.render("RotesLeben: " + str(redtank.life), 1, (10, 10, 10))
	greenlife = font.render("Grünesleben: " + str(greentank.life), 1, (10, 10, 10))
	redpoints = font.render("Rot: " + str(redtank.points), 1, (10, 10, 10))
	greenpoints = font.render("Grün: " + str(greentank.points), 1, (10, 10, 10))
	display.blit(redlife, pygame.Rect(0, 0, 20, 20))
	display.blit(greenlife, pygame.Rect(430, 0, 20, 20))
	display.blit(redpoints, pygame.Rect(220, 0, 20, 20))
	display.blit(greenpoints, pygame.Rect(300, 0, 20, 20))
	
def update():
	#hier werden die panzer geupdatet
	global redtank
	global greentank
	redtank.update()
	greentank.update()
	#überprüfft ob einer der schüsse einen panzer trifft
	for shot in greentank.shots:
		if redtank.rect.colliderect(shot.rect):
			redtank.life = redtank.life - greentank.dmg	
	greentank.shots = [shot for shot in greentank.shots if not redtank.rect.colliderect(shot.rect)]
	
	for shot in redtank.shots:
		if greentank.rect.colliderect(shot.rect):
			greentank.life = greentank.life - redtank.dmg
	redtank.shots = [shot for shot in redtank.shots if not greentank.rect.colliderect(shot.rect)]
	
	#leben überprüfen
	if greentank.life <= 0:
		greentank.life = greentank.maxlife
		redtank.points = redtank.points + 1
		greentank.x = 580
		greentank.y = 421
		
	if redtank.life <= 0:
		redtank.life = redtank.maxlife
		greentank.points = greentank.points + 1
		redtank.x = 20
		redtank.y = 40
	
	if redtank.points == 5 or greentank.points == 5:
		return 0
	else:
		return 1
	
	
	
	
	
	
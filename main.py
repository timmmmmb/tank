import pygame, game, sys, menu, options

# Game initialization hier werden alle objekte erstellt und alle wichtigen variablen erstellt

# todo options fahrzeug wählen dafür muss ich eine neue class options erstellen und einenen neuen status
game.init()
menu = menu.Menu()
options = options.Options()

clock = pygame.time.Clock()


# Gameloop
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	if menu.status == 0:
		menu.update()
		menu.draw()
		options.waitselect = 10
	elif menu.status == 1:
		menu.status = game.update()
		game.draw()
	elif menu.status == 2:
		menu.status = options.update()
		options.draw()
		menu.waitselect = 10

	pygame.display.flip()

	clock.tick(30)
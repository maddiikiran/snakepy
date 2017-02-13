import pygame
import time
import random

#initailize
pygame.init()

#dimenstions of the window
display_width = 800
display_height = 600

FPS = 30

font = pygame.font.SysFont(None, 25)

def message_to_screen(msg, color):
	screen_text = font.render(msg, True, color)
	gameDisplay.blit(screen_text, [display_width/2, display_height/2])

#Defining colors (rgb values)
BACKGROUND_COLOR = (178, 217, 4)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)


#set up the display
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("PyPyper")



block_size = 5

clock = pygame.time.Clock()

def gameloop():

	gameExit = False
	gameOver = False

	lead_x = display_width/2
	lead_y = display_height/2
	lead_x_change = 0
	lead_y_change = 0

	appleX = random.randrange(0, display_width - block_size)
	appleY = random.randrange(0, display_height - block_size)
	
	while not gameExit:
		
		while gameOver==True:
			gameDisplay.fill(white)
			message_to_screen("Game over! Restarting...", red)
			pygame.display.update()
			time.sleep(1)
			gameloop()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
				gameOver = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					lead_x_change = -block_size
					lead_y_change = 0
				elif event.key == pygame.K_RIGHT:
					lead_x_change = block_size
					lead_y_change = 0
				elif event.key == pygame.K_UP:
					lead_y_change = -block_size
					lead_x_change = 0
				elif event.key == pygame.K_DOWN:
					lead_y_change = block_size
					lead_x_change = 0

		# Defining the boundaries
		if lead_x>=display_width or lead_x<0 or lead_y>=display_height or lead_y<0:
				gameOver = True

		lead_x += lead_x_change
		lead_y += lead_y_change

		gameDisplay.fill(BACKGROUND_COLOR)
		pygame.draw.rect(gameDisplay, blue, [lead_x, lead_y, block_size, block_size])
		pygame.draw.rect(gameDisplay, red, [appleX, appleY, block_size, block_size])
		#gameDisplay.fill(red, [lead_x, lead_y, 10, 10])
		pygame.display.update()

		clock.tick(FPS) 

	#exit
	pygame.quit()
	quit()

gameloop()
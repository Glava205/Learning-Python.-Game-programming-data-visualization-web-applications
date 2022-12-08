import sys

import pygame

def bg_color():
	pygame.init()
	bg_color=(0,0,255)
	screen=pygame.display.set_mode((1200,800))
	
	
	while True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
		screen.fill(bg_color)
		pygame.display.flip()

bg_color()

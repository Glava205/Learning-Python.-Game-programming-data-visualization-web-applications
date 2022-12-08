import sys

import pygame

class Alien():
	def __init__(self, screen):
		"""Инициализирует корабль и задает его начальную позицию."""
		self.screen = screen
		# Загрузка изображения корабля и получение прямоугольника.
		self.image = pygame.image.load('alien.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		# Каждый новый корабль появляется у нижнего края экрана.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery
	def blitme(self):
		"""Рисует корабль в текущей позиции."""
		self.screen.blit(self.image, self.rect)



pygame.init()

screen=pygame.display.set_mode((1200,800))

#Создание корабля
alien=Alien(screen)
#Назначение цвета фона
bg_color=(230,150,230)

#Запуск основного цикла игры

while True:
	#Отслеживание событий клавиатуры и мыши
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
	
	screen.fill(bg_color)
	alien.blitme()
	
	#Отображение последнего прорисованного экрана
	pygame.display.flip()

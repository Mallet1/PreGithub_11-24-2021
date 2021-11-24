import pygame


class Entity:
	def __init__(self, x, y, width = None, height = None, xChange = 0,yChange = 0, image = None, color = 'WHITE'):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.xChange = xChange
		self.yChange = yChange
		self.color = color

		try:
			self.image = pygame.image.load(image)
		except TypeError:
			self.image = None

	def getRect(self):
		return self.image.get_rect(center = (self.x,self.y))
import pygame


class Entity:
	def __init__(self, x, y, width = None, height = None, xChange = 0,yChange = 0, image = None, color = 'WHITE'):
		self.x = x
		self.y = y
		self.xChange = xChange
		self.yChange = yChange

		if image is None:
			self.width = width
			self.height = height
			self.color = color
			self.image = None
			self.rect = None
		else:
			self.width = None
			self.height = None
			self.color = None
			self.image_name = image
			self.image = pygame.image.load(image)
			self.rect = self.image.get_rect()  #(self.x, self.y))

	def set_image(self, image):
		self.image_name = image
		self.image = pygame.image.load(image)
		self.rect = self.image.get_rect()
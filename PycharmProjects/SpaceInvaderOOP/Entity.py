import pygame, random, math, time
from pygame import mixer

class Entity:
	def __init__(self,image,x,y,xChange,yChange,state):
		self.image = pygame.image.load(image)
		self.x = x
		self.y = y
		self.xChange = xChange
		self.yChange = yChange
		self.state = state

	def getRect(self):
		return self.image.get_rect(center = (self.x,self.y))
import math
import random
import pygame

class Ball(pygame.sprite.Sprite):
	def __init__(self,filename,screen,**kargs):
		pygame.sprite.Sprite.__init__(self)
		self.x = kargs.get('x',random.randint(50, 200))
		self.y = kargs.get('y',random.randint(100, 400))
		self.speed = kargs.get('speed', random.random())
		self.angle = kargs.get('angle', random.uniform(0,math.pi*2))
		self.screen = screen
		self.color = (170,140,140)
		self.radius = 5
		self.rect = pygame.draw.circle(self.screen,self.color,(self.x,self.y),self.radius)

	def update(self):
		self.x = self.x + (math.sin(self.angle) * self.speed)
		self.y = self.y + (math.cos(self.angle) * self.speed)

	def boundary(self):
		if self.x > self.screen.get_width() - self.radius:
			self.x = 2*(self.screen.get_width() - self.radius) - self.x
			self.angle = - self.angle       
		if self.x < self.radius:
			self.angle = - self.angle
			self.rect.x = 2*self.radius - self.rect.x 
			

		if self.y > self.screen.get_height() - self.radius:
			self.y = 2*(self.screen.get_height() - self.radius) - self.y
			self.angle = math.pi - self.angle      

		if self.y < self.radius:
			self.y = 2*self.radius - self.y
			self.angle = math.pi - self.angle

	        
	        
	def display(self):
		self.rect = pygame.draw.circle(self.screen,self.color,(int(self.x),int(self.y)),self.radius)

	


		   




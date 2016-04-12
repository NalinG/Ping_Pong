import math
import random
import pygame

class Paddle(pygame.sprite.Sprite):
	def __init__(self,(x,y),screen):
		pygame.sprite.Sprite.__init__(self)
		self.x = x
		self.y = y
		self.color = (181,174,174)
		self.height = 40
		self.width = 6
		self.screen = screen
		self.rect = pygame.draw.rect(screen,self.color,pygame.Rect(self.x,self.y,self.width,self.height))

	def update(self,direction):
		if direction=="up":
			self.y = self.y - 5
			self.y = self.y%self.screen.get_height()
		elif direction == "down":
			self.y = self.y + 5
			self.y = self.y%self.screen.get_height()

	def display(self):
		self.rect = pygame.draw.rect(self.screen,self.color,pygame.Rect(self.x,self.y,self.width,self.height))

	def ai(self, ball):
		dx = (math.sin(ball.angle) * ball.speed)
		if dx >0:
			if self.rect.centery < ball.rect.centery:
				self.update("down")
			elif self.rect.centery > ball.rect.centery:
				self.update("up")
		elif dx<0:
			if self.rect.centery < self.screen.get_height()/2 - 5 :
				self.update("down")
			elif self.rect.centery > self.screen.get_height()/2 +5 :
				self.update("up")
				
		
				

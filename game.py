import pygame
import random
import math
from finale import Ball
from finale_paddle import Paddle
import numpy
import time

pygame.init()
screen_width = 600
screen_height = 400
score_left = 0
score_right = 0
screen = pygame.display.set_mode((screen_width, screen_height))
def start_screen():
	global screen
	# surface = pygame.Surface((300, 300))
	screen.fill((0,0,0))
	font = pygame.font.SysFont("comicsansms", 50)
	font1 = pygame.font.SysFont("comicsansms", 35)
	text= font.render("Ping Pong", True, (13, 67, 40))
	Options =  ["One Player","Two Player","Exit"]
	y =0
	screen.blit(text,(200,50,50,50))
	# screen.blit(screen,(150,150,100,100))
	for option in Options:
		text1= font1.render(str(option), True, (13, 67, 31))
		screen.blit(text1,(200,150+y))
		y = y+45
	while 1:
		for event in pygame.event.get():
			mouse_x,mouse_y = pygame.mouse.get_pos()
			if mouse_x>250 and mouse_x <423:
				if mouse_y >=150 and mouse_y < 190 and event.type == pygame.MOUSEBUTTONDOWN:
					runGame()
					exit()
				elif mouse_y >= 195 and mouse_y < 240 and event.type == pygame.MOUSEBUTTONDOWN:
					runGame_twoplayer()
					exit()
				elif mouse_y >=245 and mouse_y < 280 and event.type == pygame.MOUSEBUTTONDOWN:
					exit()	
			if event.type == pygame.QUIT:
				exit()		

		pygame.display.flip()




def draw_dashed_line(surf, color, start_pos, end_pos, width=1, dash_length=10):
    x1, y1 = start_pos
    x2, y2 = end_pos
    dl = dash_length

    if (x1 == x2):
        ycoords = [y for y in range(y1, y2, dl if y1 < y2 else -dl)]
        xcoords = [x1] * len(ycoords)
    elif (y1 == y2):
        xcoords = [x for x in range(x1, x2, dl if x1 < x2 else -dl)]
        ycoords = [y1] * len(xcoords)
    else:
        a = abs(x2 - x1)
        b = abs(y2 - y1)
        c = round(math.sqrt(a**2 + b**2))
        dx = dl * a / c
        dy = dl * b / c

        xcoords = [x for x in numpy.arange(x1, x2, dx if x1 < x2 else -dx)]
        ycoords = [y for y in numpy.arange(y1, y2, dy if y1 < y2 else -dy)]

    next_coords = list(zip(xcoords[1::2], ycoords[1::2]))
    last_coords = list(zip(xcoords[0::2], ycoords[0::2]))
    for (x1, y1), (x2, y2) in zip(next_coords, last_coords):
        start = (round(x1), round(y1))
        end = (round(x2), round(y2))
        pygame.draw.line(surf, color, start, end, width)

def collision(ball, paddle_left, paddle_right):
	dx = (math.sin(ball.angle) * ball.speed)
	if dx > 0:
		if ball.rect.colliderect(paddle_right.rect):
			ball.angle = -ball.angle
		# 	flag_left = 0
		# elif ball.rect.right > paddle_right.x +1 :
		# 	flag_left = 1
	elif dx < 0 :
		if ball.rect.colliderect(paddle_left.rect):
			ball.angle = - ball.angle
		# 	flag = 0
		# elif ball.rect.left < paddle_left.x + 1 :
		# 	flag_right = 1			


def score(ball,paddle_left,paddle_right):
	dx = (math.sin(ball.angle) * ball.speed)
	global score_left
	global score_right
	if dx > 0 :
		if ball.rect.right > ball.screen.get_width()-3:
			score_left = score_left + 1
	elif dx < 0 :
		if ball.rect.left < 2 :
			score_right = score_right + 1

def runGame_twoplayer():			
	dict = {
	'pressed_up' : False,
	"pressed_down" : False,
	"pressed_w" : False,
	"pressed_s" : False
	}
	global screen
	global score_left
	global score_right
	global screen_height
	global screen_width
	
	clocl = pygame.time.Clock()
	pygame.display.set_caption('Ping Pong')
	screen.fill((0,0,0))
	ball = Ball("ball.png",screen, speed = 3, angle = 0.47)
	p1 = Paddle((30,0),screen)
	p2 = Paddle((screen_width-30,0),screen)
	font = pygame.font.SysFont("comicsansms", 40)
	# pygame.draw.line(screen, (255,255,255), ((screen_width/2),0),((screen_width/2),screen_height), (10/4))
	draw_dashed_line(screen, (255,255,255), (screen_width/2,0), (screen_width/2,screen_height),dash_length=5)

	

	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return 
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					dict["pressed_up"] = True
				elif event.key == pygame.K_DOWN:	
					dict["pressed_down"] = True
				elif event.key == pygame.K_w:
					dict["pressed_w"] = True
				elif event.key == pygame.K_s:
					dict["pressed_s"] = True
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					dict["pressed_up"] = False
				elif event.key == pygame.K_DOWN:
					dict["pressed_down"] = False
				elif event.key == pygame.K_s:
					dict["pressed_s"] = False
				elif event.key == pygame.K_w:
					dict["pressed_w"] = False
		
		if dict["pressed_up"]==True:
			p1.update("up")
		if dict["pressed_down"]==True:
			p1.update("down")
		if dict["pressed_s"]==True:
			p2.update("down")
		if dict["pressed_w"]==True:
			p2.update("up")


		text= font.render(str(score_left), True, (212, 198, 198))
		text1 = font.render(str(score_right), True, (212, 198, 198))	
		screen.blit(text,(150,50,30,30))
		screen.blit(text1,(450,50,30,30))
		ball.update()
		# print ball
		ball.boundary()
		# p2.ai(ball)
		p2.display()
		p1.display()
		draw_dashed_line(screen, (255,255,255), (screen_width/2,0), (screen_width/2,screen_height),dash_length=5)
		ball.display()
		collision(ball,p1,p2)
		score(ball, p1, p2)
		if score_left>4 or score_right>4:
			gameover()


		pygame.display.flip()
		screen.fill((0,0,0))
		clocl.tick(220)	

def gameover():
	global screen
	global score_left
	global score_right
	screen.fill((0,0,0))
	font = pygame.font.SysFont("comicsansms", 45)
	if score_left > score_right:
		text = "Player 1 WON"
	elif score_right==score_left:
		text = "It was DRAW"
	else:
		text = "Player 1 Loses"

	text= font.render(text, True, (255, 255, 255))
	screen.blit(text,(150,150,50,50))
	pygame.display.flip()

	time.sleep(2)
	start_screen()


def runGame():
	
	dict = {
	'pressed_up' : False,
	"pressed_down" : False,
	"pressed_w" : False,
	"pressed_s" : False
	}
	global screen
	global score_left
	global score_right
	global screen_height
	global screen_width
	
	clocl = pygame.time.Clock()
	pygame.display.set_caption('Ping Pong')
	screen.fill((0,0,0))
	ball = Ball("ball.png",screen, speed = 3, angle = 0.47)
	p1 = Paddle((30,0),screen)
	p2 = Paddle((screen_width-30,0),screen)
	font = pygame.font.SysFont("comicsansms", 40)
	# pygame.draw.line(screen, (255,255,255), ((screen_width/2),0),((screen_width/2),screen_height), (10/4))
	draw_dashed_line(screen, (255,255,255), (screen_width/2,0), (screen_width/2,screen_height),dash_length=5)

	

	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return 
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					dict["pressed_up"] = True
				elif event.key == pygame.K_DOWN:	
					dict["pressed_down"] = True
				# elif event.key == pygame.K_w:
				# 	dict["pressed_w"] = True
				# elif event.key == pygame.K_s:
				# 	dict["pressed_s"] = True
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					dict["pressed_up"] = False
				elif event.key == pygame.K_DOWN:
					dict["pressed_down"] = False
				# elif event.key == pygame.K_s:
				# 	dict["pressed_s"] = False
				# elif event.key == pygame.K_w:
				# 	dict["pressed_w"] = False
		
		if dict["pressed_up"]==True:
			p1.update("up")
		if dict["pressed_down"]==True:
			p1.update("down")
		# if dict["pressed_s"]==True:
		# 	p2.update("down")
		# if dict["pressed_w"]==True:
		# 	p2.update("up")


		text= font.render(str(score_left), True, (212, 198, 198))
		text1 = font.render(str(score_right), True, (212, 198, 198))	
		screen.blit(text,(150,50,30,30))
		screen.blit(text1,(450,50,30,30))
		ball.update()
		# print ball
		ball.boundary()
		p2.ai(ball)
		p2.display()
		p1.display()
		draw_dashed_line(screen, (255,255,255), (screen_width/2,0), (screen_width/2,screen_height),dash_length=5)
		ball.display()
		collision(ball,p1,p2)
		score(ball, p1, p2)
		if score_left>4 or score_right>4:
			gameover()


		pygame.display.flip()
		screen.fill((0,0,0))
		clocl.tick(220)	


if __name__ == '__main__':
	start_screen()
	
	

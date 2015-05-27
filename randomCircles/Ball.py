from Vector import Vector
import random, pygame, sys
from pygame.locals import *

class Ball():

	BACKGROUND_COLOR = (255, 255, 255)
	DEFAULT_COLOR = (0, 0, 0)
	DEFAULT_SIZE = 30
	TRANSPARENT = (255,0,255)

	

	def __init__(self, width, height, 
				x = -1, y = -1,
				vx = 0,	vy = 0,
				ax = 0,	ay = 0,
				l = 10, c= DEFAULT_COLOR,
				r = DEFAULT_SIZE):

		self.windowWidth = width
		self.windowHeight = height
		self.r = r
		self.color = c
		self.red = 0
		self.green = 0
		self.blue = 0

		if x == -1 and y == -1:
			x = random.randint(0, width)
			y = random.randint(0, height)

		self.mass = 10
		self.location = Vector(x, y)
		self.velocity = Vector(vx, vy)
		self.acceleration = Vector(ax, ay)
		self.maxVelocity = l
		self.surf = pygame.Surface((2*self.r,2*self.r))
		self.surf.fill(Ball.TRANSPARENT)
		
		
	def __str__(self):
		ballStr = "location: "+ str(self.location.x)+", "+ str(self.location.y)+"\n"
		ballStr	= ballStr + "velocity: "+str(self.velocity.x)+", "+str(self.velocity.y)+" = "+str(self.velocity.mag())+"\n"
		ballStr	= ballStr + "acceleration: "+str(self.acceleration.x)+", "+str(self.acceleration.y)
		return ballStr

	def display(self, display):
		#pygame.draw.circle(display, self.color, (self.location.x, self.location.y), self.r)
		
		#pygame.draw.circle(display, self.color, (int(self.location.x), int(self.location.y)), self.r)
		

		self.surf.set_colorkey(Ball.TRANSPARENT)
		pygame.draw.circle(self.surf, self.color, (self.r, self.r), self.r)
		self.surf.set_alpha(100)
		display.blit(self.surf, (self.location.x-self.r, self.location.y-self.r, 2*self.r, 2*self.r))

		#It's different with edges or endless
		self.checkEdges1()

		self.update()
		print str(self)



	#Endless World
	def checkEdges2(self):
		if self.location.x >= self.windowWidth:
			self.location.x = 0
		elif self.location.x <= 0:
			self.location.x = self.windowWidth

		if self.location.y >= self.windowHeight:
			self.location.y = 0
		elif self.location.y <= 0:
			self.location.y = self.windowHeight

	#Finite World
	def checkEdges1(self):
		if self.location.x >= self.windowWidth or self.location.x <= 0:
			self.velocity.x = self.velocity.x * -1

		if self.location.y >= self.windowHeight or self.location.y <= 0:
			self.velocity.y = self.velocity.y * -1


	def update(self):		
		self.velocity.add(self.acceleration)
		self.velocity.limit(self.maxVelocity)
		self.location.add(self.velocity)
		self.acceleration.mult(0)
		
	def setAcceleration(self, ax, ay):
		self.acceleration.x = ax
		self.acceleration.y = ay

	def applyForce(self, force):
		f = Vector.divs(force, self.mass)
		self.acceleration.add(f)

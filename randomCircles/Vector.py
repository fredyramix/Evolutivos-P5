import random, pygame, sys
from pygame.locals import *
import math

class Vector:

	DEFAULT_COLOR = (0, 0, 0)
	DEFAULT_SIZE = 10

	def __init__(self, x, y, z=0):
		self.x = x
		self.y = y
		self.z = z
		random.seed()

	@staticmethod
	def adds(u, v):
		return Vector(u.x+v.x, u.y+v.y, u.z+v.z)
	
	@staticmethod
	def subs(u, v):
		return Vector(u.x-v.x, u.y-v.y, u.z-v.z)

	@staticmethod
	def divs(u, n):
		return Vector(u.x/n, u.y/n, u.z/n)


	def setVector(self, u):
		self.x = u.x
		self.y = u.y
		self.z = u.z

	def add(self, v):
		self.x = self.x + v.x
		self.y = self.y + v.y
		self.z = self.z + v.z

	def sub(self, v):
		self.x = self.x - v.x
		self.y = self.y - v.y
		self.z = self.z - v.z


	def mult(self, n):
		self.x = self.x * n
		self.y = self.y * n
		self.z = self.z * n

	def div(self, n):
		self.x = self.x / n
		self.y = self.y / n
		self.z = self.z / n

	def mag(self):
		return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z);

	def setMag(self, n):
		self.normalize()
		self.mult(n)

	def normalize(self):
		m = self.mag()
		if m != 0:
			self.div(m)
		else:
			print "It's not possible normilize thsi vector...division by 0"

	def limit(self, limit):
		if limit != 0.0:
			if self.mag() > limit:
				self.setMag(limit)



	def random2D(self):
		self.x = random.random()*2.0-1.0
		self.y = random.random()*2.0-1.0
		self.normalize()


	def random3D(self, xmin=0.0, xmax=1.0, ymin=0.0, ymax=1.0, zmin=0.0, zmax=1.0):
		self.x = random.random()*2.0-1.0
		self.y = random.random()*2.0-1.0
		self.z = random.random()*2.0-1.0
		self.normalize()


	def setx(self, x):
		self.x = x

	def sety(self, y):
		self.y = y

	def getx(self):
		return self.x

	def gety(self):
		return self.y
		

		


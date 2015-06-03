'''
Created on Jan 15, 2015

@author: chewy
'''
'''
Created on Jan 15, 2015

@author: chewy
'''

from Ball import Ball
import random, pygame, sys
from pygame.locals import *
from Vector import Vector

CONSTANT_ACCELERATION = 1
RANDOM_ACCELERATION = 2
MOUSE_ACCELERATION = 3

ACCELERATION_CHOICE = MOUSE_ACCELERATION

MAX_VELOCITY = 5

NUMBER_BALLS = 100


class World:

    

    RED = (255,0,0)
    WHITE = (255, 255, 255)
    BLUE =(0,0,220)


 
    def __init__(self, WINDOWWIDTH, WINDOWHEIGHT, FPS):
        self.WINDOWWIDTH = WINDOWWIDTH
        self.WINDOWHEIGHT = WINDOWHEIGHT
        self.FPS = FPS
        self.mousex = 0
        self.mousey = 0
        self.movement = True

    def setup(self, at):
        '''
        If you want no limit for velocity use l=0
        If you want random sizes for balls use r=random.randint(10,50)
        If you want gray scale  use c=(128,128,128,100) or colors c=(random.randint(0,255),random.randint(0,255),random.randint(0,255), 100)
        '''
        #self.balls = [Ball(self.WINDOWWIDTH, self.WINDOWHEIGHT, l=MAX_VELOCITY+i*random.random()*.5,c=(127,127,127, 100), r=30) for i in xrange(NUMBER_BALLS)]
        self.balls = [Ball(self.WINDOWWIDTH, self.WINDOWHEIGHT, l=MAX_VELOCITY+(i+1)*random.random()*5.0, c=(random.randint(0,255),random.randint(0,255),random.randint(0,255), 100), r=random.randint(10,50)) for i in xrange(NUMBER_BALLS)]

        self.f = Vector(0,0)
        self.westWind = Vector(1.0, 0)
        self.eastWind = Vector(-1.0, 0)

        self.noForceVector = Vector(0,0)
        self.gravity = Vector(0, 0.5)

    def draw(self):        
        self.f.add(self.gravity)
        self.f.add(self.westWind)
        
        for ball in self.balls:            
            #ball.applyForce(self.f)
            ball.display(self.DISPLAYSURF)

        '''
        if self.f.mag() != 0:
            self.f.setVector(self.noForceVector)
        '''
        pygame.display.flip()


    def newAcceleration(self):
        mouse = Vector(self.mousex, self.mousey)
        for ball in self.balls:
            direction = Vector.subs(mouse, ball.location)
            #magnitud = 10.0/direction.mag()
            magnitud = random.random()
            direction.normalize()
            direction.mult(magnitud)
            ball.acceleration.setVector(direction)

    def start(self):


        self.setup(ACCELERATION_CHOICE)

        print "Inicio"
        
        
        global FPSCLOCK, DISPLAYSURF
        pygame.init()
        FPSCLOCK = pygame.time.Clock()
        self.DISPLAYSURF = pygame.display.set_mode((self.WINDOWWIDTH, self.WINDOWHEIGHT))

        x=random.randint(0, self.WINDOWWIDTH)
        y=random.randint(0, self.WINDOWHEIGHT)
        s= 10

        self.DISPLAYSURF.fill(World.WHITE)
        
        while True:
            
            for event in pygame.event.get(): # event handling loop
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEMOTION:
                    self.mousex, self.mousey = event.pos
                    self.movement = True
                    print str(self.mousex)+","+str(self.mousey)
                elif event.type == MOUSEBUTTONUP:
                    print "CLick"
                    self.mousex, self.mousey = event.pos
                    mouseClicked = True
                    if self.mousex > self.WINDOWWIDTH/2:
                        self.f.add(self.eastWind)
                    else:
                        self.f.add(self.westWind)


            self.DISPLAYSURF.fill(World.WHITE)
            self.draw()
        
            pygame.display.update()
            FPSCLOCK.tick(self.FPS)





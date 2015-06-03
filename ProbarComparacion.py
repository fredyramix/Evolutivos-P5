__author__ = 'freddy'
#importamos librerias
import pygame,sys,random
from pygame.locals import *
import ImageChops
import math, operator
import Image

def Comparate():
    im1=Image.open("imagenes/soluciones/1000.jpg").histogram()
    im2=Image.open("imagenes/soluciones/3000.jpg").histogram()
    rms = math.sqrt(reduce(operator.add, map(lambda a,b: (a-b)**2, im1, im2))/len(im1))
    return rms
a=Comparate()
print a
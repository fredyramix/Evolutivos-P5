__author__ = 'fredy'
import random
import pygame
from pygame.locals import *


import math, operator
import Image

def comparate(padre,hijo):
    im1=Image.open(padre).histogram()
    im2=Image.open(hijo).histogram()
    rms = math.sqrt(reduce(operator.add, map(lambda a,b: (a-b)**2, im1, im2))/len(im1))
    return rms

def load_image(filename, transparent=False):
    try:
        image = pygame.image.load(filename)
    except pygame.error, message:
        raise SystemExit, message
        image = image.convert()
    if transparent:
        color = image.get_at((0,0))
        image.set_colorkey(color, RLEACCEL)
    return image

def evaluar(poblacion,original,bandera):
    actitudes=[]
    generation = 0
    for individuo in poblacion:
        TRANSPARENT = (255,0,255)
        R=int(individuo[0])
        G=int(individuo[1])
        B=int(individuo[2])
        X=int(individuo[3])
        Y=int(individuo[4])
        radio=int(individuo[5])
        FONDO=individuo[6]
        COLOR=(R,G,B)
        POSICION=(X,Y)
        #print "Generacion: "+ str(generation)+" R:"+str(R) +" G:"+str(G)+ " B:"+str(B)+ " X:"+str(X)+ " Y:"+str(Y)
        #print FONDO
        pygame.init()
        screen = pygame.display.set_mode((300,300))
        surf1 = pygame.Surface((500,500))
        surf1.fill(TRANSPARENT)
        surf1.set_colorkey(TRANSPARENT)
        pygame.draw.circle(surf1,COLOR,POSICION, radio)
        surf1.set_alpha(100)
        #while generation != len(poblacion):
        background_image = load_image(FONDO)
        #screen.fill((255,255,255))
        screen.blit(background_image, (0, 0))
        #for event in pygame.event.get():
        #    if event.type == QUIT:
        #        pygame.quit()
        screen.blit(surf1, (0,0))
        pygame.display.flip()
        if bandera==True:
            hijo="padres/"+str(generation)+".jpg"
            individuo[6]=hijo
        else:
            #raw_input("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
            hijo="mutadas/"+str(generation)+".jpg"
            individuo[6]=hijo
        pygame.image.save(screen,hijo)
        generation += 1
        actitudes.append(comparate(original,hijo))
        #raw_input("zzzzzzzzzzzzzzzzzzzzzzz")
    pygame.quit()
    return actitudes

def Elegir(poblacion,padre):
    aptitudes=[]
    for f in range(0,len(poblacion)):
        aptitudes.append(evaluar(poblacion[f],padre))
    return aptitudes




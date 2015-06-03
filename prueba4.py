__author__ = 'freddy'
#importamos librerias
import pygame,sys,random
from pygame.locals import *
import ImageChops
import math, operator
import Image
HIGH=300
WIDTH=300
TRANSPARENT = (255,0,255)
def Comparate():
    im1=Image.open("1.jpg")
    im2=Image.open("2.jpg")
    h = ImageChops.difference(im1, im2).histogram()
    # calculate rms
    return math.sqrt(reduce(operator.add,
        map(lambda h, i: h*(i**2), h, range(256))
    ) / (float(im1.size[0]) * im1.size[1]))

R = 0
G = 0
B= 200
A = 100
X= 10
Y= 10
r= random.randint(0,10)

#iniciamos pygame
pygame.init()

#definimos constantes
pantalla = pygame.display.set_mode((HIGH, WIDTH))
pygame.display.set_caption('Image Generator')

reloj = pygame.time.Clock()

#definimos funciones
def cargar_imagen(nombre,transparente=False):
     try:
         imagen = pygame.image.load(nombre)
     except:
         imagen = pygame.image.load("imagenes/white.jpg")
     imagen = imagen.convert()
     if transparente:
          color = imagen.get_at((0,0))
          imagen.set_colorkey(color, RLEACCEL)
     return imagen
#Aqui es donde colocamos el fondo a la pantalla
fondo = cargar_imagen('imagenes/white.jpg')
pantalla.blit(fondo, (0, 0)) #es para esto que nos sirvio poner en una
                             #variable los datos de la pantalla
pygame.display.flip()

#Bucle principal del juego
generation = 0
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
           if event.type == K_ESCAPE:
            pygame.quit()
            sys.exit()
    R= random.randint(0,255)
    G= random.randint(0,255)
    B= random.randint(0,255)
    A= 100
    X= random.randint(0,HIGH)
    Y= random.randint(0,WIDTH)
    r= random.randint(0,10)
    surf1 = pygame.Surface((HIGH,WIDTH))
    surf1.fill(TRANSPARENT)
    surf1.set_colorkey(TRANSPARENT)
    pygame.draw.circle(surf1, (R,G,B,A),(X,Y),r)
    surf1.set_alpha(100)
    pantalla.blit(surf1, (100,100,100,100))
    pygame.display.flip()
    pygame.display.update()
    pygame.image.save(pantalla, "imagenes/soluciones/"+str(generation)+".jpg")
    #comp = Comparate()
    generation = generation+1
    #raw_input("Espera")
 #reloj.tick(60)
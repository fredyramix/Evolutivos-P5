__author__ = 'freddy'

import pygame,os
from pygame.locals import *
#definimos funciones

#Cargar la imagen principal
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


#Comprobar si existe directorio
def comprobarDirectorio(ruta):
    try: os.makedirs(ruta)
    except OSError:
        pass
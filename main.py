from PIL import Image
import pygame

def imprimir(all_pixels):
    for pixel in all_pixels:
        print pixel

i = Image.open("imagenes/1.jpg")

pixels = i.load()
width, height = i.size

all_pixels = []
for x in range(width):
    for y in range(height):
        cpixel = pixels[x, y]
        all_pixels.append(cpixel)

#imprimir(all_pixels)

from scipy.misc import toimage
toimage(all_pixels).show()
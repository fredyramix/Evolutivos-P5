from PIL import Image

i = Image.open("imagenes/3.jpg")

pixels = i.load()
width, height = i.size

all_pixels = []
for x in range(width):
    for y in range(height):
        cpixel = pixels[x, y]
        all_pixels.append(cpixel)



def imprimir(all_pixels):
    for pixel in all_pixels:
    print pixel
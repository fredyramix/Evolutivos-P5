from PIL import Image
import random
im = Image.new("RGB", (255,100,))
data = [(x,x,x) for y in range(im.size[1]) for x in range(im.size[0])]
im.putdata(data)
im.save("pix.png")
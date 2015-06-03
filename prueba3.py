import pygame
import random
from pygame.locals import *
HIGH=300
WIDTH=300
TRANSPARENT = (255,0,255)
R = 0
G = 0
B= 200
A = 100
X= 10
Y= 10

pygame.init()
screen = pygame.display.set_mode((WIDTH,HIGH))

while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    R= random.randint(0,255)
    G= random.randint(0,255)
    B= random.randint(0,255)
    A= 100
    X= random.randint(0,HIGH)
    Y= random.randint(0,WIDTH)
    r= random.randint(0,10)
    surf1 = pygame.Surface((200,200))
    surf1.fill(TRANSPARENT)
    surf1.set_colorkey(TRANSPARENT)
    #circle(Surface, color, pos, radius, width=0) -> Rect
    pygame.draw.circle(surf1, (R,G,B,A),(X,Y),r)
    surf1.set_alpha(100)
    screen.blit(surf1,(0,0))
    pygame.display.flip()
    pygame.image.save(screen, "screenshot.jpg")

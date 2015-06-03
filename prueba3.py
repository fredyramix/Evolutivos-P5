import pygame
from pygame.locals import *
HIGH=300
WIDTH=300
TRANSPARENT = (255,0,255)

pygame.init()
screen = pygame.display.set_mode((WIDTH,HIGH))
surf1 = pygame.Surface((200,200))
surf1.fill(TRANSPARENT)
surf1.set_colorkey(TRANSPARENT)
#surface, color, position, radio, width

pygame.draw.circle(surf1, (0,0,200,100),(12,50),50)
surf1.set_alpha(100)
while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    screen.blit(surf1, (100,100,100,100))
    pygame.display.flip()
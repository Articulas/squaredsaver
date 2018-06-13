# Square Saver (C) 1994-2018 Adam Hansen All Rites Reserved 


import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
orange = (255,100,0)
yellow = (200,200,0)
dgrey = (110,110,110)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Square Saver")

clock = pygame.time.Clock()

saver_exit = False

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def display_engine ():

    while not saver_exit:

        randx = random.randrange(0, 784)
        randy = random.randrange(0,584)

        randc1 = random.randrange(0,255)
        randc2 = random.randrange(0,255)
        randc3 = random.randrange(0,255)
        color =  (randc1,randc2,randc3)   

        pygame.draw.rect(gameDisplay, color, [randx, randy, 32, 32])

        pygame.display.update()

        clock.tick(60)
    
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

display_engine()

pygame.quit()
quit()

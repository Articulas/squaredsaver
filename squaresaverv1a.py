

import pygame
import time
import random

pygame.init()

display_height = 600
display_width = 800

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
#pygame.draw.rect(gameDisplay, red, [100, 100, 16, 16])

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# def display_engine ():

while not saver_exit:
    # gameDisplay.fill(dgrey)

    randx = random.randrange(0, 784)
    randy = random.randrange(0,584)
        
    pygame.draw.rect(gameDisplay, red, [randx, randy, 16, 16])

    pygame.display.update()
    clock.tick(60)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

display_engine()
pygame.quit()
quit()

import pygame
import random
pygame.font.init()


screen = pygame.display.set_mode((900, 650))
  
pygame.display.set_caption("SORTING VISUALISER")

run = True

width = 900
length = 600
sz = 50000
array = [0]*(sz+1)
arr_clr = [(0, 204, 102)]*(sz+1)
clr_ind = 0
clr = [(0, 204, 102), (255, 0, 0),
       (0, 0, 153), (255, 102, 0),(230,230,250)]

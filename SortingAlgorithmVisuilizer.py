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


fnt = pygame.font.SysFont("comicsans", 30)
fnt1 = pygame.font.SysFont("comicsans", 30)
fnt2 = pygame.font.SysFont("comicsans", 20)


base_font = pygame.font.Font(None, 32)
user_text = ''

input_rect = pygame.Rect(600, 10, 140, 32)
  

color_active = pygame.Color('lightskyblue3')
  

color_passive = pygame.Color('chartreuse4')
color = color_passive
  
active = False

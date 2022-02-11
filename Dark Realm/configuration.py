
#########################
#       Dark Realm      #
#      by: Levi Modl    #
#                       #
#          2022         #
#########################

################
#   Imports    #
################
from includes import *

#################
#   Variables   #
#################
Version = 'v0.1'
DISPLAYW = 1024
DISPLAYH = 768
BLACK = (1,1,1)
WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,128)
FONT = 'Corbel'
QTEXT = 'QUIT'
NTEXT = 'NEW GAME'
OTEXT = 'OPTIONS'
screen = pygame.display.set_mode((DISPLAYW,DISPLAYH))
width = screen.get_width()
height = screen.get_height()
X, Y = screen.get_size()
BUTTON_RES_W = width/2
BUTTON_RES_H = height/2

def Text(_text_, color, fontsize):
    font = pygame.font.SysFont(FONT, fontsize)
    text = font.render(_text_, True, color)
    return text

def Res():
    return (width/2, height/2)

def Button(locationx,locationy, sizex,sizey):
    pygame.draw.rect(screen, GREEN, pygame.Rect(sizex,sizey,locationx,locationy ))
    pygame.display.flip()

#class Adventure(action):

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
DISPLAYW = 800
DISPLAYH = 600
WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,128)
FONT = 'Corbel'
QTEXT = 'QUIT'
NTEXT = 'NEW GAME'
OTEXT = 'OPTIONS'
screen = pygame.display.set_mode((DISPLAYW,DISPLAYH))
smallfont = pygame.font.SysFont(FONT, 35)
width = screen.get_width()
height = screen.get_height()

def Text(_text_, color):
    mtext = smallfont.render(_text_, True, color)

def Res():
    return (width/2 + 50, height/2)

#class Adventure(action):

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
RED = (255,0,0)
ADV_TEXT_COLOR = (153,149,148)
DMFONT = 'Commic Sans MS'
ADVFONT = 'Times New Roman'
QTEXT = 'QUIT'
NTEXT = 'NEW GAME'
OTEXT = 'OPTIONS'
screen = pygame.display.set_mode((DISPLAYW,DISPLAYH))
width = screen.get_width()
height = screen.get_height()
X, Y = screen.get_size()
BUTTON_RES_W = width/2
BUTTON_RES_H = height/2
USER_INPUT = 'Choice'
Input_Rect = ''
clock = pygame.time.Clock()

def Text(_text_, color, fontsize, FONT):
    font = pygame.font.SysFont(FONT, fontsize)
    text = font.render(_text_, True, color)
    return text

def Res():
    return (width/2, height/2)

def InputBox(SizeX, SizeY, LocX, LocY):
    Input_Rect = pygame.Rect(SizeX, SizeY, LocX, LocY)
    return Input_Rect

def Menu():
    
    base_font = pygame.font.Font(None, 32)
    Input_Rect = pygame.Rect(425,500,100,30)
    pygame.draw.rect(screen,WHITE,Input_Rect)
    Text_Surf = base_font.render(USER_INPUT, True, (BLACK))
    screen.blit(Text_Surf, (Input_Rect.x+2, Input_Rect.y+5))
    Input_Rect.w = max(100, Text_Surf.get_width()+400) 
    pygame.display.flip()
    clock.tick(60)
    
    screen.blit(Text("DARK REALM", RED, 60, 'Comic Sans MS'), (X-700, Y-700))
    screen.blit(Text(Version, RED, 32, 'Commic Sans MS'), (X-50, Y-30))
    screen.blit(Text('1. Start Adventure', ADV_TEXT_COLOR, 30, DMFONT ), (X-600, Y-500))
    screen.blit(Text('Q. Quit', ADV_TEXT_COLOR, 30, DMFONT ), (X-600, Y-350))
       

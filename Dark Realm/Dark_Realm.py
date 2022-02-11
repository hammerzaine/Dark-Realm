
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
from configuration import *

#################
#   Variables   #
#################
#Adv=Adventure()
active = False

## Creating the game window
pygame.display.set_mode((DISPLAYW, DISPLAYH))
pygame.display.set_caption('Dark Realm')

mouse = pygame.mouse.get_pos()


while True:
    Menu()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Input_Rect.collidepoint(event.pos):
                active = True
            else:
                active = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                USER_INPUT = USER_INPUT[:-1]
            else:
                USER_INPUT += event.unicode
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    pygame.display.update()
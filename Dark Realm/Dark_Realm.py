
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



## Creating the game window
pygame.display.set_mode((DISPLAYW, DISPLAYH), pygame.RESIZABLE)
pygame.display.set_caption('Dark Realm')
mouse = pygame.mouse.get_pos()
Button(140,30, X/2,Y/2)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

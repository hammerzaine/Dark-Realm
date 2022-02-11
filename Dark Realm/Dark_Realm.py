
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
pygame.display.set_mode((DISPLAYW, DISPLAYH))
pygame.display.set_caption('Dark Realm')

mouse = pygame.mouse.get_pos()
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.blit(Text("DARK REALM", RED, 60, 'Comic Sans MS'), (X-700, Y-700))
    screen.blit(Text(Version, RED, 32, 'Commic Sans MS'), (X-50, Y-30))
    pygame.display.update()
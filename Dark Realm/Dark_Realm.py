
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

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if width/2 <= mouse[0] <= width/2 + 140 and height/2 <= mouse[1] <= height/2 + 40:
                pygame.quit()

        if width/2 <= mouse[0] <= width/2 + 140 and height/2 <= mouse[1] <= height/2 + 40:
            pygame.draw.rect(screen, GREEN, [width/2, height/2, 140, 40])
        else:
            pygame.draw.rect(screen, GREEN, [width/2, height/2, 140, 40])

#screen.blit(Text(QTEXT,GREEN), Res())
pygame.display.update()
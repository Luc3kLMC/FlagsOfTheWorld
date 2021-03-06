import pygame, sys, random, time
# from flagi import randoms


pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()  # needed for 'wait vbl'

screen = pygame.display.set_mode((1024,768))
pygame.display.set_caption("Flags Python by Luc3k")

run = True


font = pygame.font.SysFont("comicsansms", 16)



# variables
blitPosition = 256 # x of the screen = 1024, flag = 512, needed to centre the blit


def menuSetup():
    menuText1 = font.render("Flags of the world - quiz-game.", True, (5,5,5))
    menuText2 = font.render("Press Enter to start game.", True, (5,5,5))
    menuText3 = font.render("Press L to start learning mode.", True, (5,5,5))
    screen.fill((230,220,250))
    screen.blit(menuText1, (400,300))
    screen.blit(menuText2, (400,340))
    screen.blit(menuText3,(400,380))
    pygame.display.flip()


menuSetup()

while run:
   
    for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                execfile('flagi.py')
            elif event.key == pygame.K_l:     
                execfile('flagiLearningMode.py')
            elif event.key == pygame.K_ESCAPE:
                run = False    
        if event.type == pygame.QUIT:
                run = False
    
    fpsClock.tick(FPS)    # wait vbl

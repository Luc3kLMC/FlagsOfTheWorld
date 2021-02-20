# FLAGS IMAGES CREATED BY Freepik / freepik.com DOWNLOADED FROM flaticon.com
# This is my freeware quiz-like game 'Flags of the world' -  
# My first project for python learning purposes
# Greets, Luc3k

import pygame, sys, random
import arrays


pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()  # needed for 'wait vbl'

screen = pygame.display.set_mode((1024,768))
pygame.display.set_caption("Flags Python by Luc3k")

run = True

font = pygame.font.SysFont("comicsansms", 16)



# variables
blitPosition = 256 # x of the screen = 1024, flag = 512, needed to centre the blit
flagsTotal = len(arrays.flagName) - 1 # sum of the flags added to program, always -1 (starting from 0!)
randomFlag = random.randint(0, flagsTotal)


upperText = font.render("Use left and right arrows to browse flags.", True, (5,5,5)) 
lowerText = font.render(arrays.flagName[randomFlag], True, (5,5,5))  # print flag name from array

flagBlit = pygame.image.load(arrays.flagImg[randomFlag]).convert() #

# functions

 

def blitting():
    screen.fill((230,220,250))
    screen.blit(flagBlit, (blitPosition,100))
    screen.blit(upperText, (400,50))
    screen.blit(lowerText, (400,550))
    pygame.display.flip()

blitting()


while run:
     
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_LEFT and randomFlag == 0:
                randomFlag = flagsTotal
            elif event.key == pygame.K_LEFT and randomFlag != 0:   
                randomFlag = randomFlag - 1
            if event.key == pygame.K_RIGHT and randomFlag == flagsTotal:
                randomFlag = 0
            elif event.key == pygame.K_RIGHT and randomFlag != flagsTotal:
                randomFlag = randomFlag + 1 
 
            
                 
            flagBlit = pygame.image.load(arrays.flagImg[randomFlag]).convert()
            lowerText = font.render(arrays.flagName[randomFlag], True, (5,5,5))
            blitting()
    

        if event.type == pygame.QUIT:
            run = False

    fpsClock.tick(FPS)    # wait vbl






    


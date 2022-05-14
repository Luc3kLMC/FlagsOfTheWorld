# FLAGS IMAGES CREATED BY Freepik / freepik.com DOWNLOADED FROM flaticon.com
# This is my freeware quiz-like game 'Flags of the world' -  
# My first project for python learning purposes
# Greets, Luc3k

import pygame, sys, random, time,datetime, os
import arrays



pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()  # needed for 'wait vbl'

screen = pygame.display.set_mode((1024,768))
pygame.display.set_caption("Flags Python by Luc3k")

now = datetime.datetime.now()
startingTick = now.second
seedTick = now.second 
random.seed(startingTick)
score = 0
wrong = 0
answer = 0

run = True
menu = True
learn = False
game = False

font = pygame.font.SysFont("comicsansms", 16)

# variables
blitPosition = 256 # x of the screen = 1024, flag = 512, needed to centre the blit
flagsTotal = len(arrays.flagName) - 1 # sum of the flags added to program, always -1 (starting from 0!)
randomFlag = random.randint(0, flagsTotal)
upperText = font.render("Use left and right arrows to browse flags.", True, (5,5,5)) 
lowerText = font.render(arrays.flagName[randomFlag], True, (5,5,5))  # print flag name from array

flagBlit = pygame.image.load(os.path.join('data', arrays.flagImg[randomFlag])).convert() #

def randoms():
    random.seed(seedTick)
    correctOne = random.randint(1, 3)  # randomly select the correct answer's slot
    randomFlag1 = random.randint(0, flagsTotal) 
    randomFlag2 = random.randint(0, flagsTotal) 
    randomFlag3 = random.randint(0, flagsTotal)
    return (correctOne, randomFlag1, randomFlag2, randomFlag3) 

def textPrep():
    upperText = font.render("Choose the correct flag name:", True, (5,5,5)) 
    scoreText = font.render("Your score is: " + str(score), True, (5,5,5))
    wrongText = font.render("Incorrect answers: " + str(wrong), True, (5,5,5))
    return (upperText, scoreText, wrongText)

def questionPrep():
    x, f1, f2, f3, = randoms()
    global answer
    answer = x
    if x == 1:
        flagBlit = pygame.image.load(os.path.join('data', arrays.flagImg[f1])).convert()
    elif x == 2:
        flagBlit = pygame.image.load(os.path.join('data', arrays.flagImg[f2])).convert()
    elif x == 3:
        flagBlit = pygame.image.load(os.path.join('data', arrays.flagImg[f3])).convert() 

    lowerText1 = font.render("1. " + arrays.flagName[f1], True, (5,5,5))  # print flag name from array
    lowerText2 = font.render("2. " + arrays.flagName[f2], True, (5,5,5))
    lowerText3 = font.render("3. " + arrays.flagName[f3], True, (5,5,5)) 
    return(flagBlit, lowerText1, lowerText2, lowerText3, x)
     
def GameModeBliting():
    x, loText1, loText2, loText3, _, = questionPrep()
    uText, scText, wgText = textPrep()
    screen.fill((230,220,250))
    screen.blit(x, (blitPosition,100))
    screen.blit(uText, (400,50))
    screen.blit(loText1, (400,500))
    screen.blit(loText2, (400,540))
    screen.blit(loText3, (400,580))
    screen.blit(scText, (400,620))
    screen.blit(wgText, (400,660))
    pygame.display.flip()

def gameOverCheck():
    global wrong, score
    global run,menu,game
    if wrong == 3:
        screen.fill((230,220,250))
        gameOverText = font.render("3 wrong answers, try again! ", True, (5,5,5))
        screen.blit(gameOverText, (400,320))
        pygame.display.flip()
        pygame.time.delay(2000)
        wrong = 0
        score = 0
        menu = True
        game = False
        menuSetup()


# drawing first flag tec.
def process():
    randoms()
    textPrep()
    questionPrep()
    GameModeBliting()


def LearnModeBliting():
    screen.fill((230,220,250))
    screen.blit(flagBlit, (blitPosition,100))
    screen.blit(upperText, (400,50))
    screen.blit(lowerText, (400,550))
    pygame.display.flip()

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

    while menu:
   
        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    process()
                    menu = False
                    game = True
                elif event.key == pygame.K_l:     
                    LearnModeBliting()
                    menu = False
                    learn = True
                elif event.key == pygame.K_ESCAPE:
                    menu = False
                    run = False    
            if event.type == pygame.QUIT:
                    menu = False
                    run = False
        
        fpsClock.tick(FPS)    # wait vbl

    while learn:
         
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: 
                
                if event.key == pygame.K_ESCAPE:
                    menuSetup()
                    menu = True
                    learn = False
                elif event.key == pygame.K_LEFT and randomFlag == 0:
                    randomFlag = flagsTotal
                elif event.key == pygame.K_LEFT and randomFlag != 0:   
                    randomFlag = randomFlag - 1
                elif event.key == pygame.K_RIGHT and randomFlag == flagsTotal:
                    randomFlag = 0
                elif event.key == pygame.K_RIGHT and randomFlag != flagsTotal:
                    randomFlag = randomFlag + 1 
 
            
            if menu == False:     
                flagBlit = pygame.image.load(os.path.join('data', arrays.flagImg[randomFlag])).convert()
                lowerText = font.render(arrays.flagName[randomFlag], True, (5,5,5))
                LearnModeBliting()
    

        if event.type == pygame.QUIT:
            learn = False
            run = False

        fpsClock.tick(FPS)    # wait vbl

    while game:
        seedTick +=1
        randoms()
        if seedTick == 10000:
            seedTick = 0
       
     
        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menuSetup()
                    menu = True
                    game = False  
                elif event.key == pygame.K_1 and answer == 1:
                    score += 1
                    process()
                elif event.key == pygame.K_2 and answer == 2:
                    score += 1
                    process()
                elif event.key == pygame.K_3 and answer == 3:
                    score += 1
                    process() 
                elif event.key == pygame.K_1 and answer != 1:
                    wrong += 1
                    process()
                elif event.key == pygame.K_2 and answer != 2:
                    wrong += 1
                    process()
                elif event.key == pygame.K_3 and answer != 3:
                    wrong += 1
                    process() 
            
            gameOverCheck() 

            
            

                

            if event.type == pygame.QUIT:
                game = False
                run = False
        
        fpsClock.tick(FPS)    # wait vbl

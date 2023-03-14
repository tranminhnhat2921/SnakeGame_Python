import pygame, time, sys
from Snake import *

#Global variable
size = 20
snakePos = [100,60]
snakeBody = [[100,60],[80,60],[60,60]]
foodFlag = True
direction = 'RIGHT'
changeTo = direction
score = 0

#Init PyGame lib
pygame.init()

#Create screen
gameSuface = pygame.display.set_mode((735,475))
pygame.display.set_caption('Snake game')

#Define color
red = pygame.Color(255,0,0)
blue = pygame.Color(65,105,255)
black = pygame.Color(255,0,0)
white = pygame.Color(255,255,255)
gray = pygame.Color(128,128,128)

#Gameover function
def gameOver():
    gFont = pygame.font.SysFont('consolas', 40)
    gSurf = gFont.render('Game over!', True, red)
    gRect = gSurf.get_rect()
    gRect.midtop = (360,150)
    showScore(0)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    sys.exit()

#Show score function
def showScore(choice = 1):
    sFont = pygame.font.SysFont('consolas', 20)
    sSurf = sFont.render('Score: {0}'.format(score), True, black)
    sRect = sSurf.get_rect()
    if choice == 1:
        sRect.midtop = (70,20)
    else:
        sRect.midtop = (360,230)
    gameSuface.blit(sSurf,sRect)

#Main game
foodPos = createFood()
while True:
    pygame.time.delay(200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                changeTo = 'RIGHT'
            if event.key == pygame.K_LEFT:
                changeTo = 'LEFT'
            if event.key == pygame.K_UP:
                changeTo = 'UP'
            if event.key == pygame.K_DOWN:
                changeTo = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))  
    direction = moving(changeTo, direction, snakePos, size)

    # Handle snake eat food:
    snakeBody.insert(0,list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1
        foodFlag = False
    else:
        snakeBody.pop()

    if foodFlag == False:
        foodPos = createFood()
        foodFlag = True
    
    # Set background and snake color
    gameSuface.fill(white)
    for pos in snakeBody:
        pygame.draw.rect(gameSuface,blue,pygame.Rect(pos[0],pos[1],size,size))
    pygame.draw.rect(gameSuface,blue,pygame.Rect(snakeBody[0][0],snakeBody[0][1],size,size))  
    pygame.draw.rect(gameSuface,gray,pygame.Rect(foodPos[0],foodPos[1],size,size))  

    # Move to border
    if snakePos[0] > 710 or snakePos[0] < 10:
        gameOver()
    if snakePos[1] > 450 or snakePos[1] < 10:
        gameOver()

    # Snake eat itself
    for b in snakeBody[1:]:
        if snakePos[0] == b[0] and snakePos[1] == b[1]:
            gameOver()

    # Draw border and display game
    pygame.draw.rect(gameSuface,gray,(10,10,715,455),2)
    showScore()
    pygame.display.flip()
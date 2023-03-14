#import lib
import pygame, random, time, sys
pygame.init()

#Load image
m = 20
imageBody = pygame.transform.scale(pygame.image.load('body.jpg'),(m,m))
imageHead = pygame.transform.scale(pygame.image.load('head.jpg'),(m,m))
imageFood = pygame.transform.scale(pygame.image.load('covid.png'),(m,m))

#Create screen
gameSuface = pygame.display.set_mode((735,475))
pygame.display.set_caption('Snake game')

#Variable
snakePos = [100,60]
snakeBody = [[100,60],[80,60],[60,60]]
foodX = random.randrange(1,71)
foodY = random.randrange(1,45)
if foodX % 2 != 1 : foodX += 1
if foodY % 2 != 1 : foodY += 1
foodPos = [foodX*10, foodY*10]
foodFlag = True
direction = 'RIGHT'
changeTo = direction
score = 0

#Color
red = pygame.color(255,0,0)
blue = pygame.color(65,105,255)
black = pygame.color(255,0,0)
white = pygame.color(255,255,255)
gray = pygame.color(128,128,128)

#Gameover function
def gameOver():
    gFont = pygame.font.SysFont('consolas', 40)
    gSurf = gFont.render('Game over!', True, red)
    gRect = gSurf.get_rect()
    gRect.midtop = (360,150)
    showScore(0)
    pygame.display.flip()
    time.sleep(5)
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

#Main loop
while True:
    pygame.time.delay(200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_RIGHT:
                changeTo = 'RIGHT'
            if event.type == pygame.K_LEFT:
                changeTo = 'LEFT'
            if event.type == pygame.K_UP:
                changeTo = 'UP'
            if event.type == pygame.K_DOWN:
                changeTo = 'DOWN'
            if event.type == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))  
    #Handle move 
    if changeTo == "RIGHT" and not direction == "LEFT":
        direction = "RIGHT"
    if changeTo == "LEFT" and not direction == "RIGHT":
        direction = "LEFT"
    if changeTo == "UP" and not direction == "DOWN":
        direction = "UP"
    if changeTo == "DOWN" and not direction == "UP":
        direction = "DOWN"
    #Update position when move:
    if direction == "RIGHT":
        snakePos[0] += m
    if direction == "LEFT":
        snakePos[0] -= m
    if direction == "DOWN":
        snakePos[1] += m
    if direction == "UP":
        snakePos[1] -= m  
    

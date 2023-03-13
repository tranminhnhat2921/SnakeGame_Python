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

#Color
red = pygame.color(255,0,0)
blue = pygame.color(65,105,255)
black = pygame.color(255,0,0)
white = pygame.color(255,255,255)
gray = pygame.color(128,128,128)

#Main loop
while True:
    pygame.time.delay(200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

#import lib
import pygame, random, time, sys

#Create screen
pygame.init()
gameSuface = pygame.display.set_mode((735,475))
pygame.display.set_caption('Snake game')

#Main loop
while True:
    pygame.time.delay(200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
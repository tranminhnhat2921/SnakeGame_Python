import random

def moving(changeTo, direction, snakePos, range):
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
        snakePos[0] += range
    if direction == "LEFT":
        snakePos[0] -= range
    if direction == "DOWN":
        snakePos[1] += range
    if direction == "UP":
        snakePos[1] -= range
    return direction

def createFood():
    foodX = random.randrange(1,71)
    foodY = random.randrange(1,45)
    if foodX % 2 != 0 : foodX += 1
    if foodY % 2 != 0 : foodY += 1
    foodPos = [foodX*10, foodY*10]
    return foodPos
import pygame, random
from Snake import Snake

pygame.init()
screen = pygame.display.set_mode((800, 800))  # creates the screen
clock = pygame.time.Clock()  # creates clock object

# title and icon
pygame.display.set_caption('Snake')
icon = pygame.image.load('Snake.ico')
pygame.display.set_icon(icon)

# game variables
score = 0
animate = False
canTurn = True # used to prevent turning directly back on your tail

# snake
cubes = [Snake(382, 382, 0, 0)]
turnInfo = []
MOVESNAKE = pygame.USEREVENT
pygame.time.set_timer(MOVESNAKE, 75)  # snake speed

# apple
isApple = False
randX = 0
randY = 0


def draw_snake():
    for i in range(len(cubes)):
        pygame.draw.rect(screen, 'GREEN', pygame.Rect(cubes[i].x, cubes[i].y, 16, 16))


def turn(coordsAndDirection, i):
    xTurn, yTurn, tailXChange, tailYChange = coordsAndDirection
    delete = True
    for k in range(len(cubes)):
        if cubes[k].x == xTurn and cubes[k].y == yTurn:
            cubes[k].xChange = tailXChange
            cubes[k].yChange = tailYChange
            delete = False

    if delete == True:
        del turnInfo[i]


def get_rand_point():
    randX = random.randint(0, 39)
    randY = random.randint(0, 39)
    for cube in cubes:
        while cube.x == randX:
            randX = random.randint(0, 39)
        while cube.y == randY:
            randY = random.randint(0, 39)
    return (((randX * 20) + 2),((randY * 20) + 2))


def draw_apple(isApple):
    global randX
    global randY
    if isApple == False:
        randX, randY = get_rand_point()

    if len(cubes) != 1:
        for i in range(1,len(cubes)): # check if it spawned inside the snake
            if randX == cubes[i].x and randY == cubes[i].y:
                isApple = False
            else:
                isApple = True
    else:
        isApple = True

    pygame.draw.rect(screen, 'RED', pygame.Rect(randX, randY, 16, 16))
    return randX, randY, isApple


def isCollision(randX, randY):
    return randX == cubes[0].x and randY == cubes[0].y


def isDeath():
    if cubes[0].x > 800 or cubes[0].x < 0 or cubes[0].y > 800 or cubes[0].y < 0:
        return True

    for i in range(1,len(cubes)-1):
        headCoord = ((cubes[0].x, cubes[0].y))
        tailCoord = ((cubes[i].x, cubes[i].y))

        if headCoord == tailCoord:
            return True

    return False


def addLength():
    prevCube = cubes[len(cubes)-1]
    cubes.append(Snake(prevCube.x - prevCube.xChange,
                       prevCube.y - prevCube.yChange,
                       prevCube.xChange,
                       prevCube.yChange))


running = True
while running:

    screen.fill((0, 0, 0))  # fills screen color with rgb value

    for event in pygame.event.get():  # loops through each even possible in pygame
        if event.type == pygame.QUIT:  # checks if the X button has been pressed
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and cubes[0].xChange != -20 and canTurn == True:
                canTurn = False
                cubes[0].xChange = 20
                cubes[0].yChange = 0
                turnInfo.append((cubes[0].x, cubes[0].y, 20, 0))
            if event.key == pygame.K_LEFT and cubes[0].xChange != 20 and canTurn == True:
                canTurn = False
                cubes[0].xChange = -20
                cubes[0].yChange = 0
                turnInfo.append((cubes[0].x, cubes[0].y, -20, 0))
            if event.key == pygame.K_UP and cubes[0].yChange != 20 and canTurn == True:
                canTurn = False
                cubes[0].xChange = 0
                cubes[0].yChange = -20
                turnInfo.append((cubes[0].x, cubes[0].y, 0, -20))
            if event.key == pygame.K_DOWN and cubes[0].yChange != -20 and canTurn == True:
                canTurn = False
                cubes[0].xChange = 0
                cubes[0].yChange = 20
                turnInfo.append((cubes[0].x, cubes[0].y, 0, 20))

        if event.type == MOVESNAKE:
            if not animate:
                for i in range(len(cubes)):
                    cubes[i].move_snake()
                    canTurn = True
            elif len(cubes) > 1:
                del cubes[len(cubes)-1]

    for i in range(len(turnInfo)):
        if i < len(turnInfo):
            turn(turnInfo[i], i)

    # death
    if isDeath():
        animate = True

    if animate == True and len(cubes) == 1:
        running = False
        pygame.display.quit()
        animate = False

    draw_snake()

    # apple collision
    if isCollision(randX,randY):
        score += 1
        isApple = False
        addLength()

    randX, randY, isApple = draw_apple(isApple)

    clock.tick(144) # fps limit for game
    pygame.display.update()
print(f'Score = {score}')

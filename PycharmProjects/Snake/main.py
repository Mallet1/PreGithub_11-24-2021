import pygame, random, ctypes
from Snake import Snake
from tkinter import *
from PIL import ImageTk, Image

user32 = ctypes.windll.user32
screensize = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))  # get screensize
WIDTH, HEIGHT = screensize

print(WIDTH, HEIGHT)

def menu(score):
    def reset_high_score():
        highFile = open('HighScore.txt', 'w')
        highFile.write('0\n')
        highFile.close()


    def average_and_add_scores():
        avg = 0

        # saving high score
        with open('HighScore.txt') as file:
            highScore = file.readlines()

        # gets rid of \n
        highScore = ''.join(highScore)
        highScore = highScore.split('\n')

        if score > 0:
            highScore.append(f'{str(score)}')

        if score > int(highScore[0]):
            highScore[0] = (str(score))

        # writes new scores in file
        with open('HighScore.txt', 'w') as highFile:
            for this_score in highScore:
                if this_score != '':
                    avg += int(this_score)
                    highFile.write(f'{this_score}\n')

        if int(highScore[0]) > 0:
            avg = (avg-int(highScore[0])) / (len(highScore)-2)

        return (highScore[0], round(avg,2))

    global root

    highScore, avg = average_and_add_scores()


    root = Tk()

    root.title('Snake')
    root.geometry('400x400')
    root.iconbitmap('Snake.ico')

    backgroundImg = Image.open('SnakeBackground.png')
    backgroundImg = backgroundImg.resize((400, 400), Image.ANTIALIAS)
    background = ImageTk.PhotoImage(backgroundImg)

    backgroundLabel = Label(root, image=background)
    backgroundLabel.place(x=0, y=0, relwidth=1, relheight=1)

    snakeImage = ImageTk.PhotoImage(Image.open('SnakeImage.png'))
    if WIDTH < 1000 or HEIGHT < 1000:
        playButton = Button(backgroundLabel, image = snakeImage, width = 200, height = 64, bd = 10, bg = 'GREEN',
                            command = lambda: main_game(True))
    else:
        playButton = Button(backgroundLabel, image = snakeImage, width = 200, height = 64, bd = 10, bg = 'GREEN',
                            command = lambda: main_game(False))
    playButton.pack(pady = 50)

    scoreText = Button(backgroundLabel, text = f'Score: {score}\nHigh Score: {highScore}\nAverage Score: {avg}', bg = 'GREEN', bd = 10, font=('Helvetica',20))
    scoreText.pack(pady = 5)

    resetHigh = Button(backgroundLabel, text = 'Reset High Score', bg = 'green', bd = 5, font = ('Helvetica', 18), command = reset_high_score)
    resetHigh.pack(pady = 5)

    root.mainloop()

def main_game(small):
    root.destroy()

    pygame.init()
    if small:
        screen = pygame.display.set_mode((400, 400))  # creates the screen
    else:
        screen = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()  # creates clock object

    # title and icon
    pygame.display.set_caption('Snake')
    icon = pygame.image.load('Snake.ico')
    pygame.display.set_icon(icon)

    # game variables
    prevTailLoc = (-1,-1)
    score = 0
    animate = False
    canTurn = True # used to prevent turning directly back on your tail

    # snake
    cubes = [Snake(2, 2, 0, 0)]
    turnInfo = []
    MOVESNAKE = pygame.USEREVENT
    pygame.time.set_timer(MOVESNAKE, 75)  # snake speed

    # apple
    isApple = False
    randX = 0
    randY = 0


    def draw_snake():
        for i in range(len(cubes)):
            if small:
                pygame.draw.rect(screen, 'GREEN', pygame.Rect(cubes[i].x, cubes[i].y, 8, 8))
            else:
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
        if small:
            randX = random.randint(0, 19)
            randY = random.randint(0, 19)

            for cube in cubes:
                while cube.x == randX:
                    randX = random.randint(0, 19)
                while cube.y == randY:
                    randY = random.randint(0, 19)
            return (((randX * 10) + 2),((randY * 10) + 2))

        else:
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
            for i in range(len(cubes)): # check if it spawned inside the snake
                if randX == cubes[i].x and randY == cubes[i].y:
                    isApple = False
                    break # exit loop if there apple spawns in any cubes
                else:
                    isApple = True
        else:
            isApple = True

        if small:
            pygame.draw.rect(screen, 'RED', pygame.Rect(randX, randY, 8, 8))
        else:
            pygame.draw.rect(screen, 'RED', pygame.Rect(randX, randY, 16, 16))
        return randX, randY, isApple


    def isCollision(randX, randY):
        return randX == cubes[0].x and randY == cubes[0].y


    def isDeath():
        if small:
            if cubes[0].x > 800 or cubes[0].x < 0 or cubes[0].y > 800 or cubes[0].y < 0:
                return True
        else:
            if cubes[0].x > 800 or cubes[0].x < 0 or cubes[0].y > 800 or cubes[0].y < 0:
                return True

        for i in range(1,len(cubes)-1):
            headCoord = ((cubes[0].x, cubes[0].y))
            tailCoord = ((cubes[i].x, cubes[i].y))

            if headCoord == tailCoord:
                return True

        return False


    def addLength(prevTailLoc):
        newX, newY, newXChange, newYChange = prevTailLoc
        cubes.append(Snake(newX,
                           newY,
                           newXChange,
                           newYChange))

    running = True
    while running:

        screen.fill((0, 0, 0))  # fills screen color with rgb value

        for event in pygame.event.get():  # loops through each even possible in pygame
            if event.type == pygame.QUIT:  # checks if the X button has been pressed
                running = False
            if event.type == pygame.KEYDOWN:
                if small:
                    if event.key == pygame.K_RIGHT and cubes[0].xChange != -10 and canTurn == True:
                        canTurn = False
                        cubes[0].xChange = 10
                        cubes[0].yChange = 0
                        turnInfo.append((cubes[0].x, cubes[0].y, 10, 0))
                    if event.key == pygame.K_LEFT and cubes[0].xChange != 10 and canTurn == True:
                        canTurn = False
                        cubes[0].xChange = -10
                        cubes[0].yChange = 0
                        turnInfo.append((cubes[0].x, cubes[0].y, -10, 0))
                    if event.key == pygame.K_UP and cubes[0].yChange != 10 and canTurn == True:
                        canTurn = False
                        cubes[0].xChange = 0
                        cubes[0].yChange = -10
                        turnInfo.append((cubes[0].x, cubes[0].y, 0, -10))
                    if event.key == pygame.K_DOWN and cubes[0].yChange != -10 and canTurn == True:
                        canTurn = False
                        cubes[0].xChange = 0
                        cubes[0].yChange = 10
                        turnInfo.append((cubes[0].x, cubes[0].y, 0, 10))

                else:
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
                    lastIndex = len(cubes) - 1
                    prevTailLoc = (cubes[lastIndex].x,
                                   cubes[lastIndex].y,
                                   cubes[lastIndex].xChange,
                                   cubes[lastIndex].yChange) # save last cube location to be placed if apple eaten

                    for i in range(len(cubes)):
                        cubes[i].move_snake()
                        canTurn = True

                elif len(cubes) > 1:
                    del cubes[len(cubes)-1]

        # apple collision
        if isCollision(randX, randY):
            score += 1
            isApple = False
            addLength(prevTailLoc)

        for i in range(len(turnInfo)):
            if i < len(turnInfo):
                turn(turnInfo[i], i)

        # death
        if isDeath():
            animate = True

        if animate == True and (len(cubes) == 1 or len(cubes) > 20):
            running = False
            menu(score)
            pygame.display.quit()
            animate = False

        draw_snake()

        randX, randY, isApple = draw_apple(isApple)

        clock.tick(144) # fps limit for game
        pygame.display.update()

menu(0)
import pygame, random, math, time
from pygame import mixer

pygame.init()  # initializes pygame

# (width, height)
screen = pygame.display.set_mode((800, 600))  # creates the screen

# background
background = pygame.image.load('SpaceBackground.png')

# background sound
#mixer.music.load('background.wav')
#mixer.music.play(-1) # -1 to loop

# title and icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('UFO.png')
pygame.display.set_icon(icon)  # adds the icon

# player
keys_down = {'left': False, 'right': False, 'space': False}
playerImg = pygame.image.load('SpaceShip.png')  # creates the spaceship to be placed on the screen
playerX = 370
playerY = 480
playerX_change = 0

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
numOfEnemies = 6

for i in range(numOfEnemies):
    enemyImg.append(pygame.image.load('SpaceEnemy.png'))  # creates the enemy spaceship to be placed on the screen
    enemyX.append(random.randint(100, 700))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# bullet
bulletImg = pygame.image.load('ArcadeBullet.png')  # creates the enemy spaceship to be placed on the screen
bulletX = playerX
bulletY = playerY
bulletX_change = 0
bulletY_change = 10
bulletState = 'ready'

# powerups
powerUp_Chance = 0
powerUp = 'ready'
displayTime = 0

# slow time
timeSlowImg = pygame.image.load('SlowTime.png')
timeSlowX = 0
timeSlowY = 0
timeSlowY_change = 4

# penetration
penetrateImg = pygame.image.load('Penetrate.png')
penetrateX = 0
penetrateY = 0
penetrateY_change = 4

# score
scoreValue = 0
font = pygame.font.Font('freesansbold.ttf',32) # creates font object to be rendered later
# you can download new fonts at dafont.com

# game over declaration

overFont = pygame.font.Font('freesansbold.ttf',64)

textX = 10
textY = 10


penetrateStart = False
penetrateBegin = 0
slowStart = False
slowBegin = 0
def slowTime():
    global powerUp
    global slowBegin
    global slowStart

    if slowStart == False:
        slowBegin = time.time()
        slowStart = True

    slowEnd = time.time()-slowBegin # calculate how many seconds

    showScore(textX, textY, powerUp, str(10 - int(slowEnd)))

    if slowEnd >= 10:  # if seconds is greater than or equal to 10 stop slowmo power up
        powerUp = 'ready'
        slowStart = False


def placeSlowTime(x,y):
    screen.blit(timeSlowImg, (x, y))


def placePenetrate(x,y):
    screen.blit(penetrateImg, (x, y))


def randPowerUp():
    return random.randint(1,20)


def showScore(x,y,currentPower,timeLimit):
    power = ''
    if currentPower == 'slowGo':
        power = 'Slow Mo Time: '
    if currentPower == 'penetrateGo':
        power = 'Penetration Time: '

    score = font.render('Score: ' + str(scoreValue)+'                     '
                                                    +power+str(timeLimit),True, (255,255,255)) # renders the text
    # (text,True,color)

    screen.blit(score, (x, y)) # displays the text


def gameOver():
    overText = overFont.render('GAME OVER', True, (255, 255, 255))
    screen.blit(overText, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))  # draws the spaceship on the screen
    # (image, (coordinates X, coordinates Y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fireBullet(x, y):
    global bulletState
    bulletState = 'fire'
    screen.blit(bulletImg, (x + 24, y + 10))


def isCollision(x1, y1, x2, y2):
    distance = math.sqrt((math.pow(x2 - x1, 2)) + (math.pow(y2 - y1, 2)))
    if distance < 27:
        return True
    return False


def enemyMovement(i,change):
    enemyX[i] += enemyX_change[i]
    if enemyX[i] <= 0:  # checking for enemy boundaries
        enemyX_change[i] = change
        enemyY[i] += enemyY_change[i]
    elif enemyX[i] >= 736:
        enemyX_change[i] = -change
        enemyY[i] += enemyY_change[i]






# game loop
running = True
while running:

    screen.fill((0, 0, 0))  # fills screen color with rgb value

    # background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():  # loops through each even possible in pygame
        if event.type == pygame.QUIT:  # checks if the X button has been pressed
            running = False
            print('score = '+str(scoreValue))

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keys_down['left'] = True
            if event.key == pygame.K_RIGHT:
                keys_down['right'] = True
            if event.key == pygame.K_SPACE and bulletState == 'ready':
                bulletSound = mixer.Sound('laser.wav') # adds laser sound
                bulletSound.play()
                bulletX = playerX
                fireBullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys_down['left'] = False
            if event.key == pygame.K_RIGHT:
                keys_down['right'] = False

    if keys_down['left']:
        playerX_change = -6

    if keys_down['right']:
        playerX_change = 6

    if (keys_down['left'] and keys_down['right']):
        playerX_change = 0

    if not keys_down['left'] and not keys_down['right']:
        playerX_change = 0

    print(f'right: {keys_down["right"]}, left: {keys_down["left"]}')

    playerX += playerX_change

    if playerX <= 0:  # keeps it in the bounds of the screen
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # enemy movement
    if powerUp != 'slowGo': # only move normal if not slow mo power up
        for i in range(numOfEnemies):
            enemyMovement(i,4)

    for i in range(numOfEnemies):

        # game over
        if enemyY[i] > 440:
            for j in range(numOfEnemies):
                enemyY[j]=2000
            gameOver()
            break

        # collision
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            #explosionSound = mixer.Sound('explosion.wav') # adds explosion sound
            #explosionSound.play()
            if powerUp != 'penetrateGo':
                bulletY = 480
                bulletState = 'ready'
            scoreValue += 1
            enemyX[i] = random.randint(100, 700)
            enemyY[i] = random.randint(50, 150)
            if randPowerUp() == 5 and powerUp == 'ready': # check for slow time power up
                powerUp = 'slowMove'
                timeSlowX = enemyX[i]
                timeSlowY = enemyY[i]
            if randPowerUp() == 4 and powerUp == 'ready':
                powerUp = 'penetrate'
                penetrateX = enemyX[i]
                penetrateY = enemyY[i]

        enemy(enemyX[i], enemyY[i], i)

        if isCollision(enemyX[i],enemyY[i],playerX,playerY):
            running = False

    if bulletY <= 0:
        bulletY = 480
        bulletState = 'ready'

    # bullet movement
    if bulletState == 'fire':
        fireBullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # MAKE POWER UPS WITH OOP LATER

    # slowTime movement
    if powerUp == 'slowMove':
        timeSlowY += timeSlowY_change
        placeSlowTime(timeSlowX,timeSlowY)
        if isCollision(playerX,playerY,timeSlowX,timeSlowY):
            powerUp = 'slowGo'
            placeSlowTime(0,-100)
        elif timeSlowY >= 600:
            powerUp = 'ready'

    # slowTime power up functioning
    if powerUp == 'slowGo':
        for i in range(numOfEnemies):
            enemyMovement(i, 2)
        slowTime()

    # penetrate movement
    if powerUp == 'penetrate':
        penetrateY += penetrateY_change
        placePenetrate(penetrateX,penetrateY)
        if isCollision(playerX,playerY,penetrateX,penetrateY):
            powerUp = 'penetrateGo'
            placePenetrate(0,-100)
        elif penetrateY >= 600:
            powerUp = 'ready'

    # penetrate power up functioning
    if powerUp == 'penetrateGo':
        if penetrateStart == False:
            penetrateBegin = time.time()
            penetrateStart = True

        penetrateEnd = time.time() - penetrateBegin  # calculate how many seconds

        showScore(textX, textY, powerUp, str(20-int(penetrateEnd))) # display the power up timer
        # penetrateEnd is an int to take off the long decimal

        if penetrateEnd >= 20:  # if seconds is greater than or equal to 10 stop slowmo power up
            powerUp = 'ready'
            penetrateStart = False

    player(playerX, playerY)
    showScore(textX, textY, '', '')
    pygame.display.update()  # to make sure everything we add gets updated in real time

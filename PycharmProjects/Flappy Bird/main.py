import pygame, random


def drawFloor(): # blits 2 floor surfaces right next to each other
    screen.blit(floorSurface,(floorX,450))
    screen.blit(floorSurface,(floorX+288, 450))


def createPipe():
    randomPipePos = random.choice(pipeHeight) # chooses random number out of the list
    bottomPipe = pipeSurface.get_rect(midtop = (350,randomPipePos)) # makes new bottom pipe moves from top
    topPipe = pipeSurface.get_rect(midbottom = (350,randomPipePos-100)) # makes new top pipe moves from bottom

    return bottomPipe,topPipe


def checkScoreInc(score, highScore):
    for pipe in pipeList:
        if pipe.centerx == 50 and gameActive == True:
            scoreSound.play()
            score += .5
    if score > highScore:
        highScore = score
    return score, highScore


def movePipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 1
    return pipes


def drawPipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 512:
            screen.blit(pipeSurface,pipe)
        else:
            flipPipe = pygame.transform.flip(pipeSurface,False,True) # flips pipe (surface,flipX?,flipY?)
            screen.blit(flipPipe, pipe)


def checkCollision(pipes):
    for pipe in pipes:
        if birdRect.colliderect(pipe): # checks if the bird rect is colliding with the pipe rect
            deathSound.play()
            return False

    if birdRect.top <= -100 or birdRect.bottom >= 450:
        return False

    return True


def rotateBird(bird):
    newBird = pygame.transform.rotozoom(bird, birdMovement * -10,1) # can scale and rotate a surface
    # (surface, rotation, scale)

    return newBird


def animateBird():
    newBird = birdFrames[birdIndex]
    newBirdRect = newBird.get_rect(center = (50,birdRect.centery)) # take the previous y of the current bird and creates the new one at the same location
    return newBird,newBirdRect


def displayScore(gameState):
    if gameState == 'main_game':
        scoreSurface = gameFont.render(str(int(score)), True,(255, 255, 255))  # (text,anti-aliased (usually true),RGB tuple)
        scoreRect = scoreSurface.get_rect(center=(144, 50))
        screen.blit(scoreSurface, scoreRect)

    if gameState == 'game_over':
        scoreSurface = gameFont.render(f'Score {int(score)}', True,(255, 255, 255))  # (text,anti-aliased (usually true),RGB tuple)
        scoreRect = scoreSurface.get_rect(center=(144, 50))
        screen.blit(scoreSurface, scoreRect)

        highScoreSurface = gameFont.render(f'High Score {int(highScore)}', True,(255, 255, 255))  # (text,anti-aliased (usually true),RGB tuple)

        # ^^ f string, REMEMBER THIS

        highScoreRect = highScoreSurface.get_rect(center=(144, 425))
        screen.blit(highScoreSurface, highScoreRect)


def animateTitleScreen():
    global gravity
    global birdMovement
    screen.blit(gameOverSurface, gameOverRect)
    birdMovement = 0
    if birdRect.centery <= 270:
        gravity += .05
    if birdRect.centery >= 300:
        gravity -= .05


def gameOverAnimate():
    global birdMovement
    birdMovement += gravity
    rotatedBird = rotateBird(birdSurface)
    birdRect.centery += birdMovement
    screen.blit(rotatedBird, birdRect)

    if birdRect.bottom >= 450:
        birdMovement = 0
        return False
    return True


#pygame.mixer.pre_init(frequency = 44100, size = 16, channels = 1, buffer = 512) # tells pygame.init() to initiate
pygame.init()
screen = pygame.display.set_mode((288,512))
clock = pygame.time.Clock() # creates clock object
gameFont = pygame.font.Font('04B_19.TTF',20)

# title and icon
pygame.display.set_caption('Flappy Bird')
icon = pygame.image.load('FlappyIcon.ico')
pygame.display.set_icon(icon)

# game variables
gravity = .075
birdMovement = 0
gameActive = True
score = 0
highScore = 0
end = False
titleScreen = True
pipesReady = False

# background
bgSurface = pygame.image.load('background-day.png').convert() # day background; convert helps pygame run
#bgSurface = pygame.transform.scale2x(bgSurface) # doubles the size of the background image

# base
floorSurface = pygame.image.load('base.png').convert()
floorX = 0

# bird
birdDownflap = pygame.image.load('yellowbird-downflap.png').convert_alpha()
birdMidflap = pygame.image.load('yellowbird-midflap.png').convert_alpha()
birdUpflap = pygame.image.load('yellowbird-upflap.png').convert_alpha()
birdFrames = [birdDownflap,birdMidflap,birdUpflap]
birdIndex = 0
birdSurface = birdFrames[birdIndex]
birdRect = birdSurface.get_rect(center = (50,256))

BIRDFLAP = pygame.USEREVENT + 1 # + 1 so that it doesn't change the spawn pipe user event
pygame.time.set_timer(BIRDFLAP,200)

#birdSurface = pygame.image.load('yellowbird-downflap.png').convert_alpha() # the alpha is to get rid of the black box ; delete the _alpha to see what I mean
#birdRect = birdSurface.get_rect(center = (50,256)) # creates rectangle around the bird

# pipes
pipeSurface = pygame.image.load('pipe-green.png')
pipeList = []
pipeRects = []
SPAWNPIPE = pygame.USEREVENT # spawnpipe userevent to be triggered by timer
pygame.time.set_timer(SPAWNPIPE,1500) # SPAWNPIPE triggered every 1.5 seconds
pipeHeight = [i for i in range(200,400)] # possible pipe locations

gameOverSurface = pygame.image.load('message.png').convert_alpha()
gameOverRect = gameOverSurface.get_rect(center = (144,200))

flapSound = pygame.mixer.Sound('sound_sfx_wing.wav')
deathSound = pygame.mixer.Sound('sound_sfx_hit.wav')
scoreSound = pygame.mixer.Sound('sound_sfx_point.wav')
dieSound = pygame.mixer.Sound('sound_sfx_die.wav')
swooshSound = pygame.mixer.Sound('sound_sfx_swooshing.wav')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.type == pygame.MOUSEBUTTONDOWN) and end == False:
                if titleScreen == True:
                    titleScreen = False
                birdMovement = 0
                birdMovement -= 2.5
                flapSound.play()
                if gameActive == False:
                    swooshSound.play()
                    titleScreen = True
                    gameActive = True
                    pipeList.clear() # clears the pipe list
                    birdRect.center = (50, 256)
                    birdMovement = 0
                    score = 0

        if event.type == BIRDFLAP and birdIndex < 2 and end == False: # every .2 seconds the bird image changes to create the animation
            birdIndex += 1
        elif end == False:
            birdIndex = 0

        birdSurface,birdRect = animateBird()

        if event.type == SPAWNPIPE and pipesReady: # runs each time SPAWNPIPE is triggered so every 1.2 seconds
            pipeList.extend(createPipe()) # .extend adds a tuple

    screen.blit(bgSurface,(0,0)) # blits background
    if pipesReady:
        drawPipes(pipeList)
    drawFloor()


    if end == True:
        end = gameOverAnimate() # animates falling bird and returns False when bird passes y 450
    elif gameActive == False:
        screen.blit(rotateBird(birdSurface), birdRect) # keeps bird at the bottom of the screen

    if gameActive:
        # bird movement


        if titleScreen == True:
            animateTitleScreen()
            pipesReady = False
        else:
            gravity = .075
            pipesReady = True

        birdMovement += gravity # gives bird gravity

        rotatedBird = rotateBird(birdSurface)

        birdRect.centery += birdMovement # gives bird's rectangle the same gravity
        # centery and centerx is the only way to move the rectangle
        screen.blit(rotatedBird,birdRect)
        gameActive = checkCollision(pipeList)

        if pipesReady:
            # pipe movement
            pipeList = movePipes(pipeList)
            if checkCollision(pipeList) == False:
                dieSound.play()
                end = True

        # floor movement
        floorX -= .6
        if floorX <= -288:  # checks when floor is off screen and teleports it back to start pos
            floorX = 0

        displayScore('main_game')  # blits score
    else:
        displayScore('game_over')

    score, highScore = checkScoreInc(score,highScore)



    clock.tick(144) # fps limit for game
    pygame.display.update()

import pygame, random
from Entity import Entity

pygame.init()  # initializes pygame

# (width, height)
screen = pygame.display.set_mode((800, 600))  # creates the screen

# background
background = pygame.image.load('SpaceBackground.png')

# title and icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('UFO.png')
pygame.display.set_icon(icon)  # adds the icon

# game variables
score = 0

# player
player = Entity('SpaceShip.png',370,480,0,0,'')

# enemy
num_of_enemies = 6
enemy = [Entity('SpaceEnemy.png', random.randint(100, 700), random.randint(50, 150), 4, 40, '') for i in range(num_of_enemies)] # makes enemies

# bullet
bullet = Entity('ArcadeBullet.png', player.x, player.y, 0, 10, 'ready')

def place_player():
    screen.blit(player.image, (player.x,player.y))

def enemyMovement(i):
    enemy[i].x += enemy[i].xChange
    if enemy[i].x <= 0:  # checking for enemy boundaries
        enemy[i].xChange = 4
        enemy[i].y += enemy[i].yChange
    elif enemy[i].x >= 736:
        enemy[i].xChange = -4
        enemy[i].y += enemy[i].yChange

def fireBullet():
    bullet.y -= bullet.yChange
    bullet.state = 'fire'
    screen.blit(bullet.image, (bullet.x + 24, bullet.y + 10))

def isCollision(rect1, rect2):
    return rect1.colliderect(rect2)

def enemyReset(i):
    enemy[i].x = random.randint(100, 700)
    enemy[i].y = random.randint(50, 150)

def bulletReset():
    bullet.y = 2000
    bullet.state = 'ready'



# game loop
running = True
while running:

    screen.fill((0, 0, 0))  # fills screen color with rgb value

    # background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():  # loops through each even possible in pygame
        if event.type == pygame.QUIT:  # checks if the X button has been pressed
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.xChange = -6
            if event.key == pygame.K_RIGHT:
                player.xChange = 6
            if event.key == pygame.K_SPACE and bullet.state == 'ready':
                bullet.y = 480
                bullet.x = player.x
                fireBullet()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.xChange = 0

    # player movement
    player.x += player.xChange

    if player.x <= 0:  # keeps it in the bounds of the screen
        player.x = 0
    elif player.x >= 736:
        player.x = 736

    # enemy movement
    for i in range(num_of_enemies):
        enemyMovement(i)
        screen.blit(enemy[i].image, (enemy[i].x, enemy[i].y))

        if isCollision(enemy[i].getRect(), player.getRect()) == True: # check if enemy hits player
            running = False

        if isCollision(enemy[i].getRect(), bullet.getRect()) == True:
            score += 1
            bulletReset()
            enemyReset(i)


    # bullet movement
    if bullet.y <= 0:
        bulletReset()

    if bullet.state == 'fire':
        fireBullet()



    place_player()
    pygame.display.update()  # to make sure everything we add gets updated in real time

print(f'Score = {score}')
import pygame, ctypes
from Entity import Entity

pygame.init()

user32 = ctypes.windll.user32
screensize = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)-60) # get screensize
WIDTH, HEIGHT = screensize
print(WIDTH, HEIGHT)
screen = pygame.display.set_mode(screensize)  # creates the screen (width, height)

clock = pygame.time.Clock()  # creates clock object

# title and icon
pygame.display.set_caption('Platformer')
# icon = pygame.image.load()
# pygame.display.set_icon(icon)

# game variables
gravity = -.01
collision = False
current_wall = ''
current_wall_index = -1
platforms = [Entity(x = 0, y = HEIGHT - (HEIGHT / 51),width = WIDTH,height = HEIGHT / 51, color = 'GREEN'),
Entity(x = 0, y = 0,width = WIDTH,height = HEIGHT / 51, color = 'GREEN'),
Entity(x = WIDTH-200, y = HEIGHT-500,width = WIDTH/100,height = 400, color = 'GREEN'),
# Entity(x = 0, y = 100,width = 20,height = HEIGHT, color = 'GREEN')
]

# player
coordinates = []
player = Entity(x = WIDTH / 2, y = HEIGHT / 2, width = 5, height = 15, yChange = 1, color = 'RED') # player object
can_jump = True
wall_jump = False
jumping = False

def place_rect(x, y, width, height, color):
    pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))
    return pygame.Rect(x, y, width, height)


def move_player():
    # player.x += player.xChange
    player.y += player.yChange
    for platform in platforms:
        platform.x += platform.xChange


def is_collision(rect1, rect2):
    print('collision')
    return rect1.colliderect(rect2)


def check_wall_jump(index): # make it so when the player drops beneath a block they can't wall jump
    return not (abs(platform_rects[index].right - player_rect.left) >= 2 and current_wall == 'right' or
           abs(platform_rects[index].left - player_rect.right) >= 2 and current_wall == 'left' or
           platform_rects[index].bottom < player_rect.top or platform_rects[index].top > player_rect.bottom)


running = True
while running:
    screen.fill((0, 0, 0))  # fills screen color with rgb value

    for event in pygame.event.get():  # loops through each even possible in pygame
        if event.type == pygame.QUIT:  # checks if the X button has been pressed
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # player.xChange = -3
                for platform in platforms:
                    platform.xChange = 3
            if event.key == pygame.K_RIGHT:
                # player.xChange = 3
                for platform in platforms:
                    platform.xChange = -3
            if event.key == pygame.K_SPACE and (can_jump is True or wall_jump is True):
                if wall_jump:
                    if current_wall == 'left':
                        player.xChange = -2
                    if current_wall == 'right':
                        player.xChange = 2

                player.y -= .01
                player.yChange = -4
                can_jump = False
                wall_jump = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.xChange = 0
                for platform in platforms:
                    platform.xChange = 0

    # player
    player_rect = pygame.Rect(player.x, player.y, player.width, player.height) # get player rectangle object
    move_player()


    # platforms
    platform_rects = []
    for platform in platforms:
        platform_rects.append(pygame.Rect(platform.x, platform.y, platform.width, platform.height)) # get platorm rectangle objects
        place_rect(platform.x, platform.y, platform.width, platform.height, platform.color) # place platforms

    # check player and platforms collisions
    for i, platform_rect in enumerate(platform_rects):


        # check for collision in x direction
        if is_collision(player_rect, pygame.Rect(platforms[i].x + platforms[i].xChange, platforms[i].y, platforms[i].width, platforms[i].height)):
            if platforms[i].xChange < 0 and abs(platform_rect.left - player_rect.right) <= 1:  # hitting left side
                wall_jump = True
                current_wall = 'left'
                current_wall_index = i
                player.x = platform_rect.left - player.width
                platforms[i].xChange = 0
            elif platforms[i].xChange > 0 and abs(platform_rect.right - player_rect.left) <= 1:  # hitting right side
                wall_jump = True
                current_wall = 'right'
                current_wall_index = i
                player.x = platform_rect.right
                platforms[i].xChange = 0

        # don't allow a wall jump if the player is too far away from a wall
        if wall_jump:
            wall_jump = check_wall_jump(current_wall_index)

        # check for collision in y direction
        if is_collision(player_rect, pygame.Rect(platforms[i].x, platforms[i].y - player.yChange, platforms[i].width, platforms[i].height)):
            if player.yChange > 0 and player_rect.bottom <= platform_rect.top: # landing on platform
                if player.xChange == 2 or player.xChange == -2: # end wall jump
                    player.xChange = 0

                current_wall = 'top'
                current_wall_index = i
                can_jump = True
                player.y = platform_rects[i].top - player.height
                player.yChange = 0
            elif player.yChange < 0 and player_rect.top >= platform_rect.bottom: # player hitting underside of platform
                current_wall = 'bottom'
                current_wall_index = i
                player.y = platform_rect.bottom
                player.yChange = 0
        else:
            player.yChange -= gravity

    if player.x >= WIDTH:
        player.xChange = 0
        player.x = WIDTH - player.width - 0.01
    if player.x <= 0:
        player.xChange = 0
        player.x = 0.01
    if player.y <= 0:
        player.yChange = 0
        player.y = 0.01

    # if you are near a wall get rid of gravity for wall jump
    if wall_jump:
        if player.yChange >= .8: # get rid of gravity once yChange reaches
            gravity = 0
    else:
        gravity = -.01

    place_rect(player.x, player.y, player.width, player.height, player.color) # place player needs to be at the end to avoid clipping through objects


    clock.tick(144) # fps limit for game
    pygame.display.update()

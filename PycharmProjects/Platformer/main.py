import pygame, ctypes

from Entity import Entity

pygame.init()

user32 = ctypes.windll.user32
screensize = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1) - 60)  # get screensize
WIDTH, HEIGHT = screensize
print(WIDTH, HEIGHT)
screen = pygame.display.set_mode(screensize)  # creates the screen (width, height)

clock = pygame.time.Clock()  # creates clock object

# title and icon
pygame.display.set_caption('Platformer')
# icon = pygame.image.load()
# pygame.display.set_icon(icon)

# game variables
keys_down = {'left': False, 'right': False, 'space': False}
gravity = -.05
current_elevators = []
current_wall = ''
current_wall_key = ''

# platforms
platforms = {'floor': Entity(x=0, y=HEIGHT - (HEIGHT / 51), width=WIDTH, height=HEIGHT / 51, color='GREEN'),
             'left_platform': Entity(x=WIDTH / 20, y=HEIGHT - 500, width=WIDTH / 100, height=400, color='GREEN'),
             'middle_platform': Entity(x=WIDTH / 2, y=HEIGHT / 2, width=200, height=400, color='GREEN'),
             'left_wall': Entity(x=0, y=100, width=20, height=HEIGHT, color='GREEN'),
             'elevator': Entity(x=WIDTH - 100, y=HEIGHT - (HEIGHT / 51) - 20, width=80, height=20, color='GRAY'),
             'other_elevator': Entity(x=WIDTH - 300, y=HEIGHT - (HEIGHT / 51) - 20, width=80, height=20, color='GRAY'),
             'exit': Entity(x=WIDTH/2, y=200, width=500, height=20, color='GREEN'),
             }
elevator_heights = {'elevator': 600, 'other_elevator': 200, 'long_elevator': 200}

for platform_name in platforms.keys(): # makes sure elevator heights includes all elevators
    if 'elevator' in platform_name and platform_name not in elevator_heights.keys():
        raise Exception("Error: number of elevators don't match")

# player
right_animate = ['player_right_neutral.png', 'player_right_right_up.png', 'player_right_left_up.png']
left_animate = ['player_left_neutral.png', 'player_left_left_up.png', 'player_left_right_up.png']
player = Entity(x=WIDTH / 2, y=HEIGHT / 2, width=5, height=15, yChange=1, color='RED', image = 'player_right_neutral.png')  # player object
new_image = 0
can_jump = False
wall_jump = False
is_jumping = False

ANIMATEPLAYER = pygame.USEREVENT
pygame.time.set_timer(ANIMATEPLAYER, 75) # speed of player animation in milliseconds


def get_image(image):
    return pygame.image.load(image)


def place_rect(x, y, width, height, color):
    pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))


def place_img(entity):
    screen.blit(entity.image, (entity.x, entity.y))


def move_player():
    player.x += player.xChange
    player.y += player.yChange


def animate_player(new_image):
    if player.xChange > 0:
        player.set_image(right_animate[new_image])

    elif player.xChange < 0:
        player.set_image(left_animate[new_image])

def move_platforms(key):
    platforms[key].x += platforms[key].xChange
    platforms[key].y += platforms[key].yChange


def is_collision(rect1, rect2):
    return rect1.colliderect(rect2)


def check_wall_jump(key):  # make it so when the player drops beneath a block they can't wall jump
    return not (abs(platform_rects[key].right - player_rect.left) >= 2 and current_wall == 'right' or
                abs(platform_rects[key].left - player_rect.right) >= 2 and current_wall == 'left' or
                platform_rects[key].bottom < player_rect.top or platform_rects[key].top > player_rect.bottom)


def elevator_motion(elevator, y_stop):
    if platforms[elevator].y <= y_stop:
        platforms[elevator].yChange = 1
    if platforms[elevator].y >= HEIGHT - (HEIGHT / 51) - 20:
        platforms[elevator].yChange = 0


def on_block(rect, block_rect):
    return abs(block_rect.top - rect.bottom) <= 1\
            and rect.left < block_rect.right - 4\
            and rect.right > block_rect.left + 4


running = True
while running:
    screen.fill((52, 177, 235))  # fills screen color with rgb value



    for event in pygame.event.get():  # loops through each even possible in pygame
        if event.type == pygame.QUIT:  # checks if the X button has been pressed
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keys_down['left'] = True
            if event.key == pygame.K_RIGHT:
                keys_down['right'] = True
            if event.key == pygame.K_SPACE and (can_jump is True or wall_jump is True):
                if wall_jump:
                    is_jumping = True
                    if current_wall == 'left':
                        player.xChange = -2
                    if current_wall == 'right':
                        player.xChange = 2

                player.y -= 2
                player.yChange = -4
                can_jump = False
                wall_jump = False
                if player.image is not None:
                    new_image = 0
                    animate_player(new_image) # when space is pressed put player in neutral position in the current direction

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                if player.image is not None:
                    new_image = 0
                    animate_player(new_image) # when player lets go of key put player in neutral position in the right direction

                keys_down['left'] = False
            if event.key == pygame.K_RIGHT:
                if player.image is not None:
                    new_image = 0
                    animate_player(new_image) # when player lets go of key put player in neutral position in the right direction

                keys_down['right'] = False

        if event.type == ANIMATEPLAYER and player.image is not None:
            animate_player(new_image)
            if player.xChange != 0 and can_jump:
                if new_image < 2:
                    new_image += 1
                else:
                    new_image = 0

    # better movement system
    if keys_down['left']:
        is_jumping = False
        player.xChange = -3

    if keys_down['right']:
        is_jumping = False
        player.xChange = 3

    if ((keys_down['left'] and keys_down['right'])):
        is_jumping = False
        player.xChange = 0

    if (not keys_down['left'] and not keys_down['right']) and is_jumping is False:
        player.xChange = 0



    # player
    if player.image is None:
        player_rect = pygame.Rect(player.x, player.y, player.width, player.height)  # get player rectangle object
    else:
        player_rect = player.rect
        player_rect.update(player.x, player.y, player_rect.width, player_rect.height)
        # continuously update to rect to have equal dimensions to the player Entity object

    move_player()




    # platforms
    platform_rects = {}
    for key, value in platforms.items():
        if key not in platform_rects.keys():
            platform_rects[key] = pygame.Rect(value.x, value.y, value.width, value.height)  # get platform rectangle objects
        place_rect(value.x, value.y, value.width, value.height, value.color)  # place platforms
        move_platforms(key)

        # keep player on moving platforms
        if on_block(player_rect, platform_rects[key]):
            player.y = platforms[key].y - player_rect.height
            player.yChange = platforms[key].yChange

    # player can't jump if they fall off platform
    if current_wall_key in platforms.keys() and abs(player.yChange - platforms[current_wall_key].yChange) > .5:
        can_jump = False

    # elevators
    for i, elevator in enumerate(current_elevators):
        current_elevator_height = elevator_heights[elevator]

        elevator_motion(elevator, current_elevator_height) # list of elevators, height of elevator

        if platforms[elevator].yChange == 0:
            del current_elevators[i]

    # check player and platforms collisions
    for i, key in enumerate(platform_rects.keys()):

        # check for collision in x direction
        if is_collision(pygame.Rect(player.x + player.xChange, player.y, player_rect.width, player_rect.height), platform_rects[key]):
            if player.xChange > 0 and abs(platform_rects[key].left - player_rect.right) <= 1:  # hitting left side
                wall_jump = True
                current_wall = 'left'
                current_wall_key = key
                player.x = platform_rects[key].left - player_rect.width
                player.xChange = platforms[key].xChange
            elif player.xChange < 0 and abs(platform_rects[key].right - player_rect.left) <= 1:  # hitting right side
                wall_jump = True
                current_wall = 'right'
                current_wall_key = key
                player.x = platform_rects[key].right
                player.xChange = platforms[key].xChange

        # don't allow a wall jump if the player is too far away from a wall
        if wall_jump:
            wall_jump = check_wall_jump(current_wall_key)

        # check for collision in y direction
        if is_collision(pygame.Rect(player.x, player.y + player.yChange, player_rect.width, player_rect.height), platform_rects[key]):

            if player.yChange > 0 and player_rect.bottom <= platform_rects[key].top:  # landing on platform

                if player.xChange == 2 or player.xChange == -2:  # end wall jump
                    player.xChange = 0

                current_wall = 'top'
                current_wall_key = key

                # add current working elevators to list when player steps on one
                if 'elevator' in current_wall_key and current_wall == 'top' and current_wall_key not in current_elevators:
                    current_elevators.append(current_wall_key)
                    platforms[current_wall_key].yChange = -1

                can_jump = True
                player.y = platform_rects[key].top - player_rect.height
                player.yChange = platforms[key].yChange

            elif player.yChange < 0 and player_rect.top >= platform_rects[key].bottom:  # player hitting underside of platform

                current_wall = 'bottom'
                current_wall_key = key
                player.y = platform_rects[key].bottom
                player.yChange = platforms[key].yChange

    player.yChange -= gravity

    if player.x >= WIDTH:
        player.xChange = 0
        player.x = WIDTH - player_rect.width - 0.01
    if player.x <= 0:
        player.xChange = 0
        player.x = 0.01
    if player.y <= 0:
        player.yChange = 0
        player.y = 0.01

    # if you are near a wall get rid of gravity for wall jump
    if wall_jump:
        if player.yChange >= .8:  # don't let yChange exceed this number while on wall
            player.yChange = .8

    # place player needs to be at the end to avoid clipping through objects
    if player.image is None:
        place_rect(player.x, player.y, player.width, player.height, player.color)
    else:
        place_img(player)

    clock.tick(144)  # fps limit for game
    pygame.display.update()

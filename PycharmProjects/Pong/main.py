from tkinter import *

def menu():
    global root

    root = Tk()

    root.configure(background='black')
    root.title('Pong')
    root.geometry('400x400')
    root.iconbitmap('PongIcon.ico')

    singleplayer_button = Button(root, text='SinglePlayer', width=32, height=3, bd=10, bg='WHITE', command= lambda : game('single'))
    singleplayer_button.pack(pady=20)

    multiplayer_button = Button(root, text='MultiPlayer', width=32, height=3, bd=10, bg='WHITE', command= lambda : game('multi'))
    multiplayer_button.pack(pady=1)

    root.mainloop()


def game(mode):
    root.destroy()

    import pygame, random
    from Entity import Entity
    from pygame import mixer

    pygame.init()
    width = 1024
    height = 512
    screen = pygame.display.set_mode((width, height))  # creates the screen
    clock = pygame.time.Clock()  # creates clock object

    # title and icon
    pygame.display.set_caption('Pong')
    icon = pygame.image.load('PongIcon.ico')
    pygame.display.set_icon(icon)

    # player 1
    paddle1 = Entity(1000,256,0,0,0)

    # player 2
    paddle2 = Entity(24,256,0,0,0)

    # ball
    ball = Entity(paddle1.x,paddle1.y,-4,0,0)

    # game variables
    start = True
    entities = [paddle1, paddle2, ball]
    font = pygame.font.Font('freesansbold.ttf',36)

    # sounds
    paddleSound = mixer.Sound('Paddle.wav')
    wallSound = mixer.Sound('Wall.wav')
    scoreSound = mixer.Sound('PongScore.wav')


    def draw_paddles():
        pygame.draw.rect(screen, 'WHITE', pygame.Rect(paddle1.x, paddle1.y, 4, 36))
        pygame.draw.rect(screen, 'WHITE', pygame.Rect(paddle2.x, paddle2.y, 4, 36))
        pygame.draw.rect(screen, 'WHITE', pygame.Rect(ball.x, ball.y, 4, 4)) # ball
        pygame.draw.rect(screen, 'WHITE', pygame.Rect(511, 0, 2, 512)) # center line


    def gameStart():
        ball.x = paddle1.x - 4
        ball.y = paddle1.y + 18


    def getYChange():
        return float(random.randint(-300,300)/100.0) # gets random decimal


    def isPaddleCollision():
        return (ball.x == paddle1.x and paddle1.y + 39 >= ball.y >= paddle1.y - 4)\
               or (ball.x == paddle2.x and paddle2.y + 39 >= ball.y >= paddle2.y - 4)


    def isBallWallCollision():
        return ball.y <= 0 or ball.y + 4 >= 512


    def displayScore():
        player1Score = font.render(str(paddle1.score), True, (255, 255, 255))
        screen.blit(player1Score, (472, 15))

        player2Score = font.render(str(paddle2.score), True, (255, 255, 255))
        screen.blit(player2Score, (532, 15))


    def isPoint():
        if ball.x <= 0:
            paddle2.score += 1
            ball.xChange = -4
            ball.yChange = 0
            return True
        if ball.x + 4 >= 1024:
            paddle1.score += 1
            ball.xChange = -4
            ball.yChange = 0
            return True
        return False


    def singleplayer():
        if ball.xChange < 0:
            if paddle2.y < ball.y:
                paddle2.yChange = 2
            elif paddle2.y > ball.y:
                paddle2.yChange = -2
            else:
                paddle2.yChange = 0
        else:
            paddle2.yChange = 0

    running = True
    while running:

        screen.fill((0, 0, 0))  # fills screen color with rgb value

        for event in pygame.event.get():  # loops through each even possible in pygame
            if event.type == pygame.QUIT:  # checks if the X button has been pressed
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    paddle1.yChange = -4
                if event.key == pygame.K_DOWN:
                    paddle1.yChange = 4
                if mode == 'multi': # multiplayer
                    if event.key == pygame.K_w:
                        paddle2.yChange = -4
                    if event.key == pygame.K_s:
                        paddle2.yChange = 4

                if event.key == pygame.K_SPACE and start == True:
                    start = False
                    ball.yChange = getYChange()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    paddle1.yChange = 0
                if mode == 'multi': # also multiplayer
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        paddle2.yChange = 0

        if start:
            gameStart() # keeps ball stuck to paddle 1

        # ball and paddle movement
        for i in range(len(entities)):
            entities[i].move()
            if i < 2:
                entities[i].checkEdge()

        # when game is going
        if not start:
            if mode == 'single': # singleplayer
                singleplayer()

            if isPaddleCollision():
                paddleSound.play()
                ball.xChange *= -1 # changes ball x direction
                ball.yChange = getYChange()

            if isBallWallCollision():
                wallSound.play()
                ball.yChange *= -1

            # point scored
            if isPoint():
                scoreSound.play()
                start = True
                paddle2.yChange = 0

        draw_paddles()
        displayScore()


        clock.tick(144) # fps limit for game
        pygame.display.update()

menu()
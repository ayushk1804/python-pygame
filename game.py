import os
import pygame

# Initialize the pygame
pygame.init()

# Set Game Canvas
win = pygame.display.set_mode((500, 480))

# Set Game Title
pygame.display.set_caption("First Game")

# Game Screen Settigs
screenWidth = 500
screenHeight = 480
screenColor = None

# Set Game Clock
clock = pygame.time.Clock()

# os.chdir("./a basic game")
# print(os.getcwd())

# Loading the Sprites
walkRight = [pygame.image.load("data/R1.png"), pygame.image.load('data/R2.png'), pygame.image.load('data/R3.png'), pygame.image.load('data/R4.png'), pygame.image.load(
    'data/R5.png'), pygame.image.load('data/R6.png'), pygame.image.load('data/R7.png'), pygame.image.load('data/R8.png'), pygame.image.load('data/R9.png')]
walkLeft = [pygame.image.load('data/L1.png'), pygame.image.load('data/L2.png'), pygame.image.load('data/L3.png'), pygame.image.load('data/L4.png'), pygame.image.load(
    'data/L5.png'), pygame.image.load('data/L6.png'), pygame.image.load('data/L7.png'), pygame.image.load('data/L8.png'), pygame.image.load('data/L9.png')]
bg = pygame.image.load('data/bg.jpg')
char = pygame.image.load('data/standing.png')


class playerSprite(object):
    def __init__(self, x, y, width, height):
        # Player config
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # Predefined
        # Movements
        self.left = False
        self.right = False
        self.walkCount = 0
        # Jump settings
        self.isJump = False
        self.jumpCount = 10
        # Speed settings
        self.vel = 5
        # Additional
        # Sprite syncing

    # Draw funtion of the Player-Sprite
    def draw(self, canvasWindow):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            canvasWindow.blit(walkLeft[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            canvasWindow.blit(walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        else:
            canvasWindow.blit(char, (self.x, self.y))


# Redraw function - to redraw the Game Window after an update so that the previous window is not sustained
def redrawGameWindow():
    win.blit(bg, (0, 0))
    man.draw(win)

    pygame.display.update()


# Game Loop
man = playerSprite(200, 410, 64, 64)
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():

        # Quit the game if Game window is closed.
        if event.type == pygame.QUIT:
            run = False

        # Key-movements
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False

    elif keys[pygame.K_RIGHT] and man.x < (screenWidth - man.width - man.vel):
        man.x += man.vel
        man.left = False
        man.right = True

    else:
        man.left = False
        man.right = False
        man.walkCount = 0

    if not(man.isJump):
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.left = False
            man.right = False
            man.walkCount = 0

    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * neg // 2
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()

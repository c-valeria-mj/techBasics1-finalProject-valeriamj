import pygame, sys

# GLOBAL VARIABLES
# dimensions for game screen
DISPLAY_HEIGHT = 640
DISPLAY_WIDTH = 960

WALL_THICKNESS = 42

# color palette
BG_COLOR = (37, 19, 26)

# player coordinates
X = DISPLAY_WIDTH / 2
Y = DISPLAY_HEIGHT / 2

# player movement
LEFT_PRESSED = False
RIGHT_PRESSED = False
UP_PRESSED = False
DOWN_PRESSED = False

img_right = pygame.image.load("assets/player_sprites/mc_right_2.png")
img_left = pygame.image.load("assets/player_sprites/mc_left_2.png")
img_up = pygame.image.load("assets/player_sprites/mc_up_2.png")
img_idle = pygame.image.load("assets/player_sprites/mc_down_2.png")

class Player:
    def __init__(self, pos_x, pos_y, speed):
        # init position
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = speed

    def move(self, direction):
        if WALL_THICKNESS < self.pos_x < DISPLAY_WIDTH - WALL_THICKNESS:
            if direction == 'right':
                self.pos_x += self.speed
            if direction == 'left':
                self.pos_x -= self.speed
        elif self.pos_x > DISPLAY_WIDTH - 42:
            self.pos_x -= 10
        elif self.pos_x < 42:
            self.pos_x += 10

        if WALL_THICKNESS < self.pos_y < DISPLAY_HEIGHT - WALL_THICKNESS:
            if direction == 'up':
                self.pos_y -= self.speed
            if direction == 'down':
                self.pos_y += self.speed
        elif self.pos_y > DISPLAY_HEIGHT- 42:
            self.pos_y -= 10
        elif self.pos_y < 42:
            self.pos_y += 10

    def draw(self, img):
        screen.blit(img, (self.pos_x, self.pos_y))

# activate the pygame library
pygame.init()

# create the display
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

# Create one dino object at a start location
player = Player(X, Y, 5)

# Init the clock
clock = pygame.time.Clock()

current_img = img_idle

while True:
    # ticking the clock
    clock.tick(60)

    # update player's position
    if RIGHT_PRESSED:
        current_img = img_right
        player.move('right')
    elif LEFT_PRESSED:
        current_img = img_left
        player.move('left')
    elif UP_PRESSED:
        current_img = img_up
        player.move('up')
    elif DOWN_PRESSED:
        current_img = img_idle
        player.move('down')

    # set background color
    screen.fill(BG_COLOR)
    # Using blit to copy image to screen at a specific location
    player.draw(current_img)
    # refresh the display
    pygame.display.flip()

    for event in pygame.event.get():
        # code you need to end pygame
        if event.type == pygame.QUIT:
            # print("quit")
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                UP_PRESSED = True
            if event.key == pygame.K_a:
                LEFT_PRESSED = True
            if event.key == pygame.K_s:
                DOWN_PRESSED = True
            if event.key == pygame.K_d:
                RIGHT_PRESSED = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                UP_PRESSED = False
            if event.key == pygame.K_a:
                LEFT_PRESSED = False
            if event.key == pygame.K_s:
                DOWN_PRESSED = False
            if event.key == pygame.K_d:
                RIGHT_PRESSED = False

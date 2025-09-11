import pygame

# GLOBAL VARIABLES
# dimensions for game screen
DISPLAY_HEIGHT = 640
DISPLAY_WIDTH = 960
WALL_THICKNESS = 32
SLIME_AREA = (672, 416)

# color palette
BG_COLOR = (37, 19, 26)

# player starting coordinates
X = DISPLAY_WIDTH / 2
Y = WALL_THICKNESS * 2 + 32

# player movement
LEFT_PRESSED = False
RIGHT_PRESSED = False
UP_PRESSED = False
DOWN_PRESSED = False
MOVEMENT_BOX = (896, 544)

# sprite things
SPRITE_SPEED = 0.2

# slimes collected
NUM_OF_SLIMES = 0

# dungeon levels found
LEVEL = 0

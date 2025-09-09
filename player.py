"""
    The PLayer class is built from my assignment from week8 (animation.py) and what I learned in class (week9).
"""

import pygame, sys
import global_var

class Player(pygame.sprite.Sprite): # inherit the properties from pygame's sprite class
    def __init__(self, pos_x, pos_y, speed, sprite_speed):
        # sprites
        super().__init__()  # call constructor for sprite class
        self.sprites = []
        for i in range(1, 12):
            img = pygame.image.load(f"assets/player_sprites/{i}.png")
            self.sprites.append(pygame.transform.scale(img, (64, 64)))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.sprite_speed = sprite_speed

        # init position
        self.pos_x = pos_x
        self.pos_y = pos_y

        # rectangle around sprites
        self.rect = self.image.get_rect()  # this will allow us to move the sprites
        self.rect.center = (pos_x, pos_y)

        # player movement speed
        self.speed = speed

    def update(self, first_spite, last_sprite, sprite_speed):
        current_sprites = []
        for i in range(first_spite, last_sprite):
            current_sprites.append(self.sprites[i])

        self.current_sprite += sprite_speed

        if self.current_sprite >= len(current_sprites):
            self.current_sprite = 0

        self.image = current_sprites[int(self.current_sprite)]

    def move(self, direction):
        if global_var.WALL_THICKNESS < self.rect.x < global_var.DISPLAY_WIDTH - 88:
            if direction == 'right':
                self.rect.x += self.speed
            if direction == 'left':
                self.rect.x -= self.speed
        elif self.rect.x > global_var.DISPLAY_WIDTH - 88:
            self.rect.x -= 10
            # self.speed *= -1
        elif self.rect.x < global_var.WALL_THICKNESS:
            #self.speed *= -1
            self.rect.x += 10

        if global_var.WALL_THICKNESS < self.rect.y < global_var.DISPLAY_HEIGHT - 88:
            if direction == 'up':
                self.rect.y -= self.speed
            if direction == 'down':
                self.rect.y += self.speed
        elif self.rect.y > global_var.DISPLAY_HEIGHT- 88:
            self.rect.y -= 10
        elif self.rect.y < global_var.WALL_THICKNESS:
            self.rect.y += 10

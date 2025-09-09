import pygame, random, sys
import global_var

class Slime(pygame.sprite.Sprite): # inherit the properties from pygame's sprite class
    def __init__(self, pos_x, pos_y):
        super().__init__() #  call constructor for sprite class
        self.sprites = []
        for i in range (1, 6):
            img = pygame.image.load(f"assets/slime_sprites/{i}.png")
            self.sprites.append(pygame.transform.scale(img, (48, 48)))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect() # this will allow us to move the sprites

        self.rect.center = (pos_x, pos_y)

    def update(self, speed):
        self.current_sprite += speed
        # self.rect.centery -= 5

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0


        self.image = self.sprites[int(self.current_sprite)]

        # self.rect.centery -= 5

'''testing things pls work :')'''
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((global_var.DISPLAY_WIDTH, global_var.DISPLAY_HEIGHT))
'''you can delete after class works'''

slime_x = random.randrange(0, global_var.DISPLAY_WIDTH)
slime_y = random.randrange(0, global_var.DISPLAY_HEIGHT)

# creating the sprites for animation
slime_group = pygame.sprite.Group()
new_slime = Slime(global_var.DISPLAY_WIDTH / 2, global_var.DISPLAY_HEIGHT / 2)
slime_group.add(new_slime)

# load background image for dungeon
dungeon_img = pygame.image.load('assets/dungeon.png')
# scale up world map image
dungeon_img = pygame.transform.scale(dungeon_img, (global_var.DISPLAY_WIDTH, global_var.DISPLAY_HEIGHT))

while True:
    '''if cat_x < DISPLAY_WIDTH:
        cat_x += 5
    else:
        cat_x = 0'''

    # set background color
    screen.fill(global_var.BG_COLOR)
    # display
    screen.blit(dungeon_img, (0, 0))  # draws the surface with our background image
    # Using blit to copy image to screen at a specific location
    slime_group.draw(screen)
    slime_group.update(0.15)
    # refresh the display
    pygame.display.flip()

    for event in pygame.event.get():
        # code you need to end pygame
        if event.type == pygame.QUIT:
            # print("quit")
            pygame.quit()
            sys.exit()


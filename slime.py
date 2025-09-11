import pygame, random
import global_var

class Slime(pygame.sprite.Sprite): # inherit the properties from pygame's sprite class
    def __init__(self, pos_x, pos_y):
        super().__init__() #  call constructor for sprite class
        # sprites
        self.sprites = []
        for i in range (1, 7):
            img = pygame.image.load(f"assets/slime_sprites/{i}.png")
            self.sprites.append(pygame.transform.scale(img, (48, 48)))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        # rect around sprites
        self.rect = self.image.get_rect() # this will allow us to move the sprites

        # initial position
        self.rect.center = (pos_x, pos_y)

    def update(self, speed):
        self.current_sprite += speed

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]

    def check_collision(self, player):
        if self.rect.colliderect(player.rect):
            print('player has collected meeeee :o')
            global_var.NUM_OF_SLIMES += 1
            print(global_var.NUM_OF_SLIMES)
            self.kill()

def create_slimes():
    # generate random coordinates for slime
    slime_x = random.randrange(160, global_var.SLIME_AREA[0])
    slime_y = random.randrange(96, global_var.SLIME_AREA[1])

    # creating the sprites for animation
    slime_group = pygame.sprite.Group()
    new_slime = Slime(slime_x, slime_y)
    slime_group.add(new_slime)

    return slime_group

import pygame, random
import global_var


class Dragon(pygame.sprite.Sprite): # inherit the properties from pygame's sprite class
    def __init__(self):
        super().__init__() #  call constructor for sprite class
        self.sprites = []
        for i in range (1, 6):
            img = pygame.image.load(f"assets/dragon_sprites/{i}.png")
            self.sprites.append(pygame.transform.scale(img, (224, 224)))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect() # this will allow us to move the sprites

        self.rect.center = (192, 448)

    def update(self, speed):
        self.current_sprite += speed

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]

    def check_collision(self, player):
        if self.rect.colliderect(player.rect):
            print('fight?')

def create_dragon():
    # creating the sprites for animation
    dragon_group = pygame.sprite.Group()
    new_dragon = Dragon()
    dragon_group.add(new_dragon)

    return dragon_group

import pygame, random
import global_var

class Slime(pygame.sprite.Sprite): # inherit the properties from pygame's sprite class
    """
    Slime makes, displays and animates slime objects on screen and also lets them be collected by the player.
    """
    def __init__(self, pos_x, pos_y):
        """
        Initialize a Slime object
        :param pos_x: X position of the slime
        :param pos_y: Y position of the slime
        """
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
        """
        Cycle through sprites to animate
        :param speed: rate at which sprites change to simulate animation
        """
        self.current_sprite += speed

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]

    def check_collision(self, player):
        """
        Allows slime to be collected (disappear when player touches it)
        :param player: sprite group with whom slime collides
        """
        if self.rect.colliderect(player.rect):
            global_var.NUM_OF_SLIMES += 1
            self.kill()

def create_slimes():
    """
    Makes slime to be displayed
    :return: Group object (collection of sprites) to be displayed
    """
    # generate random coordinates for slime
    slime_x = random.randrange(160, global_var.SLIME_AREA[0])
    slime_y = random.randrange(96, global_var.SLIME_AREA[1])

    # creating the sprites for animation
    slime_group = pygame.sprite.Group()
    new_slime = Slime(slime_x, slime_y)
    slime_group.add(new_slime)

    return slime_group

import pygame

class Dragon(pygame.sprite.Sprite): # inherit the properties from pygame's sprite class
    """
    Displays and animates, dragon. Also, checks for collisions to trigger event.
    """
    def __init__(self, pos_x, pos_y):
        """
        Initialize dragon.
        :param pos_x: X position of the dragon.
        :param pos_y: Y position of the dragon.
        """
        super().__init__() #  call constructor for sprite class
        self.sprites = []
        for i in range (1, 6):
            img = pygame.image.load(f"assets/dragon_sprites/{i}.png")
            self.sprites.append(pygame.transform.scale(img, (224, 224)))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect() # this will allow us to move the sprites

        self.rect.center = (pos_x, pos_y)

    def update(self, speed):
        """
        Cycle through the sprites to animates.
        :param speed: rate at which the sprite changes.
        """
        self.current_sprite += speed

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]

    def check_collision(self, player):
        """
        Check if player came into contact with Dragon.
        :param player: sprite group that could touch Dragon.
        """
        if self.rect.colliderect(player.rect):
            return True
        else:
            return False

def create_dragon(posx, posy):
    """
    Create dragon.
    :param posx: X position of the dragon.
    :param posy: Y position of the dragon.
    """
    # creating the sprites for animation
    dragon_group = pygame.sprite.Group()
    new_dragon = Dragon(posx, posy)
    dragon_group.add(new_dragon)

    return dragon_group

import pygame

class Walk(pygame.sprite.Sprite): # inherit the properties from pygame's sprite class
    """
    Animates our game characters walking to display during endscreen.
    """
    def __init__(self, pos_x, pos_y):
        """
        Initializes object for animation.
        :param pos_x: X position
        :param pos_y: Y position
        """
        super().__init__() #  call constructor for sprite class
        self.sprites = []
        for i in range (1, 3):
            img = pygame.image.load(f"assets/end_screen/{i}.png")
            self.sprites.append(pygame.transform.scale(img, (64*4, 32*4)))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect() # this will allow us to move the sprites

        self.rect.midtop = (pos_x, pos_y)

    def update(self, speed):
        """
        Cycle through sprites to simulate movement.
        :param speed: rate at which the sprite changes.
        """
        self.current_sprite += speed

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]
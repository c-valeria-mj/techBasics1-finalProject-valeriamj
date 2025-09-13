import pygame

class Button: # This class makes buttons and deals with whether they're clicked
    def __init__(self, x, y, source_img, scale):
        """
        Initialize a button.
        :param x: X position for the button.
        :param y: Y position for the button.
        :param source_img: Image source for the button.
        :param scale: Resize the button image to this scale.
        """

        width, height = source_img.get_size()
        self.source_img = pygame.transform.scale(source_img, (int(width * scale) , int(height * scale)))
        self.rect = self.source_img.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw_btn(self, surface): # draws the buttons on the game screen
        """
        Draw the button on the surface and check if clicked.
        :param surface: button is drawn on the surface.
        :return: whether the button was clicked.
        """

        action = False

        # get mouse position
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        # draw button on screen
        surface.blit(self.source_img, (self.rect.x, self.rect.y))

        return action

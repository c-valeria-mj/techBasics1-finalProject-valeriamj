import pygame

# button class
class Button():
    def __init__(self, x, y, source_img, scale):
        width, height = source_img.get_size()
        self.source_img = pygame.transform.scale(source_img, (int(width * scale) , int(height * scale)))
        self.rect = self.source_img.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw_btn(self, surface): # draws the buttons on the game screen
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

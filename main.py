import pygame, sys
import menu

# GLOBAL VARIABLES
# dimensions for game screen
DISPLAY_HEIGHT = 640
DISPLAY_WIDTH = 960

# color palette
bg_color = (37, 19, 26)

pygame.init()

# initialize game screen and give it a title
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Dungeons & Dating')

# load background image for menu
bg_surface = pygame.image.load('assets/menu_bg.png')
# scale up background image
bg_surface = pygame.transform.scale(bg_surface, (DISPLAY_WIDTH, DISPLAY_HEIGHT))

# load button images
play_img = pygame.image.load('assets/buttons/play_btn.png')
how_to_img = pygame.image.load('assets/buttons/how_to_btn.png')
exit_img = pygame.image.load('assets/buttons/exit_btn.png')

# create the button instances
play_btn = menu.Button(400, 176, play_img, 4)
how_to_btn = menu.Button(288, 272, how_to_img, 4)
exit_btn = menu.Button(400, 368, exit_img, 4)

def world_map_menu():
    # load background image for world map
    world_map = pygame.image.load('assets/world_map.png')
    # scale up world map image
    world_map = pygame.transform.scale(world_map, (DISPLAY_WIDTH, DISPLAY_HEIGHT))

    while True:
        screen.fill(bg_color)

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # display
        screen.blit(world_map, (0, 0))  # draws the surface with our background image

        pygame.display.update()

def how_to():
    # load background image for how to screen
    how_to_surface = pygame.image.load('assets/how_to.png')
    # scale up world map image
    how_to_surface = pygame.transform.scale(how_to_surface, (DISPLAY_WIDTH, DISPLAY_HEIGHT))

    while True:
        screen.fill(bg_color)

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()

        # display
        screen.blit(how_to_surface, (0, 0))  # draws the surface with our background image

        pygame.display.update()

def main_menu():
    # game loop
    while True:
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # display
        screen.blit(bg_surface, (0, 0))  # draws the surface with our background image

        # buttons
        if play_btn.draw_btn(screen):
            world_map_menu()
        if how_to_btn.draw_btn(screen):
            how_to()
        if exit_btn.draw_btn(screen):
            pygame.quit()
            sys.exit()

        pygame.display.update()

main_menu()
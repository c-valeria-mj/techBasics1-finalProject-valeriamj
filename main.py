import pygame, sys
import button

pygame.init()

# GLOBAL VARIABLES
# dimensions for game screen
DISPLAY_HEIGHT = 640
DISPLAY_WIDTH = 960

# color palette
BG_COLOR = (37, 19, 26)

# fonts
GAME_FONT = pygame.font.Font('assets/AbaddonBold.ttf', 25)

# initialize game screen and give it a title
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Dungeons & Dating')

def dungeon():
    # load background image for dungeon
    dungeon_img = pygame.image.load('assets/dungeon.png')
    # scale up world map image
    dungeon_img = pygame.transform.scale(dungeon_img, (DISPLAY_WIDTH, DISPLAY_HEIGHT))

    while True:
        screen.fill(BG_COLOR)

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # display
        screen.blit(dungeon_img, (0, 0))  # draws the surface with our background image

        pygame.display.update()

def world_map_menu():
    # load background image for world map
    world_map = pygame.image.load('assets/world_map.png')
    # scale up world map image
    world_map = pygame.transform.scale(world_map, (DISPLAY_WIDTH, DISPLAY_HEIGHT))

    # load button images - main menu
    house_img = pygame.image.load('assets/buttons/house_btn.png')
    shop_img = pygame.image.load('assets/buttons/shop_btn.png')
    dungeon_img = pygame.image.load('assets/buttons/dungeon_btn.png')

    # create the button instances - main menu
    house_btn = button.Button(216, 336, house_img, 4)
    shop_btn = button.Button(352, -32, shop_img, 4)
    dungeon_btn = button.Button(768, 0, dungeon_img, 4)

    while True:
        screen.fill(BG_COLOR)

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # display
        screen.blit(world_map, (0, 0))  # draws the surface with our background image

        # buttons
        if house_btn.draw_btn(screen):
            print('house')
        if shop_btn.draw_btn(screen):
            print('shop')
        if dungeon_btn.draw_btn(screen):
            # print('dungeon')
            dungeon()

        pygame.display.update()

def how_to():
    # load background image for how to screen
    how_to_surface = pygame.image.load('assets/how_to.png')

    while True:
        screen.fill(BG_COLOR)

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN: # return to main menu after pressing ESC
                if event.key == pygame.K_ESCAPE:
                    main_menu()

        # display
        screen.blit(how_to_surface, (0, 0))  # draws the surface with our background image

        pygame.display.update()

def main_menu():
    # load background image for main menu
    bg_surface = pygame.image.load('assets/menu_bg.png')
    # scale up background image
    bg_surface = pygame.transform.scale(bg_surface, (DISPLAY_WIDTH, DISPLAY_HEIGHT))

    # load button images - main menu
    play_img = pygame.image.load('assets/buttons/play_btn.png')
    how_to_img = pygame.image.load('assets/buttons/how_to_btn.png')
    exit_img = pygame.image.load('assets/buttons/exit_btn.png')

    # create the button instances - main menu
    play_btn = button.Button(400, 176, play_img, 4)
    how_to_btn = button.Button(288, 272, how_to_img, 4)
    exit_btn = button.Button(400, 368, exit_img, 4)

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
            break
        if how_to_btn.draw_btn(screen):
            how_to()
        if exit_btn.draw_btn(screen):
            pygame.quit()
            sys.exit()

        pygame.display.update()

def title():
    # load game title image
    title_img = pygame.image.load('assets/title.png')

    # game loop
    while True:
        screen.fill(BG_COLOR)
        screen.blit(title_img, (0, 0))

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main_menu()

        pygame.display.update()

def start_sequence():
    # load images for start sequence
    intro_sequence = []
    for i in range(5):
        intro_sequence.append(pygame.image.load('assets/intro/intro_seq_' + str(i) + '.png'))
        i += 1

    current_scene = 0

    enter_to_cont_img = pygame.image.load('assets/enter_to_cont.png')

    # game loop
    while True:
        screen.fill(BG_COLOR)
        screen.blit(enter_to_cont_img, (0, 0))
        screen.blit(intro_sequence[current_scene], (0, 0))

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if current_scene < (len(intro_sequence) - 1):
                        # screen.fill(BG_COLOR)
                        current_scene += 1
                        screen.blit(intro_sequence[current_scene], (0, 0))
                        pygame.display.flip()
                    elif current_scene == (len(intro_sequence) - 1):
                        title()

        pygame.display.update()

# main_menu()
start_sequence()
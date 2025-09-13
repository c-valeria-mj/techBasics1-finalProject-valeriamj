import pygame
import random
import sys

from modules import global_var, button, player, slime, dragon, walk
from dialogue import dialogue_lines

# activate the pygame library
pygame.init()
pygame.font.init()

# initialize game screen and give it a title
screen = pygame.display.set_mode((global_var.DISPLAY_WIDTH, global_var.DISPLAY_HEIGHT))
pygame.display.set_caption('Dungeons & Dating')

# font
GAME_FONT = pygame.font.Font('assets/AbaddonBold.ttf', 32)

# Init the clock
clock = pygame.time.Clock()

def loading():
    """
    Draw a surface over the entire screen at different opacities to simulate a fading effect when going deeper into the dungeons.
    """
    fade_surface = pygame.Surface((global_var.DISPLAY_WIDTH, global_var.DISPLAY_HEIGHT))
    fade_surface.fill(global_var.BG_COLOR)
    for alpha in range(0, 300):
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(5)


def the_end():
    """
    Nice looking end screen displayed after the player wins the game.
    """
    # load background image for how to screen
    end_surface = pygame.image.load('assets/the_end.png')

    # creating the sprites for animation
    walk_group = pygame.sprite.Group()
    new_frame = walk.Walk(global_var.DISPLAY_WIDTH / 2, 96)
    walk_group.add(new_frame)

    while True:
        screen.fill(global_var.BG_COLOR)

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:  # return to main menu after pressing ESC
                if event.key == pygame.K_RETURN:
                    pygame.quit()
                    sys.exit()

        # display
        screen.blit(end_surface, (0, 0))  # draws the surface with our background image
        walk_group.draw(screen)
        walk_group.update(0.1)

        pygame.display.update()


def game_over():
    """
    If the player chooses to fight the dragon or the wrong dialogue options it's game over :(
    """
    # load background image for how to screen
    game_over_surface = pygame.image.load('assets/game_over.png')

    while True:
        screen.fill(global_var.BG_COLOR)

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:  # return to main menu after pressing ESC
                if event.key == pygame.K_RETURN:
                    pygame.quit()
                    sys.exit()

        # display
        screen.blit(game_over_surface, (0, 0))  # draws the surface with our background image

        pygame.display.update()


def good_ending():
    """
    This is the ony path to the end of the game (different from a game over).
    It can only be reached if the player chooses the correct dialogue options.
    """

    # load background image for endgame sequence
    endgame_img = pygame.image.load('assets/endgame.png')
    # scale up background image
    endgame_img = pygame.transform.scale(endgame_img, (global_var.DISPLAY_WIDTH, global_var.DISPLAY_HEIGHT))

    '''
    Delphine
    '''
    delphine_character = pygame.image.load('assets/delphine_sprites/2.png')
    delphine_character = pygame.transform.scale(delphine_character, (224,224))

    '''
    Dialogue
    '''

    current_scene = 5
    dragon_line = GAME_FONT.render('Dragon: ' + dialogue_lines[current_scene][0], True, 'white')

    player_ans_1 = GAME_FONT.render(dialogue_lines[current_scene][1], True, 'white')
    player_ans_2 = GAME_FONT.render(dialogue_lines[current_scene][2], True, 'white')

    player_ans_1_rect = player_ans_1.get_rect()
    player_ans_1_rect.topleft = (62, 448)
    player_ans_1_clicked = False

    # game loop
    while True:
        # display
        screen.blit(endgame_img, (0, 0))  # draws the surface with our background image

        # delphine
        screen.blit(delphine_character, (global_var.DISPLAY_WIDTH / 2 - 112, global_var.DISPLAY_HEIGHT / 2 - 224))

        # text
        screen.blit(dragon_line, (62, 372))
        screen.blit(player_ans_1, player_ans_1_rect)

        # get mouse position
        mouse_position = pygame.mouse.get_pos()

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if player_ans_1_rect.collidepoint(mouse_position):
            if pygame.mouse.get_pressed()[0] == 1 and player_ans_1_clicked == False:
                if current_scene < len(dialogue_lines) - 1:
                    # current_scene += 1
                    the_end()
                player_ans_1_clicked = True

        pygame.display.update()


def dialogue():
    """
    This function runs the dialogue between the dragon & the player.
    """

    # load background image for endgame sequence
    endgame_img = pygame.image.load('assets/endgame.png')
    # scale up background image
    endgame_img = pygame.transform.scale(endgame_img, (global_var.DISPLAY_WIDTH, global_var.DISPLAY_HEIGHT))

    '''
    Dragon
    '''
    dragon_character = dragon.create_dragon(global_var.DISPLAY_WIDTH / 2, 192)
    '''
    Dialogue
    '''
    current_scene = 0
    dragon_line = GAME_FONT.render('Dragon: ' + dialogue_lines[current_scene][0], True, 'white')

    player_ans_1 = GAME_FONT.render(dialogue_lines[current_scene][1], True, 'white')
    player_ans_2 = GAME_FONT.render(dialogue_lines[current_scene][2], True, 'white')

    player_ans_1_rect = player_ans_1.get_rect()
    player_ans_1_rect.topleft = (62, 448)
    player_ans_1_clicked = False

    player_ans_2_rect = player_ans_2.get_rect()
    player_ans_2_rect.topleft = (62, 512)
    player_ans_2_clicked = False

    # game loop
    while True:

        # display
        screen.blit(endgame_img, (0, 0))  # draws the surface with our background image

        # dragon sprites
        dragon_character.draw(screen)
        dragon_character.update(0.05)

        # text
        screen.blit(dragon_line, (62, 372))
        screen.blit(player_ans_1, player_ans_1_rect)
        screen.blit(player_ans_2, player_ans_2_rect)

        # get mouse position
        mouse_position = pygame.mouse.get_pos()

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if player_ans_1_rect.collidepoint(mouse_position):
            if pygame.mouse.get_pressed()[0] == 1 and player_ans_1_clicked == False:
                if current_scene < len(dialogue_lines) - 1:
                    if current_scene == 4:
                        loading()
                        good_ending()
                        break
                    if current_scene == 7:
                        loading()
                        good_ending()
                        break
                    else:
                        current_scene += 1
                        dragon_line = GAME_FONT.render('Dragon: ' + dialogue_lines[current_scene][0], True, 'white')

                        player_ans_1 = GAME_FONT.render(dialogue_lines[current_scene][1], True, 'white')
                        player_ans_2 = GAME_FONT.render(dialogue_lines[current_scene][2], True, 'white')

                        # pygame.mouse.set_pos((610, 380))

                player_ans_1_clicked = True

            if pygame.mouse.get_pressed()[0] == 0:
                player_ans_1_clicked = False

        elif player_ans_2_rect.collidepoint(mouse_position):
            if pygame.mouse.get_pressed()[0] == 1 and player_ans_2_clicked == False:
                if current_scene < len(dialogue_lines) - 1:
                    # current_scene += 1
                    if current_scene == 0:
                        loading()
                        game_over()

                    if current_scene == 1:
                        current_scene = 6
                        dragon_line = GAME_FONT.render('Dragon: ' + dialogue_lines[current_scene][0], True, 'white')

                        player_ans_1 = GAME_FONT.render(dialogue_lines[current_scene][1], True, 'white')
                        player_ans_2 = GAME_FONT.render(dialogue_lines[current_scene][2], True, 'white')

                        # pygame.mouse.set_pos((610, 380))

                    if current_scene == 5:
                        loading()
                        game_over()

                    if current_scene == 7:
                        loading()
                        game_over()

            if pygame.mouse.get_pressed()[0] == 0:
                player_ans_1_clicked = False

        pygame.display.update()


def endgame():
    """
    This functions runs the endgame, which is when the player decides whether to fight or talk to the dragon or fight it (and loose).
    """
    # load background image for endgame sequence
    endgame_img = pygame.image.load('assets/endgame.png')
    # scale up background image
    endgame_img = pygame.transform.scale(endgame_img, (global_var.DISPLAY_WIDTH, global_var.DISPLAY_HEIGHT))

    '''
    Dragon
    '''
    dragon_character = dragon.create_dragon(global_var.DISPLAY_WIDTH / 2, 192)

    '''
    Buttons
    '''
    # load button images - endgame
    fight_img = pygame.image.load('assets/buttons/fight_btn.png')
    talk_img = pygame.image.load('assets/buttons/talk_btn.png')

    # create the button instances - endgame
    fight_btn = button.Button(224, 416, fight_img, 4)
    talk_btn = button.Button(544, 416, talk_img, 4)

    # game loop
    while True:
        # display
        screen.blit(endgame_img, (0, 0))  # draws the surface with our background image

        # dragon sprites
        dragon_character.draw(screen)
        dragon_character.update(0.05)

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # buttons
        if fight_btn.draw_btn(screen):
            loading()
            game_over()
        if talk_btn.draw_btn(screen):
            dialogue()

        pygame.display.update()


def dragon_dungeon():
    """
    Runs the dungeon containing the dragon from which the player can enter the end game.
    """

    '''
    Dragon
    '''
    dragon_character = dragon.create_dragon(192, 448)

    '''
    Player Character 
    '''
    # creating the Player object
    player_group = pygame.sprite.Group()
    new_player = player.Player(global_var.X, global_var.Y, 5, global_var.SPRITE_SPEED)
    player_group.add(new_player)

    '''
    Background 
    '''
    # load background image for dungeon
    dungeon_img = pygame.image.load('assets/dragon_dungeon.png')
    # scale up world map image
    dungeon_img = pygame.transform.scale(dungeon_img, (global_var.DISPLAY_WIDTH, global_var.DISPLAY_HEIGHT))

    '''
    Game Loop
    '''
    while True:
        # ticking the clock
        clock.tick(60)

        # set background color
        screen.fill(global_var.BG_COLOR)

        # display
        screen.blit(dungeon_img, (0, 0))  # draws the surface with our background image

        # dragon sprites
        dragon_character.draw(screen)
        dragon_character.update(0.05)
        for dragon_sprite in dragon_character:  # this checks if an individual dragon sprite collided with a player sprite
            if dragon_sprite.check_collision(new_player):
                loading()
                endgame()

        # player sprites
        # update player's position
        player.update_player_pos(new_player)
        # using blit to draw player to screen at a specific location
        player_group.draw(screen)

        # refresh the display
        pygame.display.flip()

        # event handler
        for event in pygame.event.get():
            # code you need to end pygame
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    global_var.UP_PRESSED = True
                if event.key == pygame.K_a:
                    global_var.LEFT_PRESSED = True
                if event.key == pygame.K_s:
                    global_var.DOWN_PRESSED = True
                if event.key == pygame.K_d:
                    global_var.RIGHT_PRESSED = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    global_var.UP_PRESSED = False
                if event.key == pygame.K_a:
                    global_var.LEFT_PRESSED = False
                if event.key == pygame.K_s:
                    global_var.DOWN_PRESSED = False
                if event.key == pygame.K_d:
                    global_var.RIGHT_PRESSED = False


def dungeon():
    """
    This function runs the dungeons of the game. It generates the player character sprites and the slime sprites.
    It also tracks WASD input from player to move main character and muse clicks to collect the slimes.
    """

    '''
    Slimes 
    '''
    num_of_slimes = random.randrange(3, 12)
    slimes = []
    for i in range(num_of_slimes):
        slimes.append(slime.create_slimes())

    '''
    Player Character 
    '''
    # creating the sprites for animation
    player_group = pygame.sprite.Group()
    new_player = player.Player(global_var.X, global_var.Y, 5, global_var.SPRITE_SPEED)
    player_group.add(new_player)

    '''
    Background 
    '''
    # load background image for dungeon
    dungeon_img = pygame.image.load('assets/dungeon.png')
    # scale up world map image
    dungeon_img = pygame.transform.scale(dungeon_img, (global_var.DISPLAY_WIDTH, global_var.DISPLAY_HEIGHT))

    '''
    Buttons
    '''
    # load button images - dungeon
    stairs_img = pygame.image.load('assets/buttons/stairs_btn.png')

    # create button instance
    stairs_btn = button.Button(832, 480, stairs_img, 4)
    '''
    Game Loop
    '''
    while True:
        # ticking the clock
        clock.tick(60)

        # update player's position
        player.update_player_pos(new_player)

        # set background color
        screen.fill(global_var.BG_COLOR)

        # display
        screen.blit(dungeon_img, (0, 0))  # draws the surface with our background image

        # Using blit to draw player to screen at a specific location
        player_group.draw(screen)

        # Using blit to draw the slimes to screen at a specific location & cycling through sprites
        for new_slime in slimes:
            new_slime.draw(screen)
            new_slime.update(0.1)
            for slime_sprite in new_slime: # this checks if an individual slime sprite collided with a player sprite
                slime_sprite.check_collision(new_player)


        # refresh the display
        pygame.display.flip()

        # event handler
        for event in pygame.event.get():
            # code you need to end pygame
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    global_var.UP_PRESSED = True
                if event.key == pygame.K_a:
                    global_var.LEFT_PRESSED = True
                if event.key == pygame.K_s:
                    global_var.DOWN_PRESSED = True
                if event.key == pygame.K_d:
                    global_var.RIGHT_PRESSED = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    global_var.UP_PRESSED = False
                if event.key == pygame.K_a:
                    global_var.LEFT_PRESSED = False
                if event.key == pygame.K_s:
                    global_var.DOWN_PRESSED = False
                if event.key == pygame.K_d:
                    global_var.RIGHT_PRESSED = False

        if stairs_btn.draw_btn(screen):
            global_var.LEVEL += 1
            if global_var.LEVEL > 3 and global_var.NUM_OF_SLIMES >= 10:
                loading()
                dragon_dungeon()
            else:
                loading()
                dungeon()


def house_or_shop(button_pressed):
    """
    This displays a message to the player letting them know the shop or house are currently unavailable.
    """
    # load background image for how to screen
    shop_surface = pygame.image.load('assets/shop.png')
    house_surface = pygame.image.load('assets/house.png')

    while True:
        screen.fill(global_var.BG_COLOR)

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:  # return to main menu after pressing ESC
                if event.key == pygame.K_ESCAPE:
                    world_map_menu()

        # display
        if button_pressed == 'shop':
            screen.blit(shop_surface, (0, 0))  # draws the surface with our background image
        if button_pressed == 'house':
            screen.blit(house_surface, (0, 0))

        pygame.display.update()


def world_map_menu():
    """
    This displays the map of the game world and the buttons that allow the player to navigate to different game locations.
    """
    # load background image for world map
    world_map = pygame.image.load('assets/world_map.png')
    # scale up world map image
    world_map = pygame.transform.scale(world_map, (global_var.DISPLAY_WIDTH, global_var.DISPLAY_HEIGHT))

    # load button images - main menu
    house_img = pygame.image.load('assets/buttons/house_btn.png')
    shop_img = pygame.image.load('assets/buttons/shop_btn.png')
    dungeon_img = pygame.image.load('assets/buttons/dungeon_btn.png')

    # create the button instances - main menu
    house_btn = button.Button(216, 336, house_img, 4)
    shop_btn = button.Button(352, -32, shop_img, 4)
    dungeon_btn = button.Button(768, 0, dungeon_img, 4)

    while True:
        screen.fill(global_var.BG_COLOR)

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # display
        screen.blit(world_map, (0, 0))  # draws the surface with our background image

        # buttons
        if house_btn.draw_btn(screen):
            house_or_shop('house')
        if shop_btn.draw_btn(screen):
            house_or_shop('shop')
        if dungeon_btn.draw_btn(screen):
            # print('dungeon')
            dungeon()

        pygame.display.update()


def how_to():
    """
    This displays game instructions to the player until they press ESC to return to the main menu.
    """
    # load background image for how to screen
    how_to_surface = pygame.image.load('assets/how_to.png')

    while True:
        screen.fill(global_var.BG_COLOR)

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
    """
    Displays main menu to the user, where they can choose to play, read some instructions or exit the game completely.
    """
    # load background image for main menu
    bg_surface = pygame.image.load('assets/menu_bg.png')
    # scale up background image
    bg_surface = pygame.transform.scale(bg_surface, (global_var.DISPLAY_WIDTH, global_var.DISPLAY_HEIGHT))

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
    """
    This displays game title to the user. Starts game when they press ENTER (aka goes to main menu).
    """
    # load game title image
    title_img = pygame.image.load('assets/title.png')

    # game loop
    while True:
        screen.fill(global_var.BG_COLOR)
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
    """
    Displays text introducing the player to the story of the game, allowing from time to read until player presses ENTER to continue.
    """
    # load images for start sequence
    intro_sequence = []
    for i in range(5):
        intro_sequence.append(pygame.image.load('assets/intro/intro_seq_' + str(i) + '.png'))
        i += 1

    current_scene = 0

    enter_to_cont_img = pygame.image.load('assets/enter_to_cont.png')

    # game loop
    while True:
        screen.fill(global_var.BG_COLOR)
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
                        loading()
                        current_scene += 1
                        screen.blit(intro_sequence[current_scene], (0, 0))
                        # pygame.display.flip()
                    elif current_scene == (len(intro_sequence) - 1):
                        loading()
                        title()

        pygame.display.update()

'''
    Hi professor! If you don't feel like restarting the whole game to check something, 
    just un-comment the part you want to checkout :D
'''

start_sequence()
# main_menu()
# world_map_menu()
# dungeon()
# dragon_dungeon()
# endgame()
# good_ending()
# the_end()
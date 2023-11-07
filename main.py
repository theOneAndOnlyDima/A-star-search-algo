import sys

import pygame

# pygame setup
pygame.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

# set the window name
pygame.display.set_caption('A-star algorithm')


class Coords:
    start = [0, 0]
    end = [0, 0]


# display window to ask for start and end coords
# TODO: finish this abomination
# TODO: choose better text font and color
def ask_coords_window() -> Coords:
    window_width = 500
    window_height = 230
    input_window = pygame.Rect(width/2-window_width/2, height/2-window_height/2, window_width, window_height)
    pygame.draw.rect(screen, input_window_color, input_window)

    font = pygame.font.Font('freesansbold.ttf', 16)

    # label1
    label1 = font.render('Start coordinates (between (0, 0) and (50, 50)):', True, 'white')
    label1_rect = label1.get_rect()
    label1_rect.center = (width/2-60, height/2-60)
    screen.blit(label1, label1_rect)

    # label2
    label2 = font.render('End coordinates (between (0, 0) and (50, 50)):', True, 'white')
    label2_rect = label2.get_rect()
    label2_rect.center = (width/2-63, height/2-10)
    screen.blit(label2, label2_rect)

    input_width = 100
    input_height = 40

    # input1
    input1 = ''
    input1_is_active = False
    input1_rect = pygame.Rect(width/2+125, height/2-80, input_width, input_height)
    pygame.draw.rect(screen, input_box_color, input1_rect)

    # input2
    input2 = ''
    input2_is_active = False
    input2_rect = pygame.Rect(width/2+125, height/2-30, input_width, input_height)
    pygame.draw.rect(screen, input_box_color, input2_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            if input1_rect.collidepoint(event.pos):
                input1_is_active = True
                input2_is_active = False
            elif input2_rect.collidepoint(event.pos):
                input1_is_active = False
                input2_is_active = True
            else:
                input1_is_active = False
                input2_is_active = False

        if event.type == pygame.KEYDOWN and input1_is_active:
            if event.key == pygame.K_BACKSPACE:
                input1 = input1[:-1]

    pass


# vars
background_color = pygame.Color(4, 8, 15)
button_color = pygame.Color(80, 125, 188)
input_box_color = pygame.Color(187, 209, 234)
input_window_color = pygame.Color(42, 67, 102)
grid_color = pygame.Color(23, 38, 59)
start_end_point_color = pygame.Color(69, 40, 230)
wall_color = pygame.Color(211, 24, 57)
all_paths_color = pygame.Color(24, 190, 182)
shortest_path_color = pygame.Color(13, 179, 17)
# https://coolors.co/04080f-17263b-213551-2a4366-507dbc-a1c6ea-bbd1ea


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((95, 95, 95))

    ask_coords_window()

    pygame.display.flip()

pygame.quit()

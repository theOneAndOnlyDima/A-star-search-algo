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


input_state = [False] * 4
input_content = [''] * 4


def draw_text(font: pygame.font.Font, text: str, color: str, pos_x: int, pos_y: int):
    label = font.render(text, True, color)
    label_rect = label.get_rect()
    label_rect.center = (pos_x, pos_y)
    screen.blit(label, label_rect)


def draw_input_box(pos_x: int, pos_y: int) -> pygame.Rect:
    input_width = 50
    input_height = 40
    input_rect = pygame.Rect(pos_x, pos_y, input_width, input_height)
    pygame.draw.rect(screen, input_box_color, input_rect)
    return input_rect


def set_text(e: pygame.event.Event, index: int) -> None:
    text = input_content[index]
    if e.key == pygame.K_BACKSPACE:
        text = text[:-1]
    else:
        text += e.unicode
    input_content[index] = text


# display window to ask for start and end coords
# TODO: change input box color when active
# TODO: restrict input text length
# TODO: check if input is in the desired range and only numeric
# TODO: finish this abomination
# TODO: add text All coords must be between 0 and 50
# TODO: study the algorithm
def ask_coords_window() -> Coords:
    window_width = 400
    window_height = 230
    input_window = pygame.Rect(width/2-window_width/2, height/2-window_height/2, window_width, window_height)
    pygame.draw.rect(screen, input_window_color, input_window)

    font = pygame.font.Font('freesansbold.ttf', 16)

    # label1
    draw_text(font, 'Start coordinates:', 'white', width//2-110, height//2-60)

    # x1
    draw_text(font, 'x:', 'white', width//2, height//2-60)

    # y1
    draw_text(font, 'y:', 'white', width//2+105, height//2-60)

    # label2
    draw_text(font, 'End coordinates:', 'white', width//2-113, height//2-10)

    # x2
    draw_text(font, 'x:', 'white', width//2, height//2-10)

    # y2
    draw_text(font, 'y:', 'white', width//2+105, height//2-10)

    # input x1
    input_x1 = draw_input_box(width//2+20, height//2-80)

    # input y1
    input_y1 = draw_input_box(width//2+125, height//2-80)

    # input x2
    input_x2 = draw_input_box(width//2+20, height//2-30)

    # input y2
    input_y2 = draw_input_box(width//2+125, height//2-30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_x1.collidepoint(event.pos):
                input_state[0] = True
                input_state[1] = False
                input_state[2] = False
                input_state[3] = False
            elif input_y1.collidepoint(event.pos):
                input_state[0] = False
                input_state[1] = True
                input_state[2] = False
                input_state[3] = False
            elif input_x2.collidepoint(event.pos):
                input_state[0] = False
                input_state[1] = False
                input_state[2] = True
                input_state[3] = False
            elif input_y2.collidepoint(event.pos):
                input_state[0] = False
                input_state[1] = False
                input_state[2] = False
                input_state[3] = True
            else:
                input_state[0] = False
                input_state[1] = False
                input_state[2] = False
                input_state[3] = False
        if event.type == pygame.KEYDOWN:
            if input_state[0]:
                set_text(event, 0)
            if input_state[1]:
                set_text(event, 1)
            if input_state[2]:
                set_text(event, 2)
            if input_state[3]:
                set_text(event, 3)

    draw_text(font, input_content[0], 'black', width // 2 + 45, height // 2 - 60)
    draw_text(font, input_content[1], 'black', width // 2 + 150, height // 2 - 60)
    draw_text(font, input_content[2], 'black', width // 2 + 45, height // 2 - 10)
    draw_text(font, input_content[3], 'black', width // 2 + 150, height // 2 - 10)

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

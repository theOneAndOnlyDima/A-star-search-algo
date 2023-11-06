import pygame

# pygame setup
pygame.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True


class Coords:
    start = [0, 0]
    end = [0, 0]


# display window to ask for start and end coords
# TODO: fix the dimensions
def ask_coords_window() -> Coords:
    input_window = pygame.Rect(width/2-150, height/2-100, 350, 200)
    pygame.draw.rect(screen, input_window_color, input_window)
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

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

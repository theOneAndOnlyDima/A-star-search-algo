import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

start_point = ''
end_point = ''

# create input rectangle
start_input_rect = pygame.Rect(200, 200, 140, 32)

# vars
color = pygame.Color(80, 125, 188)
background_color = pygame.Color(4, 8, 15)
button_color = pygame.Color(42, 67, 102)
input_box_color = pygame.Color(187, 209, 234)
input_window_color = pygame.Color()
grid_color = pygame.Color(23, 38, 59)
start_end_point_color = pygame.Color()
wall_color = pygame.Color()
all_paths_color = pygame.Color()
shortest_path_color = pygame.Color()
# https://coolors.co/04080f-17263b-213551-2a4366-507dbc-a1c6ea-bbd1ea


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((95, 95, 95))

    pygame.draw.rect(screen, color, start_input_rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

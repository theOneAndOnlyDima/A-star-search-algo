import sys
import pygame
import tkinter as tk
from tkinter import *

# pygame setup
width = 900
height = 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('A-star algorithm')

# vars
background_color = pygame.Color(4, 8, 15)
button_color = pygame.Color(80, 125, 188)
hovered_button_color = pygame.Color(29, 118, 242)
input_box_color = pygame.Color(146, 181, 222)
input_box_selected_color = pygame.Color(204, 220, 240)
input_window_color = pygame.Color(42, 67, 102)
grid_color = pygame.Color(23, 38, 59)
start_end_point_color = pygame.Color(69, 40, 230)
wall_color = pygame.Color(211, 24, 57)
all_paths_color = pygame.Color(24, 190, 182)
shortest_path_color = pygame.Color(13, 179, 17)
# https://coolors.co/04080f-17263b-213551-2a4366-507dbc-a1c6ea-bbd1ea

class Cell:
    def __init__(self, x, y) -> None:
        self.i = x
        self.j = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.neighbors = []
        self.previous = None
        self.wall = False
    
    def show(self, color, stroke=0):
        x = self.i * w
        y = self.j * h
        pygame.draw.rect(screen, color, (x, y, w, h), stroke)
        pygame.display.update()


cols = 50
rows = 50
grid = [[Cell(i, j) for j in range(cols)] for i in range(rows)]
w = width // cols
h = height // rows


# show grid
for i in range(rows):
    for j in range(cols):
        grid[i][j].show(grid_color, 1)

# draw border
for i in range(0, rows):
    grid[0][i].show(input_window_color)
    grid[0][i].wall = True
    grid[rows-1][i].show(input_window_color)
    grid[rows-1][i].wall = True
    grid[i][0].show(input_window_color)
    grid[i][0].wall = True
    grid[i][cols-1].show(input_window_color)


def verify_coords(start, end) -> bool:
    if len(start) != 2 or len(end) != 2:
        return False
    if not start[0].isdigit() or not start[1].isdigit() or not end[0].isdigit() or not end[1].isdigit():
        return False
    if int(start[0]) < 1 or int(start[0]) > 48 or int(start[1]) < 1 or \
        int(start[1]) > 48 or int(end[0]) < 1 or int(end[0]) > 48 or int(end[1]) < 1 or int(end[1]) > 48:
        return False
    return True


def on_submit():
    global start
    global end
    s = entry_start.get().split(",")
    e = entry_end.get().split(",")
    if verify_coords(s, e) and s != e:
        start = grid[int(s[0])][int(s[1])]
        end = grid[int(e[0])][int(e[1])]
        window.quit()
        window.destroy()
    elif s != e:
        label_error.config(text="Only digits between 1 and 48 are allowed!",
                           foreground="red")
    else:
        label_error.config(text="Start and end coordinates must be different!",
                           foreground="red")


window = Tk()
window.title("Coordinates")

window_width = window.winfo_screenwidth()
window_height = window.winfo_screenheight()

window.geometry(f"270x95+{window_width//2-135}+{window_height//2-40}")
label_start = Label(window, text="Start coordinates (x,y):")
label_end = Label(window, text="End coordinates (x,y):")
label_error = Label(window, text = "")

label_start.grid(row=0, column=0)
label_end.grid(row=1, column=0)
label_error.grid(row = 3, columnspan=2)

entry_start = Entry(window)
entry_end = Entry(window)

entry_start.grid(row=0, column=1)
entry_end.grid(row=1, column=1)

submit = Button(window, text="Submit", command=on_submit)

submit.grid(row=2, columnspan=2)

window.update()
mainloop()

pygame.init()

start.show(start_end_point_color)
end.show(start_end_point_color)

valid = True
while valid:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            valid = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                x = pos[0] // w
                y = pos[1] // h
                if grid[x][y] != start and grid[x][y] != end and not grid[x][y].wall:
                    grid[x][y].wall = True
                    grid[x][y].show(wall_color)
        if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            x = pos[0] // w
            y = pos[1] // h
            if grid[x][y] != start and grid[x][y] != end and not grid[x][y].wall:
                grid[x][y].wall = True
                grid[x][y].show(wall_color)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                valid = False

def main():
    start.show(start_end_point_color)
    end.show(start_end_point_color)

while True:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
    main()

"""Pacman 2018
Martin Janecek & Terezie Hrubanova"""
import pygame, random, sys
from pygame.locals import *


FPS = 10
WINDOWWIDTH = 960
WINDOWHEIGHT = 720
CELLSIZE = 30
assert WINDOWWIDTH % CELLSIZE == 0, 'Window width must be a multiple of cell size.'
assert WINDOWHEIGHT % CELLSIZE == 0, 'Window height must be a multiple of cell size.'
NUM_CELLS_X = WINDOWWIDTH // CELLSIZE
NUM_CELLS_Y = WINDOWHEIGHT // CELLSIZE

BGCOLOR = (0,0,0)
YELLOW = (255,255,0)
PAPAYA = (255,239,213)

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Pacman')

    welcome_screen()
    pygame.display.update()

    while True:
        was_key_pressed()



def welcome_screen():
    title_font = pygame.font.Font('freesansbold.ttf', 100)
    title_surface = title_font.render('PACMAN', True, YELLOW)
    title_rect = title_surface.get_rect()
    title_rect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)

    msg_font = pygame.font.Font('freesansbold.ttf', 25)
    msg = msg_font.render('Press any key to start', True, PAPAYA)
    msg_rect = msg.get_rect()
    msg_rect.center = (WINDOWWIDTH / 1.4, WINDOWHEIGHT / 1.1)



    DISPLAYSURF.fill(BGCOLOR)
    DISPLAYSURF.blit(title_surface, title_rect)
    DISPLAYSURF.blit(msg, msg_rect)

def terminate():
    pygame.quit()
    sys.exit

def was_key_pressed():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    key_up_events = pygame.event.get(KEYUP)
    if len(key_up_events) == 0:
        return
    if key_up_events[0].key == K_ESCAPE:
        terminate()
    if len(key_up_events)>0:
        run_game()

    return True

def create_grid():
    grid = []
    for i in range(NUM_CELLS_X):
        y_list = []
        for j in range(NUM_CELLS_Y):
            y_list.append(0)
        grid.append(y_list)

    return grid

def draw_screen():
    grid = create_grid()
    obstacle_position = [[15,15],[16,15],[17,15],[18,15],[19,15],[20,15],[21,15],[22,15]]
    for n in range(NUM_CELLS_Y):
        grid[0][n] = 1
        grid[31][n] = 1


    for m in range(NUM_CELLS_X):
        grid[m][0] = 1
        grid[m][23] = 1
    for k in obstacle_position:
        grid[k[0]][k[1]] = 1


    DISPLAYSURF.fill(BGCOLOR)
    for i in range(NUM_CELLS_X):
        for j in range(NUM_CELLS_Y):
            if (grid[i][j]==1):
                pygame.draw.rect(DISPLAYSURF, YELLOW, (i*CELLSIZE,j*CELLSIZE, CELLSIZE, CELLSIZE))
    pygame.display.update()


def run_game():
    draw_screen()




if __name__ == '__main__':
    main()

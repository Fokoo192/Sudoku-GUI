import pygame as pg
from rules import *
#initializing the module, creating the screen and making a font variable 
# to use for numbers that will be later rendered onto the screen
pg.init()
screen = pg.display.set_mode((450,450))
running = True
BG_COLOR = pg.Color("white")
LINE_COLOR = pg.Color("black")

pg.display.set_caption("SUDOKU")
screen.fill(BG_COLOR)
running = True
key = None

def draw():
    for i in range(9): # 9 because the grid is 9x9
        if i == 3 or i == 6: # making the 3rd and 6th line thicker by 5
            pg.draw.line(screen,LINE_COLOR,(i*50,0),(i*50,450),5)
            pg.draw.line(screen,LINE_COLOR,(0,i*50),(450,i*50),5)
        else:
            pg.draw.line(screen,LINE_COLOR,(i*50,0),(i*50,450))
            pg.draw.line(screen,LINE_COLOR,(0,i*50),(450,i*50))
draw()
#event loop
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    pg.display.update()
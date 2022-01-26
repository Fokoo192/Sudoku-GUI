import pygame as pg
from rules import *
#initializing the module, creating the screen and making a font variable 
# to use for numbers that will be later rendered onto the screen
pg.init()
screen = pg.display.set_mode((450,450))
font = pg.font.SysFont("comicsans",40)

#random sudoku board
sample_board = [
        [0,6,0,0,3,0,0,0,1],
        [0,0,1,7,4,5,0,6,3],
        [7,3,0,0,9,0,8,0,0],
        [5,1,3,9,0,0,0,2,0],
        [0,0,0,0,5,7,0,1,8],
        [8,7,0,6,0,3,0,0,0],
        [9,0,6,0,0,0,0,5,0],
        [1,0,0,4,2,9,0,0,7],
        [0,0,0,5,0,1,2,8,0]
] 

#colors 
BG_COLOR = pg.Color("white")
LINE_COLOR = pg.Color("black")
SQUARE_COLOR = pg.Color("red")
TEXT_COLOR = pg.Color("black")

# drawing the grid
def draw():
    for i in range(9): # 9 because the grid is 9x9
        if i == 3 or i == 6: # making the 3rd and 6th line thicker by 5
            pg.draw.line(screen,LINE_COLOR,(i*50,0),(i*50,450),5)
            pg.draw.line(screen,LINE_COLOR,(0,i*50),(450,i*50),5)
        else:
            pg.draw.line(screen,LINE_COLOR,(i*50,0),(i*50,450))
            pg.draw.line(screen,LINE_COLOR,(0,i*50),(450,i*50))
# puts the number on the board
def rendering_num():
    PADDING_X = 18
    PADDING_Y = 12
    for row in range(len(sample_board)):
        for col in range(len(sample_board[0])):
            number = sample_board[row][col]
            if number == 0:
                number = ""
            text = font.render(str(number),True,TEXT_COLOR)
            screen.blit(text,(col*50+PADDING_X,row*50+PADDING_Y))

# drawing the small red square
def draw_square(TL_coordinate=[0,0],length=50,thickness=4):
    TL_coord = TL_coordinate
    TR_coord = [TL_coordinate[0]+length,TL_coordinate[1]]
    BL_coord = [TL_coordinate[0],TL_coordinate[1]+length]
    BR_coord = [TL_coordinate[0]+length,TL_coordinate[1]+length] 
    pg.draw.line(screen, SQUARE_COLOR,TL_coord,TR_coord,thickness)
    pg.draw.line(screen, SQUARE_COLOR,TR_coord,BR_coord,thickness)
    pg.draw.line(screen, SQUARE_COLOR,BR_coord,BL_coord,thickness)
    pg.draw.line(screen, SQUARE_COLOR,BL_coord,TL_coord,thickness)
#making the initial changes to the screen
pg.display.set_caption("SUDOKU")
screen.fill(BG_COLOR)
draw()
rendering_num()
running = True
key = None
#event loop
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            screen.fill(BG_COLOR) # to remove the pervious red square
            draw()
            rendering_num()
            x = int(event.pos[0] // 50)
            y = int(event.pos[1] // 50)
            draw_square([x*50,y*50],50,4)
        if event.type == pg.TEXTINPUT:
            key = event.text
            num = font.render(str(key),True,TEXT_COLOR)
            screen.blit(num,(x*50+18,y*50+12))
            if key.isnumeric():
                if Is_valid(sample_board,int(key),y,x):
                    sample_board[y][x] = int(key)
    pg.display.update()

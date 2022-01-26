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
# checks if the value is already in the row
def check_row(board,value,row):
    for w in board[row]:
        if w == value:
            return False
    return True
#print(check_row(sample_board,6,1))
# checks if the value is already in the column
def check_col(board,value,col):
    r = 0
    while r < 9:
        if value == board[r][col]:
            return False
        r += 1
    return True
#print(check_col(sample_board,6,1))
#returns the index of the square the value entered is located in
def square_index(row,col):
    a = 0
    b = 0 
    if row in [3,4,5]:
        a = 3
    if row in [6,7,8]:
        a = 6
    if col in [3,4,5]:
        b = 1
    if col in [6.7,8]:
        b = 2 
    return a+b 
# checks if the number is already in the square
def check_square(board,value,row,col):
    a = 0
    b = 0
    index = square_index(row,col)
    if index in [3,4,5]:
        a = 3
    if index in [6,7,8]:
        a = 6
    if index in [1,4,7]:
        b = 3
    if index in [2,5,8]:
        b = 6
    for x in range(a,a+3):
        for y in range(b,b+3):
            if value == board[x][y]:
                return False
    return True
#print(check_square(sample_board,6,1,1))
#makes sure you don't change the numbers that are already on the board
def check_blankspace(board,row,col):
    return board[row][col] == 0
# checks if the value entered is valid
def Is_valid(board,value,row,col):
    return check_row(board,value,row) and check_col(board,value,col) and check_square(board,value,row,col) and check_blankspace(board,row,col)
#print(Is_valid(sample_board,6,1,1))  

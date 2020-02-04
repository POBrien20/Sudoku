#Sudoku


import random



#Prints basic sudoku board
def print_board(board):
    print("---------------------")
    for row in board:
        print(row)
    print("---------------------")
        
#returns list of elements in that row
def get_row(row, board):
    return board[row]

#returns list of elements in that column
def get_col(col, board):
    retval = []
    for row in range(len(board)):
        retval.append(board[row][col])
    return retval

#returns list of elements in that box
def get_box(row, col, board):
    retval = []
    boxrow = row // 3
    boxcol = col // 3
    for i in range(boxrow*3, boxrow*3 + 3):
        for j in range(boxcol*3, boxcol*3 + 3):
            retval.append(board[i][j])
##    print("SADF")
##    print(retval)
##    print("ASDFASFADS")
    return retval

def nextNum(num):
    if num == 8:
        return 0
    else:
        return num + 1

        
def create_board():
    rows, cols = (9, 9) 
    arr = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(15):
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        while arr[x][y] != 0:
            x = random.randint(0, 8)
            y = random.randint(0, 8)
        val = random.randint(1, 9)
        while isValid(x, y, val, arr) == False:
            val = random.randint(1, 9)
        arr[x][y] = val
    print_board(arr)
    return arr
            
    

def isValid(row, col, num, board):
##    print(num)
##    print_board(board)
    if num in get_row(row, board):
        return False
    if num in get_col(col, board):
        return False
    if num in get_box(row, col, board):
        return False
    else:
        return True

#################################

def find_zero(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                return (row, col)

def solve(board):
    currentSpace = find_zero(board)
    print(currentSpace)
    if currentSpace:
        row, col = currentSpace
    else:
        print("sdf")
        return True #Done - base case, no more empty spaces, solved

    for i in range(1,10):
        if isValid(row, col, i, board):
            board[row][col] = i
            print_board(board)
            if solve(board) == True:
                return True
            board[row][col] = 0
    return False

def inputBoard():
    rows, cols = (9, 9) 
    arr = [[int(input("Enter value for {}, {}:".format(i+1, j+1))) for i in range(cols)] for j in range(rows)]
    return arr
    

arr = create_board()
##arr = inputBoard()
copy = arr
solve(arr)
print_board(copy)

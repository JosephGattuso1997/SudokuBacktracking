#Backtracking sudoku solver

import numpy as np
import sys
sys.setrecursionlimit(250)
# Get the file specified and read it in as a txt

matrixList = []
filename = 'puzzle1-Gavant'
file = open('puzzles/' + filename + '.txt').read()

# Loop over the lines of the txt replacing the X with 0 for usability
# Append to list to create array for matrix

for item in file:
    if item == 'X':
        matrixList.append(item.replace('X','0'))
    if item.isnumeric():
        matrixList.append(item)
    else:
        pass

# Take the list and create a 9x9 matrix

board = np.array(list(matrixList),dtype=float).reshape((9,9))

boardLength = 9

def solve(board):
    
# Call getEmpty to get the position of the empty spot to try numbers 1-9

    empty = getEmpty(board)
    
    if not empty:
        return True
    
    else:
        row, col = empty

    for number in range(1,10):

# Call the check funtion and if correct make that loccation the current number
# Recursive call of check to go to the next empty box if True
# If false backtrack by making the location 0 again and go back to previous box
        
        if check(board, number, (row, col)):
            board[row][col] = number

            if solve(board):
                return True

            board[row][col] = 0
            
    return False

def check(board, num, pos):

# Check row for repeat of number
    
    for element in range(boardLength):
        
# loop through every element in the board row.
# get first element from position go get row number
# if repeat in for retun false
        
        if board[pos[0]][element] == num:

            return False

    for element in range(boardLength):
        
# loop through every element in the board column.
# get second element from position go get column number
# if repeat in for retun false
      
        if board[element][pos[1]] == num:

            return False

# Check the 3x3 square to check for repeating numbers

    start_x = pos[0] - pos[0] % 3
    start_y = pos[1] - pos[1] % 3
    
    for i in range(3):
        for j in range(3):
            if board[i + start_x][j + start_y] == num:
                return False

    return True

# look through the matrix index to find zeros and return their x,y location

def getEmpty(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return row, col

    return None


#save matrix board as txt file in solutions folder

def saveBoard(board, filename):
    with open('solutions/' + filename + ".sln.txt", "w") as text_file:
        np.savetxt(text_file, board, fmt='%i')

# Call the functions and save results

if __name__ == '__main__':
    try:
        solve(board)
        saveBoard(board, filename)
    except Exception as e:
        print("This puzzle was unable to be solved because", e)

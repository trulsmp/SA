__author__ = 'trulsmp & larsland'
import math
import random
import numpy as np

m = int(input("M value: "))
n = int(input("N value: "))
k = int(input("K value: "))

validBoards = []
    

def validate_board(board):
    return True

def calculate_score(board):
    score = 0
    for i in range(0,m):
        for j in range(0,n):
            if board[i][j] == '1':
                score += 1
    return score


def print_board(board):
    string = ''
    for i in range(0,m):
        string += '\n'
        for j in range(0,n):
            string += (board[i][j]) +""
    return string


def initiate_board():
    board = []
    for i in range(0,m):
        board.append([])
        for j in range(0,n):
            board[i].append('0')
    return board

def generate_start(board):
    eggs = 10
    while True:
        randomRow = random.randint(0, m - 1)
        randomCol = random.randint(0, n - 1)
        if board[randomRow][randomCol] == '0':
            board[randomRow][randomCol] = '1'
            eggs -= 1
        if eggs == 0:
            break
    return board

def objective(board):
    if validate_board(board):
        print ("calculating score")
        return calculate_score(board)
    else:
        return 0;


def evaluate_neighbours():
    pass

def generate_neighbours():
    pass


def checkRow(board):
	count = 0
	for i in board:
		if (i == '1'):
			count += 1
			if (count > 2):
				return False
		elif (i == '\n'):
			count = 0
	return True

	
def checkCol(board):
    count = 0
    for i in range(n):
        count = 0
        for x in range(m):
            if (board[x][i] == '1'):
                    count += 1
        #print count
        if count > k:
            return False
    return True
    
def checkDiagonal(board):
    # create a numpy array
    a = np.array(board)
    # Then a list comprehension is used to collect all the diagonals
    diags = [a[::-1,:].diagonal(i) for i in range(-a.shape[0]+1,a.shape[1])]

    # Now back to the original array to get the upper-left-to-lower-right diagonals,
    # starting from the right, so the range needed for shape (x,y) was y-1 to -x+1 descending.
    diags.extend(a.diagonal(i) for i in range(a.shape[1]-1,-a.shape[0],-1))

    # Another list comp to convert back to Python lists from numpy arrays
    diagonals = [n.tolist() for n in diags]
    eggs = 0
    for i in diagonals:
        for y in i:
            if y == '1':
                eggs += 1
        if eggs > k:
            print ("Total number of eggs in diagonal is above K value")
            return False
        eggs = 0

    return True
    
    
def validateBoard(board, stringBoard):
    if (checkRow(stringBoard) and checkCol(board) and checkDiagonal(board)):
        return True
    else:
        return False

    
def SA():
    temperature = 10000  # ???
    firstCorrect = []
    x = True
    while x:
        board = initiate_board()
        board = generate_start(board)
        stringBoard = (print_board(board))
        if (validateBoard(board, stringBoard)):
            firstCorrect = board
            x = False
    print(print_board(firstCorrect))
  
    F = objective(board)  # Objective function
    print (F)
    
    '''' while True:
    
        neighbours = generate_neighbours()
        p_max = evaluate_neighbours()
    
    
        q = (objective(p_max) - (objective(board)/objective(board)))
    
        p = min(1, math.e**(-q/temperature))
    
        x = math.random();
    
        if x > p:
            board = p_max
        else:
            board = 0 #random choice
    
        temperature = temperature - 1 '''''


SA()

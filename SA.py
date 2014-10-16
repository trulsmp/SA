__author__ = 'trulsmp & larsland'
import math
import random
import numpy as np

m = n = int(input("M and N value: "))
k = int(input("K value: "))
max_eggs = m*k


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
            string += (board[i][j]) + " "
    print(string)


def initiate_board():
    board = []
    for i in range(0,m):
        board.append([])
        for j in range(0,n):
            board[i].append('0')
    return board

def generate_start(board):
    eggs = max_eggs
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
    if validateBoard(board):
        return calculate_score(board)
    else:
        return 0;


def evaluate_neighbours(neighbours):
    highest_neighbour = neighbours[0]
    for i in neighbours:
        if objective(i) > objective(highest_neighbour):
            highest_neighbour = i
    return highest_neighbour

def generate_neighbours(board):
    array = []
    array.append(board)
    for i in range(0,20):
        new_board = initiate_board()
        new_board = generate_start(new_board)
        array.append(new_board)
    return array


def checkRow(board):
    count = 0
    for i in range(n):
        count = 0
        for x in range(m):
            if (board[i][x] == '1'):
                    count += 1
        #print count
        if count > k:
            return False
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
            return False
        eggs = 0

    return True
    
    
def validateBoard(board):
    if checkRow(board) and checkCol(board) and checkDiagonal(board):
        return True
    else:
        return False

    
def SA():
    temperature = 100000  # ???

    board = initiate_board()
    board = generate_start(board)



    F = objective(board)  # Objective function
    
    while temperature > 0:
    
        neighbours = generate_neighbours(board)
        p_max = evaluate_neighbours(neighbours)
        if objective(p_max) > objective(board):
            board = p_max
        if objective(board) == max_eggs:
            return board
        ''' q = (objective(p_max) - (objective(board)/objective(board)))
    
        p = min(1, math.e**(-q/temperature))
    
        x = random.randint(0,1)
        if x > p:
            board = p_max
        else:
            board = 0 #random choice '''''
    
        temperature -= 1

    return board

final_board = SA()
print_board(final_board)
print (validateBoard(final_board))


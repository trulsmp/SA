__author__ = 'trulsmp & larsland'
import math
import random
import numpy as np
from random import randint, shuffle, randrange

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
    while eggs > 0:
        for i in range(n):
            x = randint(0,n-1)
            board[i][x] = '1'
            eggs -= 1
            putted = 1
            while putted < k:
                y = randint(0,n-1)
                if board[i][x] != board[i][y]:
                    board[i][y] = '1'
                    eggs -= 1
                    putted += 1
    return board



    return board

def objective(board):
    if validateBoard(board):
        return calculate_score(board)
    else:
        return 1;


def evaluate_neighbours(neighbours):
    highest_neighbour = neighbours[0]
    for i in neighbours:
        if objective(i) > objective(highest_neighbour):
            highest_neighbour = i
    return highest_neighbour

def generate_neighbours(board):

    # Function that generates a set of neighbours (different boards) based on the current board state.
    # Returns a list of n neighbours. The neighbours are only generated if there are columns or rows with
    # egg > k.

    to_check = []
    cols = []
    # Finds all columns
    for i in range (len(board)):
        temp = []
        for j in range(len(board)):
            temp.append(board[j][i])
        cols.append(temp)
    # All columns with number_of_eggs > k, appended to a list
    to_check = [row for row in cols if row.count('1') > k ]
    # Finding all rows that has an egg in a column > k eggs, and adds it to rows.
    rows = []
    for row in to_check:
        for x in range(len(row)):
            if row[x] == '1' and board[x] not in rows:
                rows.append(board[x])

    neighbours = []
    for x in range(len(board)):
        if board[x] in rows:
            boardcopy = list(board)
            row = board[x]
            row = list(row)
            shuffle(row)
            board[x] = row
            neighbours.append(board)
            board = boardcopy

    #If there is no neighbours, there is a conflict in the diagonals. We have no support for this, so shuffeling the first row

    if len(neighbours) == 0:
        neighbour = list(board)
        row = board[0]
        row = list(row)
        shuffle(row)
        neighbour[0] = row
        return [neighbour]
    return neighbours


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
    temperature = 8000  # ???

    board = initiate_board()
    board = generate_start(board)
    print_board(board)
    max_board = board



    F = objective(board)  # Objective function
    
    while temperature > 0:
    
        neighbours = generate_neighbours(board)
        p_max = evaluate_neighbours(neighbours)
        if objective(max_board) < objective(p_max):
            max_board = p_max
        if objective(board) == max_eggs:
            return board
        q = (objective(p_max) - (objective(board)/objective(board)))
    
        p = min(1, math.e**(-q/temperature))
    
        x = random.randint(0,1)
        if x > p:
            board = p_max
        else:
            board = random.choice(neighbours)
    
        temperature -= 0.04
    return max_board

final_board = SA()
print_board(final_board)
print (validateBoard(final_board))


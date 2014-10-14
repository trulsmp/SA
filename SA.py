__author__ = 'trulsmp'
import math
import random

#m = int(input("How many rows? "))
#n = int(input("How many cols? "))
#k = int(input("How many eggs? "))
m = n = 5
k = 2



def validate_board(self):
    return True

def calculate_score(self):
    score = 0
    for i in range(0,m):
        for j in range(0,n):
            if [i][j] == 1:
                score += 1








def print_board(self):
    for i in range(0,m):
        for j in range(0,n):
            print(self.board_array[i][j])
        print("\n")




def SA():

    m = int(input("M value: "))
    n = int(input("N value: "))
    k = int(input("K value: "))


    temperature = 3000  # ???
    board = initiate_board(m, n)
    print (generate_start(board))


    F = objective(board)  # Objective function

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

def initiate_board(m, n):
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
    print(board)

def objective(board):
    if board.validate_board():
        return board.calculate_score()
    else:
        return 0;


def objective(P):
    return 0


def evaluate_neighbours():
    pass

def generate_neighbours():
    pass




SA()

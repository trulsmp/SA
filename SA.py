__author__ = 'trulsmp'
import math

#m = int(input("How many rows? "))
#n = int(input("How many cols? "))
#k = int(input("How many eggs? "))
m = n = 5
k = 2

class Board:
    BoardArray = [[]]
    def __init__(self, m, n, k):
        self.rows = m
        self.cols = n
        self.eggs = k

    def validate_board(self):
        pass

    def calculate_score(self):
        pass

    def initiate_board(self):
        board = []
        for i in range(0,m):
            board.append([])
            for j in range(0,n):
                board[i].append('X')
        return board



def SA():
    target = 10  # ?????
    temperature = 20  # ???
    board = Board(m, n, k)
    board.initiate_board()
    start = board[0][0]

    F = objective(board)  # Objective function
    while True:
        if F > target:
            return Board;

        neighbours = generate_neighbours()
        p_max = evaluate_neighbours()


        q = (objective(p_max) - (objective(board)/objective(board)))

        p = min(1, math.e**(-q/temperature))

        x = math.random();

        if x > p:
            board = p_max
        else:
            board = 0 #random choice

        temperature = temperature - 1



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






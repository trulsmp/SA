__author__ = 'trulsmp'
import math


class Board():
    BoardArray = [[]]
    def __init__(self):
        pass


    def validate_board(self):
        pass

    def calculate_score(self):
        pass

    def initiate_board(self):
        pass
    def getHeight(self):
        return







def SA():
    target = 10  # ?????
    temperature = 20  # ???
    board = Board()
    board.initiate_board()
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



def evaluate_neighbours():
    pass


def generate_neighbours():
    pass






__author__ = 'trulsmp'
import math

#m = int(input("How many rows? "))
#n = int(input("How many cols? "))
#k = int(input("How many eggs? "))
m = n = 5
k = 2

class Board:
    board_array = []
    def __init__(self, m, n, k):
        self.rows = m
        self.cols = n
        self.eggs = k
        board_array = self.initiate_board()

    def validate_board(self):
        return True

    def calculate_score(self):
        score = 0
        for i in range(0,m):
            for j in range(0,n):
                if [i][j] == 1:
                    score += 1


    def initiate_board(self):
        board = []
        for i in range(0,m):
            board.append([])
            for j in range(0,n):
                self.board_array[i].append(0)
        return board

    def generate_start(self):

        pass

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
    board = Board(m, n, k)
    board.generateStart()

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

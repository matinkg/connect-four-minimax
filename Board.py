from config import *

class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(7)] for _ in range(6)]

    # print the board
    def printBoard(self):

        for row in self.board:
            print ('|' + '|'.join(row) + '|')
        
        # print horizontal line
        print('---------------')

        # print column numbers
        print(' 1 2 3 4 5 6 7')

    def dropPiece(self, column, player):
        for row in range(5, -1, -1):
            if self.board[row][column] == EMPTY:
                self.board[row][column] = player
                break

    def checkWin(self):
        board = self.board

        # check horizontal
        for row in range(6):
            for col in range(4):
                if board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] != EMPTY:
                    return board[row][col]

        # check vertical
        for row in range(3):
            for col in range(7):
                if board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] != EMPTY:
                    return board[row][col]
                    
        # check diagonal
        for row in range(3):
            for col in range(4):
                if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3] != EMPTY:
                    return board[row][col]

        for row in range(3):
            for col in range(3, 7):
                if board[row][col] == board[row + 1][col - 1] == board[row + 2][col - 2] == board[row + 3][col - 3] != EMPTY:
                    return board[row][col]

        return None

    # a function to evaluate the window
    # a window is a list of 4 cells in the board (row, column, diagonal)
    @staticmethod
    def evaluate_window(window, player):
        score = 0
        opponent = PLAYER1 if player == PLAYER2 else PLAYER2

        if window.count(player) == 4:
            score += 100
        elif window.count(player) == 3 and window.count(EMPTY) == 1:
            score += 5
        elif window.count(player) == 2 and window.count(EMPTY) == 2:
            score += 2

        if window.count(opponent) == 3 and window.count(EMPTY) == 1:
            score -= 4

        return score

    # a function to evaluate user score based on the board state
    # it is a simple heuristic function to evaluate the score of the board
    # used by the AI to make a move (minimax algorithm)
    def evalScore(self, player):
        score = 0
        
        # the center column is the best column to play in because it gives the player more options
        # so we give it a little higher score
        center_column = []
        for row in range(6):
            center_column.append(self.board[row][3])
        center_count = center_column.count(player)
        score += center_count * 3

        # horizontal
        for row in range(6):
            row_array = self.board[row]
            for col in range(4):
                window = row_array[col:col + 4]
                score += self.evaluate_window(window, player)

        # vertical
        for col in range(7):
            col_array = []
            for row in range(6):
                col_array.append(self.board[row][col])
                
            for row in range(3):
                window = col_array[row:row + 4]
                score += self.evaluate_window(window, player)

        # diagonal
        for row in range(3):
            for col in range(4):
                window = [self.board[row + i][col + i] for i in range(4)]
                score += self.evaluate_window(window, player)
        
        for row in range(3):
            for col in range(4):
                window = [self.board[row + 3 - i][col + i] for i in range(4)]
                score += self.evaluate_window(window, player)
        
        return score
    
    # a function to get all the possible moves
    def getValidMoves(self):
        valid_moves = []
        for col in range(7):
            if self.board[0][col] == EMPTY:
                valid_moves.append(col)
        return valid_moves
    
    # a function to check if the board is full
    def isBoardFull(self):
        for row in range(6):
            for col in range(7):
                if self.board[row][col] == EMPTY:
                    return False
        return True
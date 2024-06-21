import random

EMPTY = ' '
PLAYER1 = 'X'
PLAYER2 = 'O'


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

class ConnectFour:
    def __init__(self):
        self.board = Board()
        self.gameOver = False
        self.turn = PLAYER1
        self.winner = None

    def makeMove(self):
        print(f"Player {self.turn}'s turn")
        column = input("Enter column number: ")

        # check if column is not integer or out of range
        if not column.isdigit() or int(column) < 1 or int(column) > 7:
            print("Invalid input. Please enter a number between 1 and 7...")
            return self.makeMove()
        column = int(column)

        self.board.dropPiece(column - 1, self.turn)

    def switchTurn(self):
        self.turn = PLAYER1 if self.turn == PLAYER2 else PLAYER2

    @staticmethod
    def checkWin(board):
        board = board.board
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
        

    def playGame(self):
        # random turn
        self.turn = PLAYER1 if random.randint(0, 1) == 0 else PLAYER2
        print(f"Player {self.turn} goes first")

        self.board.printBoard()
        
        while not self.gameOver:
            self.makeMove()
            self.board.printBoard()
            
            if self.checkWin(self.board):
                self.gameOver = True
                self.winner = self.turn
                print(f"Player {self.winner} wins!")
                break
            
            self.switchTurn()

if __name__ == '__main__':
    game = ConnectFour()
    game.playGame()

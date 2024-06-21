# ConnectFour Game

EMPTY = ' '
PLAYER1 = 0
PLAYER2 = 1
PLAYER1_PIECE = 'X'
PLAYER2_PIECE = 'O'


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
                self.board[row][column] = PLAYER1_PIECE if player == PLAYER1 else PLAYER2_PIECE
                break

class ConnectFour:
    def __init__(self):
        self.board = Board()
        self.gameOver = False
        self.turn = PLAYER1

    def makeMove(self):
        print(f"Player {self.turn}'s turn")
        column = int(input("Enter column number: ")) - 1
        self.board.dropPiece(column, self.turn)

    def switchTurn(self):
        self.turn = PLAYER1 if self.turn == PLAYER2 else PLAYER2

    @staticmethod
    def checkWin(board):
        return False
        

    def playGame(self):
        while not self.gameOver:
            self.board.printBoard()
            self.makeMove()
            ConnectFour.checkWin(self.board.board)
            self.switchTurn()

if __name__ == '__main__':
    game = ConnectFour()
    game.playGame()

from config import *
from Board import Board
import random
import copy

class ConnectFour:
    def __init__(self):
        self.board = Board()
        self.gameOver = False
        self.turn = PLAYER1
        self.winner = None
        self.opponent_type = None
        self.depth = None

    def getBoard(self):
        return self.board

    def makeMove(self):
        print(f"\nPlayer {self.turn}'s turn")
        column = input("Enter column number: ")

        # check if column is not integer or out of range
        if not column.isdigit() or int(column) < 1 or int(column) > 7:
            print("Invalid input. Please enter a number between 1 and 7...")
            return self.makeMove()
        column = int(column)

        self.board.dropPiece(column - 1, self.turn)

        print ("\n--------------------------------------\n")

    def makeAIMove(self):
        print(f"\nPlayer {self.turn}'s turn. AI is thinking...")
        column, minimax_score = self.minimax(self.board, self.depth, True)
        print(f"Player {self.turn} chooses column {column + 1}")
        self.board.dropPiece(column, self.turn)

        print ("\n--------------------------------------\n")

    def switchTurn(self):
        self.turn = PLAYER1 if self.turn == PLAYER2 else PLAYER2

    def minimax(self, board, depth, maximizingPlayer):
        valid_moves = board.getValidMoves()
        is_terminal = board.isBoardFull() or board.checkWin()
        if depth == 0 or is_terminal:
            if is_terminal:
                if board.checkWin() == PLAYER2:
                    return (None, 100000000000000 + depth)
                elif board.checkWin() == PLAYER1:
                    return (None, -100000000000000 - depth)
                else:
                    return (None, 0)
            else:
                return (None, board.evalScore(PLAYER2))
        
        if maximizingPlayer:
            value = -100000000000000
            column = random.choice(valid_moves)
            for col in valid_moves:
                board_copy = copy.deepcopy(board)
                board_copy.dropPiece(col, PLAYER2)
                new_score = self.minimax(board_copy, depth - 1, False)[1]
                if new_score > value:
                    value = new_score
                    column = col
            return (column, value)
        else:
            value = 100000000000000
            column = random.choice(valid_moves)
            for col in valid_moves:
                board_copy = copy.deepcopy(board)
                board_copy.dropPiece(col, PLAYER1)
                new_score = self.minimax(board_copy, depth - 1, True)[1]
                if new_score < value:
                    value = new_score
                    column = col
            return (column, value)

    def playGame(self):
        print ("Welcome to Connect Four!")
        # choose between playing against AI or another player
        while self.opponent_type is None:
            print ("Do you want to play against AI or another player?")
            print ("1. AI")
            print ("2. Player")
            
            opponent = input("\nEnter your choice (1 or 2): ")
            print ()

            if opponent.isdigit() and int(opponent) == 1:
                self.opponent_type = "ai"

                print("Choose the difficulty level:")
                print("1. Easy")
                print("2. Medium")
                print("3. Hard")
                print("4. Expert")
                print("5. Impossible")
                print("6. Extremely Impossible")
                print("7. Inhuman")
                print("8. Godlike")


                while self.depth is None:
                    level = input("\nEnter the difficulty level (1-8): ")
                    if level.isdigit() and 1 <= int(level) <= 8:
                        self.depth = int(level)
                    else:
                        print("Invalid input. Please enter a number between 1 and 6...")
                        
            elif opponent.isdigit() and int(opponent) == 2:
                self.opponent_type = "player"
            else:
                print("Invalid input. Please enter 1 or 2...")


        # random turn
        self.turn = PLAYER1 if random.randint(0, 1) == 0 else PLAYER2

        print ("\n---- Let's start the game! ----\n")
            
        self.board.printBoard()

        while not self.gameOver:
            # if ai turn
            if self.opponent_type == "ai" and self.turn == PLAYER2:
                self.makeAIMove()
            else:
                self.makeMove()
                
            self.board.printBoard()
            
            if self.board.checkWin():
                self.gameOver = True
                self.winner = self.turn
                print(f"\n\n**** Player {self.winner} wins! ****\n\n")
                break

            if self.board.isBoardFull():
                self.gameOver = True
                print("\n\n**** It's a tie! ****\n\n")
                break
            
            self.switchTurn()
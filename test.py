from ConnectFour import ConnectFour

game = ConnectFour()

# set up the board for testing
game.getBoard().board =[
    [' ', ' ', ' ', 'X', 'X', ' ', ' '],
    [' ', ' ', ' ', 'O', 'O', ' ', ' '],
    [' ', ' ', ' ', 'O', 'X', ' ', ' '],
    ['X', 'O', ' ', 'O', 'O', ' ', ' '],
    ['O', 'O', 'X', 'X', 'X', ' ', ' '],
    ['O', 'X', 'X', 'O', 'X', ' ', ' ']
]

print (game.minimax(game.getBoard(), 5, True))
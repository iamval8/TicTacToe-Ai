# TicTacToe with minimax algorithm
import random

# Global Variables
board = []
player = "X"

# Functions
def print_board():
    print("\n")
    print("\t0\t\t1\t\t2")  # Column Labels -- Index of columns
    count = 0  # Row counter
    for item in board:
        row = ""  # Displays row labels
        for space in item:
            row += "\t" + space + "\t"  # Add each space in the row
        print(count, row + "\n")  # Prints the completed row
        count += 1  # Increments the row counter

# Returns true if a row, col on the board is open
def is_valid_move(row, col):
    # Check that the move is within the board
    if row >= len(board) or col >= len(board[row]):
        return False
    # Check if the position is available (no other player)
    return board[row][col] == "-"

# Places player on row, col on the board
def place_player(player, row, col):
    board[row][col] = player

# Asks the user to enter a row and col until the user enters a valid location
# Adds user location to the board, and prints the board
def take_turn(player):
    print(player, "'s Turn")  # "X's Turn OR O's Turn"
    if player == "X":
        row = int(input("Enter a row: "))
        col = int(input("Enter a col: "))
        while not is_valid_move(row, col):
            print("Please enter a valid move")
            row = int(input("Enter a row: "))
            col = int(input("Enter a col: "))
        place_player(player, row, col)
    else:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        while not is_valid_move(row, col):
            row = random.randint(0, 2)
            col = random.randint(0, 2)
        place_player(player, row, col)
    print_board()

# Write your check win functions here:
def check_row_win(player):
    for i in range(3):
        # Check for horizontal wins
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    return False

def check_col_win(player):
    for i in range(3):
        # Check for vertical wins
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    return False

def check_diag_win(player):
    # Check diagonal wins
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True
    return False

def check_win(player):
    return check_col_win(player) or check_row_win(player) or check_diag_win(player)

def check_tie():
    if "-" in board[0] or "-" in board[1] or "-" in board[2]:
        return False
    return not check_win("X") and not check_win("O")

def check_results():
    if check_win("X"):
        print("X Wins!")
    elif check_win("O"):
        print("O Wins!")
    else:
        print("It's a tie!")

# Minimax algorithm -- Ai Opponent
def minimax(player):
    # Initializes variables to store optimal move starting with invalid values
    # These values later get updated with valid values
    optimalRow = -1
    optimalCol = -1
    # If player X has won the game, returns a -10 score since it's bad for O
    # None is for no row and no column
    if check_win("X"):
        return (-10, None, None)
    # If player O has won the game, returns a 10 score since it's good for O
    # None is for no row and no column
    elif check_win("O"):
        return (10, None, None)
    # If the game is tied, return a score of 0 (neutral) -- no row or column
    elif check_tie():
        return (0, None, None)
    # If it's player X's turn -- worst is a large positive number (minimizing player)
    if player == "X":
        worst = 1000
        # Traverse through every cell in our matrix to check for an empty space
        for row in range(3):
            for col in range(3):
                if board[row][col] == "-":
                    # Simulate placing player X in the current empty cell
                    place_player("X", row, col)
                    # Call the minimax function recursively for player "O" (the opponent), getting the value of the move
                    moveVal = minimax("O")[0]
                    # If this move results in a smaller value than the current 'worst', update 'worst', 'optimalRow', and 'optimalCol'
                    if moveVal < worst:
                        worst = moveVal
                        optimalRow = row
                        optimalCol = col
                    # Undo the move (backtrack) to explore other possibilities
                    place_player("-", row, col)
        # After evaluating all possible moves, return the worst score (since "X" is minimizing) and the best move
        return (worst, optimalRow, optimalCol)
    else:
        # If it's player "O"'s turn, initialize 'best' as a large negative number (maximizing player)
        best = -1000
        for row in range(3):
            for col in range(3):
                if board[row][col] == "-":
                    place_player("O", row, col)
                    # Call the minimax function recursively for player "X" (the opponent), getting the value of the move
                    moveVal = minimax("X")[0]
                    # If this move results in a larger value than the current 'best', update 'best', 'optimalRow', and 'optimalCol'
                    if moveVal > best:
                        best = moveVal
                        optimalRow = row
                        optimalCol = col
                    place_player("-", row, col)
        # After evaluating all possible moves, return the best score (since "O" is maximizing) and the best move
        return (best, optimalRow, optimalCol)

# Start of program
for i in range(3):
    board.append(["-", "-", "-"])  # Initializing the board

print("\t\tWelcome to Tic Tac Toe!")
print_board()

# Main Game Loop
while not check_win("X") and not check_win("O") and not check_tie():
    take_turn(player)
    if player == "X":
        player = "O"
    else:
        player = "X"

check_results()



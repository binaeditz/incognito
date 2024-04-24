def display_board(board):
    """Prints the current state of the board."""
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def player_input():
    """Asks the player to choose their marker (X or O)."""
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1, choose X or O: ").upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    """Places the player's marker on the board."""
    board[position] = marker

def win_check(board, mark):
    """Checks if the given mark has won the game."""
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the left side
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal

def choose_first():
    """Randomly chooses which player goes first."""
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    """Checks if the given position on the board is empty."""
    return board[position] == ' '

def full_board_check(board):
    """Checks if the board is full."""
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    """Asks the player for their move."""
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input("Choose your next position (1-9): "))
    return position

def replay():
    """Asks the players if they want to play again."""
    return input("Do you want to play again? Enter Yes or No: ").lower().startswith('y')

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    game_on = True

    while game_on:
        if turn == 'Player 1':
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)

            if win_check(board, player1_marker):
                display_board(board)
                print('Congratulations! Player 1 has won the game!')
                game_


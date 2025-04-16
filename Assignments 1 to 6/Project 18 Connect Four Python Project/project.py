ROWS = 6
COLS = 7

# Initialize empty board
def create_board():
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

# Print board
def print_board(board):
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
    print('  ' + '   '.join(str(i) for i in range(COLS)))

# Drop piece in the board
def drop_piece(board, col, piece):
    for row in reversed(board):
        if row[col] == ' ':
            row[col] = piece
            return True
    return False  # Column full

# Check win
def check_winner(board, piece):
    # Horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c+i] == piece for i in range(4)):
                return True
    # Vertical
    for r in range(ROWS - 3):
        for c in range(COLS):
            if all(board[r+i][c] == piece for i in range(4)):
                return True
    # Diagonal (positive slope)
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True
    # Diagonal (negative slope)
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r-i][c+i] == piece for i in range(4)):
                return True
    return False

# Check draw
def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)

# Main game loop
def play_game():
    board = create_board()
    turn = 0
    print_board(board)

    while True:
        piece = 'X' if turn % 2 == 0 else 'O'
        try:
            col = int(input(f"Player {1 if piece == 'X' else 2} ({piece}) - Choose column (0-{COLS - 1}): "))
        except ValueError:
            print("Invalid input! Try again.")
            continue

        if col < 0 or col >= COLS:
            print("Column out of bounds. Try again.")
            continue

        if not drop_piece(board, col, piece):
            print("Column full. Try another.")
            continue

        print_board(board)

        if check_winner(board, piece):
            print(f"🎉 Player {1 if piece == 'X' else 2} ({piece}) wins!")
            break

        if is_draw(board):
            print("😮 It's a draw!")
            break

        turn += 1

play_game()

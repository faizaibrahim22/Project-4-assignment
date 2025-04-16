import random

# Board size and number of bombs
SIZE = 5
BOMBS = 5

class Minesweeper:
    def __init__(self, size, bombs):
        self.size = size
        self.bombs = bombs
        self.board = self.make_new_board()
        self.assign_values_to_board()
        self.dug = set()

    def make_new_board(self):
        board = [[None for _ in range(self.size)] for _ in range(self.size)]
        bombs_planted = 0

        while bombs_planted < self.bombs:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)

            if board[row][col] == '*':
                continue

            board[row][col] = '*'
            bombs_planted += 1

        return board

    def assign_values_to_board(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        num_bombs = 0
        for r in range(max(0, row - 1), min(self.size, row + 2)):
            for c in range(max(0, col - 1), min(self.size, col + 2)):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_bombs += 1
        return num_bombs

    def dig(self, row, col):
        self.dug.add((row, col))

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        for r in range(max(0, row - 1), min(self.size, row + 2)):
            for c in range(max(0, col - 1), min(self.size, col + 2)):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)
        return True

    def show_board(self):
        for r in range(self.size):
            row = ''
            for c in range(self.size):
                if (r, c) in self.dug:
                    row += f'{self.board[r][c]} '
                else:
                    row += '_ '
            print(row)

def play():
    game = Minesweeper(SIZE, BOMBS)

    while len(game.dug) < (SIZE * SIZE - BOMBS):
        game.show_board()
        try:
            user_input = input("Enter row and column (e.g. 1 3): ").split()
            row, col = int(user_input[0]), int(user_input[1])
        except:
            print("Invalid input. Try again.")
            continue

        if row < 0 or row >= SIZE or col < 0 or col >= SIZE:
            print("Invalid location. Try again.")
            continue

        safe = game.dig(row, col)
        if not safe:
            print("Game Over! You hit a bomb 💣")
            game.dug = [(r, c) for r in range(SIZE) for c in range(SIZE)]
            game.show_board()
            return

    print("Congratulations! You won 🎉")
    game.show_board()

play()

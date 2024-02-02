class GameBoard:
    def __init__(self):
        self.size = 3
        self.board = [[' ' for _ in range(self.size)] for _ in range(self.size)]

    def display_board(self):
        print("\nGame Board:")
        print("-" * (self.size * 4))
        for row in self.board:
            print(" | ".join(row))
            print("-" * (self.size * 4))

    def is_space_free(self, row, col):
        # Check if the specified cell is free.
        return self.board[row][col] == ' '

    def make_move(self, row, col, player_symbol):
        try:
            if self.is_space_free(row, col):
                self.board[row][col] = player_symbol
                return True
            else:
                print("This cell is already occupied!")
                return False
        except IndexError:
            print("Invalid move. Please choose a row and column within the board range.")
            return False

    def check_win(self, player_symbol):
        # Check horizontal, vertical, and diagonal wins
        for i in range(self.size):
            if all(self.board[i][j] == player_symbol for j in range(self.size)):
                return True
            if all(self.board[j][i] == player_symbol for j in range(self.size)):
                return True

        if all(self.board[i][i] == player_symbol for i in range(self.size)):
            return True
        if all(self.board[i][self.size - 1 - i] == player_symbol for i in range(self.size)):
            return True

        return False

    def is_board_full(self):
        return all(self.board[row][col] != ' ' for row in range(self.size) for col in range(self.size))

class Player:
    def __init__(self, symbol, game_board):
        self.symbol = symbol
        self.game_board = game_board

    def make_move(self):
        valid_move = False
        while not valid_move:
            try:
                row = int(input("Enter the row (1-3): ")) - 1
                col = int(input("Enter the column (1-3): ")) - 1
                if 0 <= row < self.game_board.size and 0 <= col < self.game_board.size:
                    valid_move = self.game_board.make_move(row, col, self.symbol)
                    if not valid_move:
                        print("This space is already occupied or move is out of bounds, try again.")
                else:
                    print("Invalid input. Please enter numbers between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

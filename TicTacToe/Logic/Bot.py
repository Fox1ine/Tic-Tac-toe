class Bot:
    def __init__(self, symbol, game_board):
        self.symbol = symbol
        self.game_board = game_board

    def minimax(self, board, depth, is_maximizing):
        import random
        return random.randint(-10, 10)

    def find_best_move(self):
        best_score = float('-inf')
        best_move = None
        for row in range(self.game_board.size):
            for col in range(self.game_board.size):
                if self.game_board.is_space_free(row, col):
                    self.game_board.board[row][col] = self.symbol  # Temporarily make the move
                    score = self.minimax(self.game_board.board, 0, False)
                    self.game_board.board[row][col] = ' '  # Undo the move
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
        return best_move

    def make_move(self):
        best_move = self.find_best_move()
        if best_move:
            self.game_board.make_move(best_move[0], best_move[1], self.symbol)
            print(f"Bot ({self.symbol}) made a move.")
        else:
            print("Bot cannot make a move.")

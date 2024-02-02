from Logic.GameBoard import GameBoard
from Logic.Player import Player
from Logic.Bot import Bot


def main():
    game_board = GameBoard()
    player = Player('X', game_board)
    bot = Bot('O', game_board)

    current_turn = "Player"

    while True:
        if current_turn == "Player":
            print("\nPlayer's turn.")
            player.make_move()
            if game_board.check_win(player.symbol):
                print("Player wins!")
                break
        else:
            print("\nBot's turn.")
            bot.make_move()
            if game_board.check_win(bot.symbol):
                print("Bot wins!")
                break

        game_board.display_board()

        if game_board.is_board_full():
            print("The game is a tie!")
            break

        # Switch turn
        current_turn = "Bot" if current_turn == "Player" else "Player"

    game_board.display_board()  # Show final state of the game board


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

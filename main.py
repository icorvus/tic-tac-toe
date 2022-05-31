from board import Board
from game import Game

def main():
    print("""Welcome to Command Line Tic-Tac-Toe!
You already know the rules right?\n""")
    print(Game.instructions())
    board1 = Board()
    print(board1)
    board1.state[2], board1.state[4], board1.state[6] = "x", "x", "x"
    print(board1)
    print(board1.is_game_over('x'))
    print(board1.is_move_legal(21))

if __name__ == "__main__":
    main()
import os
from board import Board
from game import Game
from player import Player

def main():
    os.system("cls||clear")
    print("""Welcome to Command Line Tic-Tac-Toe!
You already know the rules right?\n""")
    print(Game.instructions())

    board = Board()
    player_name = input("What's the name of the first player: ")
    player1 = Player(player_name, "x")
    player_name = input("What's the name of the second player: ")
    player2 = Player(player_name, "o")

    game = Game(player1, player2, board)
    game.play()

if __name__ == "__main__":
    main()
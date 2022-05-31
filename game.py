import os
from board import Board
from player import Player

class Game:
    def __init__(self, player1: Player, player2: Player, board: Board):
        self.player1 = player1
        self.player2 = player2
        self.board = board

    def play(self):
        is_winner_selected = False
        player = self.player1
        round = 0
        winner = None
        os.system("cls||clear")
        #print(self.board)
        while not is_winner_selected and round < 9:
            round += 1
            if round % 2 == 0:
                player = self.player2
            else:
                player = self.player1
            os.system("cls||clear")
            print(f"Round {round}!\n")
            print(self.board)
            print(f"{player.name} now it's your turn")

            move = input("What is your play?: ")
            while not self.board.update(move, player.sign):
                os.system("cls||clear")
                print("That is not a valid move!")
                print(self.instructions())
                print(self.board)
                move = input("What is your play?: ")
            if self.board.is_game_over(player.sign):
                is_winner_selected = True
                winner = player.name
        os.system("cls||clear")
        print("The game is over!\n")
        print(self.board)
        if winner:
            print(f"The winner is {winner}")
        else:
            print("It's a tie!")
        
            
            

    @staticmethod
    def instructions():
        return """Choose the place you want to place your X or O
by typing the number from 1 to 9,
corresponding to the place on the grid shown below:
 1 | 2 | 3
———————————
 4 | 5 | 6
———————————
 7 | 8 | 9
        """
    
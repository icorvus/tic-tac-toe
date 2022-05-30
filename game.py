class Game:
    def __init__(self, player1, player2, board):
        self.player1 = player1
        self.player2 = player2
        self.board = board

    def play(self):
        pass

    @staticmethod
    def instructions():
        return """You choose the place you want to place your X or O
by typing the number from 1 to 9,
corresponding to the place on the grid shown below:
 1 | 2 | 3
———————————
 4 | 5 | 6
———————————
 7 | 8 | 9
        """
    
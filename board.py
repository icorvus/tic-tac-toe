class Board:
    WINNING_COMBOS = [[0,1,2], [3,4,5], [6,7,8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    def __init__(self):
        self.state = ['_' for x in range(9)]
    
    def __str__(self):
        return """
 {} | {} | {}
———————————
 {} | {} | {}
———————————
 {} | {} | {}
        """.format(*self.state)

    def is_game_over(self, sign):
        for combo in self.WINNING_COMBOS:
            if self.state[combo[0]] == self.state[combo[1]] == self.state[combo[2]] == sign:
                return True
        return False



    def is_move_legal(self, move):
        if move in range(1, 10) and self.state[move - 1] == '_':
            return True
        return False
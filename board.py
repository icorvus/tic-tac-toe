class Board:
    WINNING_COMBOS = [[0,1,2], [3,4,5], [6,7,8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    def __init__(self, state=None):
        if state:
            self.__state = state
        else:
            self.__state = ['_' for x in range(9)]
        
    
    def __str__(self):
        return """
 {} | {} | {}
———————————
 {} | {} | {}
———————————
 {} | {} | {}
        """.format(*self.__state)

    def __repr__(self):
        return f"Board({self.__state})"

    def update(self, move: int, sign):
        if not self.is_move_legal(move):
            return False
        self.__state[move - 1] = sign
        return True

    def is_game_over(self, sign):
        for combo in self.WINNING_COMBOS:
            if self.__state[combo[0]] == self.__state[combo[1]] == self.__state[combo[2]] == sign:
                return True
        return False

    def is_move_legal(self, move: int):
        if move in range(1, 10) and self.__state[move - 1] == '_':
            return True
        return False
class Player:
    def __init__(self, name: str, sign: str):
        assert len(name) < 30, f"The player name: {name} is too long!(>30 characters)"
        assert sign in ["X", "O", "x", "o"], f"The sign is not an \"X\" or not an \"O\""

        self.name = name
        self.sign = sign.lower()

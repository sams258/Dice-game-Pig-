class Intelligence:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def choose_action(self, score, opponent_score):
        if self.difficulty == "easy":
            return "roll" if score < 20 else "hold"
        elif self.difficulty == "medium":
            return "roll" if score < 25 or score < opponent_score else "hold"
        elif self.difficulty == "hard":
            return "roll" if score < 30 or score < opponent_score else "hold"

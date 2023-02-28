class Game:
    def __init__(self, player1, player2, high_scores):
        self.player1 = player1
        self.player2 = player2
        self.high_scores = high_scores

    def play(self):
        print("Welcome to Pig!")
        print(f"{self.player1.name} vs. {self.player2.name}")
        while True:
            if self.player1.play(self.player2.score, self.high_scores):
                break
            if self.player2.play(self.player1.score, self.high_scores):
                break

        print("High Scores:")
        for name, score in self.high_scores.get_high_scores():
            print(f"{name}: {score}")

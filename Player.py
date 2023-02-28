from Dicehand import Dicehand
from Histogram import Histogram


class Player:
    def __init__(self, name, intelligence=None):
        self.name = name
        self.score = 0
        self.intelligence = intelligence

    def __str__(self):
        return f"{self.name} ({self.score})"

    def play(self, opponent_score, high_scores):
        print(f"{self.name}'s turn")
        print(f"{self.name} score: {self.score}")
        print(f"Opponent score: {opponent_score}")
        dice_hand = Dicehand()
        turn_score = 0
        while True:
            action = None
            if self.intelligence:
                action = self.intelligence.choose_action(self.score, opponent_score)
            else:
                while action not in ["roll", "hold"]:
                    action = input("Roll or hold? ").lower()
            if action == "roll":
                dice = dice_hand.roll()
                print(f"{self.name} rolls: {dice}")
                hist = Histogram(dice)
                print(hist)
                if 1 in dice:
                    print("Pig! No points earned.")
                    turn_score = 0
                    break
                else:
                    turn_score += sum(dice)
            else:
                break
        self.score += turn_score
        print(f"{self.name} ends turn with {turn_score} points")
        print(f"{self.name} total score: {self.score}")
        if self.score >= 100:
            print(f"{self.name} wins!")
            high_scores.add_score(self.name, self.score)
            return True
        else:
            return False

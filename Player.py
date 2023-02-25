from DiceHand import DiceHand


class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.hand = DiceHand()

    def roll_dice(self):
        self.hand.roll_all()

    def select_dice(self, dice_indices):
        selected_dice = []
        for i in dice_indices:
            selected_dice.append(self.hand.dice[i])
            return selected_dice


    def get_score(self):
        return self.score

    def set_score(self, new_score):
        self.score = new_score

    def __str__(self):
        return f"Player {self.name} with score {self.score} and hand: {self.hand}"
from Dice import Dice


class Dicehand:
    def __init__(self, dice=None):
        self.dice = [Dice(), Dice()]  # default to two dice
        self.num_dice = len(self.dice)

    def roll(self):
        for die in self.dice:
            die.roll()

    def add_dice(self, num_dice=1, num_sides=6):
        for i in range(num_dice):
            self.dice.append(Dice(num_sides))
        self.num_dice = len(self.dice)

    def remove_dice(self, num_dice=1):
        for i in range(num_dice):
            self.dice.pop()
        self.num_dice = len(self.dice)

    def __str__(self):
        return f"DiceHand with {self.num_dice} dice: {', '.join(str(die) for die in self.dice)}"

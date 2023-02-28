from Dice import Dice

class Dicehand:
    def __init__(self, num_dice=1, num_sides=6):
        self.dice = [Dice(num_sides) for _ in range(num_dice)]
        self.values = []

    def roll(self):
        self.values = [die.roll() for die in self.dice]
        return self.values

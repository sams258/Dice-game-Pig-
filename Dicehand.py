from Dice import Dice

class Dicehand:
    def __init__(self, dice=None):
        self.dice = dice or [Dice(), Dice()]  # default to two dice
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

##############################################

    # def __init__(self):
    #     self.dice = [Dice(), Dice(), Dice(), Dice(), Dice()]

    # def roll_all(self):
    #     for die in self.dice:
    #         die.roll()

    # def __str__(self):
    #     result = ''
    #     for die in self.dice:
    #         result = result + str(die) + ' '
    #     return result

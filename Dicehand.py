import random

class Dicehand:
    def __init__(self):
        self.dice = []
        for i in range(5):
            self.dice.append(Die())
    def roll(self):
        for die in self.dice:
            die.roll()
    def __str__(self):
        result = ''
        for die in self.dice:
            result = result + str(die) + ''
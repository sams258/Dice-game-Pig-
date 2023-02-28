import random

class Dice:
    def __init__(self, faces=6):
        self.sides = faces

    def roll(self):
        return random.randint(1, self.sides)
    
    def __str__(self):
        return "A " + str(self.sides) + "-sided dice"



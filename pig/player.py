from pig.print import Print
from pig.histogram import Histogram
import random


class Player:
    def __init__(self, name):
        self.name = name
        self.total_score = 0

    def take_turn(self):
        turn_score = 0
        while True:
            roll = random.randint(1, 6)
            Print.print_sleep(f"{self.name} rolled a {[roll]}")

            Histogram.add_roll(roll)
            if roll == 1:
                Print.print_sleep(f"{self.name} lost their turn!")

                return 0
            else:
                turn_score += roll
                Print.print_sleep(f"{self.name}'s current "
                                  "turn score: {turn_score}")

                while True:
                    try:
                        choice = input("Do you want to Roll or Hold?"
                                       "(r/h) ")

                        if choice.lower() not in ["r", "h", "c"]:
                            raise ValueError
                        break
                    except ValueError:
                        Print.print_sleep(
                            "Invalid input. Please enter 'r', 'h', or 'c'."
                        )

                if choice.lower() == "h":
                    self.total_score += turn_score
                    Print.print_sleep(f"{self.name}'s total score: "
                                      "{self.total_score}")

                    return turn_score
                elif choice.lower() == "c":
                    self.total_score = 100
                    Print.print_sleep(f"{self.name} cheated and won the game!")

                    return 100

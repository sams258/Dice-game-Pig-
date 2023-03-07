from Player import Player
from Print import Print
from Histogram import Histogram
import random

class ComputerPlayer(Player):
    def __init__(self, name, difficulty):
        super().__init__(name)
        self.difficulty = difficulty

    def take_turn(self):
        turn_score = 0
        while True:
            
            roll = random.randint(1, 6)
            dice_faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
            Print.print_sleep(f"{self.name} rolled a {[roll]} {dice_faces[roll-1]}")
            
            Histogram.add_roll(roll)
            if roll == 1:
                Print.print_sleep(f"{self.name} lost their turn!")
                
                return 0
            else:
                turn_score += roll
                Print.print_sleep(f"{self.name}'s current turn score: {turn_score}")
                
                if self.difficulty == "easy":
                    if turn_score >= 10:
                        self.total_score += turn_score
                        Print.print_sleep(f"{self.name}'s total score: {self.total_score}")
                        
                        return turn_score
                elif self.difficulty == "hard":
                    if turn_score >= (15 - len(str(self.total_score))):
                        self.total_score += turn_score
                        Print.print_sleep(f"{self.name}'s total score: {self.total_score}")
                        
                        return turn_score
                else:
                    # choice = input("Do you want to roll again? (y/n) ")
                    # if choice.lower() == "n":
                        
                        self.total_score += turn_score
                        Print.print_sleep(f"{self.name}'s total score: {self.total_score}")
                        
                        return turn_score

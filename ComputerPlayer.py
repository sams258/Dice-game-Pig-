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
            Print.print_sleep(f"{self.name} rolled a {[roll]}")
            
            Histogram.add_roll(roll)
            if roll == 1:
                Print.print_sleep(f"{self.name} lost their turn!")
                
                return 0
            else:
                turn_score += roll
                Print.print_sleep(f"{self.name}'s current turn score: {turn_score}")
                
                if self.difficulty == "easy":
                    if turn_score >= 15:
                        self.total_score += turn_score
                        Print.print_sleep(f"{self.name}'s total score: {self.total_score}")
                        
                        return turn_score
                elif self.difficulty == "hard":
                    if turn_score >= (25 - len(str(self.total_score))):
                        self.total_score += turn_score
                        Print.print_sleep(f"{self.name}'s total score: {self.total_score}")
                        
                        return turn_score
                else:

                        
                        self.total_score += turn_score
                        Print.print_sleep(f"{self.name}'s total score: {self.total_score}")
                        
                        return turn_score


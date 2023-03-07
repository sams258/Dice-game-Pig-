from Game import Game
from Player import Player
from ComputerPlayer import ComputerPlayer
from Print import Print


class Main:
    def __init__(self):
        self.game = Game()

    def start(self):
        while True:
            try:
                choice = input("\nDo you want to play the Pig dice game? (y/n) ")
                if choice.lower() not in ["y", "n"]:
                    raise ValueError
                break
            except:
                Print.print_sleep("\nInvalid input. Please enter 'y' or 'n'.")
        if choice.lower() == "y":
            while True:
                try:
                    mode_choice = int(input("\nPlay against Computer or Human? choose 1 for computer or 2 for human: "))
                    if mode_choice not in [1, 2]:
                        raise ValueError
                    break
                except:
                    Print.print_sleep("\nInvalid input. Please enter 1 or 2.")
            
            if mode_choice == 1:
                while True:
                    try:
                        difficulty_choice = int(input("\nChoose difficulty: 1 for easy or 2 for hard: "))
                        if difficulty_choice not in [1, 2]:
                            raise ValueError
                        break
                    except:
                        Print.print_sleep("\nInvalid input. Please enter 1 or 2.")
                name = input("\nEnter your name: ")
                self.game.players.append(Player(name))
                self.game.players.append(ComputerPlayer("Computer", "easy" if difficulty_choice == 1 else "hard"))
                
            elif mode_choice == 2:
                name1 = input("\nEnter Player 1's name: ")
                self.game.players.append(Player(name1))
                name2 = input("\nEnter Player 2's name: ")
                self.game.players.append(Player(name2))
            
            self.game.start()
        else:
            Print.print_sleep("\nThanks for playing!")

if __name__ == "__main__":
    main = Main()
    main.start()

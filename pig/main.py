"""This module contains the Main class."""

import sys
import os
from game import Game
from scoreboard import Scoreboard
from player import Player
from computer_player import ComputerPlayer


class Main:
    """The main class for the Pig game."""

    def __init__(self):
        """Initialize a new instance of the Main.

        class with a new Game and empty player_name and scoreboard.
        """
        self.game = Game()
        self.player_name = ""
        self.scoreboard = Scoreboard()

    def display_menu(self):
        """Display the main menu of the game."""
        print("+" + "-" * 35 + "+")
        print("|" + " " * 13 + "PIG MENU" + " " * 14 + "|")
        print("+" + "-" * 35 + "+")
        print("|" + " " * 35 + "|")
        print("|" + " " * 6 + "1. Start Game" + " " * 16 + "|")
        print("|" + " " * 6 + "2. Show Rules" + " " * 16 + "|")
        print("|" + " " * 6 + "3. Show High Scores" + " " * 10 + "|")
        print("|" + " " * 6 + "4. Restart Game" + " " * 14 + "|")
        print("|" + " " * 6 + "5. Exit Game" + " " * 17 + "|")
        print("|" + " " * 35 + "|")
        print("+" + "-" * 35 + "+")

    def start(self):
        """Start the Pig game.

        and waits for user input to navigate the game menus.
        """
        while True:
            self.display_menu()
            try:
                choice = int(input("\nEnter your choice: "))
                if choice not in [1, 2, 3, 4, 5]:
                    raise ValueError
            except ValueError:
                print("\nInvalid input. "
                      "Please enter a number between 1 and 5.\n")
                continue

            if choice == 1:
                self.start_game()
            elif choice == 2:
                self.show_rules()
            elif choice == 3:
                self.show_high_scores()
            elif choice == 4:
                self.restart_game()
            elif choice == 5:
                self.exit_game()
            else:
                self.display_menu()

    def start_game(self):
        """Start a new game of Pig.

        and allows the user to choose the game mode and players.
        """
        while True:
            try:
                mode_choice = int(
                    input(
                        "\nPlay against Computer or Human? "
                        "choose 1 for computer or 2 for human: "
                    )
                )
                if mode_choice not in [1, 2]:
                    raise ValueError
                break
            except ValueError:
                print("\nInvalid input. Please enter 1 or 2.\n")

        if mode_choice == 1:
            while True:
                try:
                    difficulty_choice = int(
                        input("\nChoose difficulty: "
                              "1 for easy or 2 for hard: ")
                    )
                    if difficulty_choice not in [1, 2]:
                        raise ValueError
                    break
                except ValueError:
                    print("\nInvalid input. Please enter 1 or 2.\n")

            if not self.player_name:
                self.player_name = input("\nEnter your name: ")
            self.game.players.append(Player(self.player_name))
            self.game.players.append(
                ComputerPlayer("Computer", "easy"
                               "" if difficulty_choice == 1 else "hard")
            )

        elif mode_choice == 2:
            if not self.player_name:
                name1 = input("\nEnter Player 1's name: ")
            if name1 == self.player_name:
                name1 += " (You)"
            self.game.players.append(Player(name1))
            name2 = input("\nEnter Player 2's name: ")
            if name2 == self.player_name:
                name2 += " (You)"
            self.game.players.append(Player(name2))

        self.game.start()

    def show_rules(self):
        """Display the rules of the Pig game."""
        os.system("cls")
        print("+" + "-" * 64 + "+")
        print("|" + " " * 29 + "RULES" + " " * 30 + "|")
        print("+" + "-" * 64 + "+")
        print("|" + " " * 64 + "|")
        print(
            "|"
            + " " * 7
            + "The objective of the game is to be the first player"
            + " " * 6
            + "|"
        )
        print("|" + " " * 7 + "to reach 100 points." + " " * 37 + "|")
        print("|" + " " * 64 + "|")
        print(
            "|"
            + " " * 7
            + "On each turn, the player rolls a six-sided die. If"
            + " " * 7
            + "|"
        )
        print(
            "|"
            + " " * 7
            + "the player rolls a 1, their turn ends and they"
            + " " * 11
            + "|"
        )
        print("|" + " " * 7 + "receive no points." + " " * 39 + "|")
        print("|" + " " * 64 + "|")
        print(
            "|"
            + " " * 7
            + "If the player rolls any other number, they can"
            + " " * 11
            + "|"
        )
        print(
            "|"
            + " " * 7
            + "choose to roll again or hold to keep score."
            + " " * 14
            + "|"
        )
        print("|" + " " * 64 + "|")
        print(
            "|" + " " * 7 + "If a player chooses to hold their turn, "
            "" + " " * 17 + "|"
        )
        print("|" + " " * 7 + "total is added to their score."
              "" + " " * 27 + "|")
        print("|" + " " * 64 + "|")
        print("+" + "-" * 64 + "+")
        input("\nPress Enter to continue...")

    def show_high_scores(self):
        """Display the high scores of the Pig game."""
        os.system("cls")
        print("+" + "-" * 35 + "+")
        print(
            "|"
            + " " * int((36 - len("HIGH SCORES") - len(self.player_name)) / 2)
            + "HIGH SCORES"
            + " " * int((35 - len("HIGH SCORES") - len(self.player_name)) / 2)
            + "|"
        )
        print("+" + "-" * 35 + "+")
        high_scores = self.scoreboard.get_high_scores()
        if not high_scores:
            print("|" + " " * 7 + "No high scores yet." + " " * 9 + "|")
            print("+" + "-" * 35 + "+")
            return
        for i, score in enumerate(high_scores):
            print(f"| {i+1}. {score[0]:<{25-len(self.player_name)}}"
                  f"{score[1]:>4}  |")
        print("+" + "-" * 35 + "+")

    def restart_game(self):
        """Restarts the Pig game."""
        self.game = Game()
        self.player_name = ""
        print("\nGame restarted.\n")

    def exit_game(self):
        """Exit the Pig game."""
        print("\nThanks for playing!")
        sys.exit()


if __name__ == "__main__":
    main = Main()
    main.start()

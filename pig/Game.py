from pig.Player import Player
from pig.ComputerPlayer import ComputerPlayer
from pig.Print import Print
from pig.Histogram import Histogram
from pig.Scoreboard import Scoreboard
import sys


class Game:
    def __init__(self):
        self.scoreboard = Scoreboard()
        self.players = []
        self.round = 0
        self.game_over = False

    def start(self):
        while not self.game_over:
            self.round += 1
            self.play_round()
        self.end_game()

    def play_round(self):
        self.add_players()
        Print.print_sleep("\nWelcome to the Pig dice game!")
        Print.print_sleep(f"\nRound {self.round}:")
        while True:
            for player in self.players:
                Print.print_sleep(f"\n{player.name}'s turn:")

                player_score = player.take_turn()
                if player_score == 0:
                    continue
                self.scoreboard.add_score(player.name, player_score)
                if self.check_win_condition(player):
                    self.game_over = True
                    return

    def add_players(self):
        if self.players:
            for i, player in enumerate(self.players):
                Print.print_sleep(f"Player {i + 1}: {player.name}")
                if isinstance(player, ComputerPlayer):
                    continue
                while True:
                    try:
                        new_name = input("\nDo you want to change your name? (y/n) ")
                        if new_name.lower() == "y":
                            new_name = input("\nEnter your new name: ")
                            player_name_stats = self.scoreboard.scores.pop(player.name)
                            player.name = new_name
                            self.scoreboard.scores[new_name] = player_name_stats
                        elif new_name.lower() == "n":
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        Print.print_sleep("\nInvalid input. Please enter 'y' or 'n'.")
            return
        while True:
            try:
                game_mode = input(
                    "\nDo you want to play against the computer or another human player? Choose 1 for computer or 2 for human. "
                )
                if game_mode not in ["1", "2"]:
                    raise ValueError
                break
            except:
                Print.print_sleep(
                    "\nInvalid input. Please choose 1 for computer or 2 for human."
                )
        if game_mode == "1":
            while True:
                try:
                    difficulty = input(
                        "\nChoose difficulty: 1 for easy or 2 for hard. "
                    )
                    if difficulty not in ["1", "2"]:
                        raise ValueError
                    break
                except:
                    Print.print_sleep(
                        "\nInvalid input. Please choose 1 for easy or 2 for hard."
                    )
            name = input("\nEnter your name: ")
            self.players.append(Player(name))
            self.players.append(ComputerPlayer("Computer", difficulty))
        else:
            name1 = input("\nEnter Player 1's name: ")
            self.players.append(Player(name1))
            name2 = input("\nEnter Player 2's name: ")
            self.players.append(Player(name2))

    def check_win_condition(self, player):
        if player.total_score >= 100:
            return True
        else:
            return False

    def end_game(self):
        winner_score = -1
        winner_name = ""
        for player in self.players:
            if player.total_score >= 100 and player.total_score > winner_score:
                winner_score = player.total_score
                winner_name = player.name
        if winner_name != "":
            Print.print_sleep(f"\n{winner_name} wins!")
        else:
            Print.print_sleep("\nNo one wins!")

        Print.print_sleep("\nGame over!")
        high_scores = self.scoreboard.get_high_scores()
        Print.print_sleep("\nHighest Round Score:")
        for score in high_scores:
            Print.print_sleep(f"{score[0]}: {score[1]}")
        Histogram.display()

        self.play_again()

    def play_again(self):
        while True:
            try:
                choice = input("\nDo you want to play again? (y/n) ")
                if choice.lower() not in ["y", "n"]:
                    raise ValueError
                break
            except:
                Print.print_sleep("\nInvalid input. Please enter 'y' or 'n'.")
        if choice.lower() == "y":
            self.players.clear()
            self.round = 0
            self.game_over = False
            self.add_players()
            self.start()
        else:
            Print.print_sleep("\nThanks for playing!")
            sys.exit()

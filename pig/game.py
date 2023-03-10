"""This module contains the Game class."""

import sys
from player import Player
from computer_player import ComputerPlayer
from print import Print
from histogram import Histogram
from scoreboard import Scoreboard


class Game:
    """A class representing the Pig dice game.

    Attributes:
        scoreboard (Scoreboard): The scoreboard to keep track of scores.
        players (list): A list of Player objects.
        round (int): The current round of the game.
        game_over (bool): Whether the game is over or not.
    """

    def __init__(self):
        """Initialize the Game object."""
        self.scoreboard = Scoreboard()
        self.players = []
        self.round = 0
        self.game_over = False

    def start(self):
        """Start the game."""
        while not self.game_over:
            self.round += 1
            self.play_round()
        self.end_game()

    def play_round(self):
        """Play a round of the game."""
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
        """Add players to the game."""
        if self.players:
            self.change_names()
            return
        self.get_game_mode()
        self.get_player_names()

    def change_names(self):
        """Change the name of players in the game."""
        for i, player in enumerate(self.players):
            Print.print_sleep(f"Player {i + 1}: {player.name}")
            if isinstance(player, ComputerPlayer):
                continue
            while True:
                try:
                    new_name = input("\nDo you want to change your name in Highscores? (y/n) ")
                    if new_name.lower() == "y":
                        if player.name in self.scoreboard.scores:
                            self.change_player_name(player)
                        else:
                            Print.print_sleep("\nPlayer name not found in Highscores.")
                            break
                    elif new_name.lower() == "n":
                        break
                    else:
                        raise ValueError
                except ValueError:
                    Print.print_sleep("\nInvalid input. Please enter 'y' or 'n'.")

    def change_player_name(self, player):
        """Change the name of a player in the game."""
        new_name = input("\nEnter your new name: ")
        player_name_stats = self.scoreboard.scores.pop(player.name)
        player.name = new_name
        self.scoreboard.scores[new_name] = player_name_stats

    def get_game_mode(self):
        """Get the game mode from the user."""
        while True:
            try:
                game_mode = input("\nDo you want to play against the computer or another human player? Choose 1 for computer or 2 for human. ")
                if game_mode not in ["1", "2"]:
                    raise ValueError
                break
            except:
                Print.print_sleep("\nInvalid input. Please choose 1 for computer or 2 for human.")
        if game_mode == "1":
            difficulty = self.get_computer_difficulty()
            name = input("\nEnter your name: ")
            self.players.append(Player(name))
            self.players.append(ComputerPlayer("Computer", difficulty))

    def get_computer_difficulty(self):
        """Get the computer difficulty from the user."""
        while True:
            try:
                difficulty = input("\nChoose difficulty: 1 for easy or 2 for hard. ")
                if difficulty not in ["1", "2"]:
                    raise ValueError
                break
            except:
                Print.print_sleep("\nInvalid input. Please choose 1 for easy or 2 for hard.")
            self.computer_difficulty = difficulty

    def get_player_names(self):
        """Get the names of the players from the user."""
        name1 = input("\nEnter Player 1's name: ")
        self.players.append(Player(name1))
        name2 = input("\nEnter Player 2's name: ")
        self.players.append(Player(name2))
        
    def check_win_condition(self, player):
        """Check if the player has won the game.

    Args:
        player (Player): The player to check for winning.

    Returns:
        bool: True if the player has won, False otherwise.
    """
        if player.total_score >= 100:
            return True
        else:
            return False

    def end_game(self):
        """Prints the winner of the game and ends the game."""
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
            print(f"{score[0]}: {score[1]}")
        Histogram.display()

        self.play_again()

    def play_again(self):
        """Asks the player if they want to play again.

    If the player chooses to play again, starts a new game.
    Otherwise, ends the game.
    """
        while True:
            try:
                choice = input("\nDo you want to play again? (y/n) ")
                if choice.lower() not in ["y", "n"]:
                    raise ValueError
                break
            except ValueError:
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

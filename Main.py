from Dice import Dice
from Dicehand import Dicehand
from Player import Player
from Histogram import Histogram
from Highscore import Highscore
from Intelligence import Intelligence
from Game import Game


class Main:
  
    high_scores = Highscore()
    player1 = Player("Alice")
    player2 = Player("Bob", Intelligence("medium"))
    game = Game(player1, player2, high_scores)
    game.play()
    

import random
import pandas as pd
from Player import Player

RNG = random.SystemRandom()
SCORE_LIMIT = 10000
NUM_PLAYERS = 5

def generate_possibilities(num_dice):
    pass

def setup():
    players = []
    for i in range(NUM_PLAYERS):
        players.append(Player(i))
    return players


def turn(players):
    for player in players:
        #Here is where the game logic for a player taking their turn is outlined
        print(player.id)



if __name__ == "__main__":
    players = setup()
    turn(players)


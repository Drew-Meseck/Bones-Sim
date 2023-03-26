import random
import pandas as pd
from Player import Player

RNG = random.SystemRandom()
SCORE_LIMIT = 10000
NUM_PLAYERS = 5



    

def score(hand):
    pass

def generate_score_possibilities(p, memo={}):
    for hand in p:
        score(p)
        
    



def setup():
    players = []
    for i in range(NUM_PLAYERS):
        players.append(Player(i))
    return players


def turn(players):
    for player in players:
        scores = [player.score for player in players]
        #Here is where the game logic for a player taking their turn is outlined
        print('Turn Player: ' + str(player.id))
        player.take_turn(scores)



if __name__ == "__main__":
    players = setup()

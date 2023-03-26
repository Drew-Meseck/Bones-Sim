import random
from itertools import product

RNG = random.SystemRandom()


class Player():
    def __init__(self, i):
        self.id = i
        self.hand = []
        self.state = True
        self.score = 0
        self.scoring = []
        self.scoring_dict = {
            (1): 100,
            (5): 50,
            (1,1,1): 1000,
            (1,1,1,1): 10000,
            (2,2,2): 200,
            (2,2,2,2): 1200,
            (2,2,2,2,2): 2000,
            (3,3,3): 300,
            (3,3,3,3): 1300,
            (3,3,3,3,3): 3000,
            (4,4,4): 400,
            (4,4,4,4): 1400,
            (4,4,4,4,4): 4000,
            (5,5,5): 500,
            (5,5,5,5): 1500,
            (5,5,5,5,5): 5000,
            (6,6,6): 600,
            (6,6,6,6): 1600,
            (6,6,6,6,6): 6000
        }
    
    def state_true(self):
        self.state = True

    def state_false(self):
        self.state = False
    
    def generate_hand(self):
        self.hand = sorted([RNG.randint(1,6) for i in len(self.hand)])

    
    def check_for_trips_quads(self):
        counts = [0] * 6
        for die in self.hand:
            counts[die-1] += 1
        for count in counts:
            if count >= 3:
                return True  # Found triples
        for count in counts:
            if count == 4 or count == 5:
                return True  # Found quads or fives of a kind
        return False  # No triples or quads found

    #This probably needs to be recursive in order to make sense. Work this out logically...
    def generate_score_possibilities(self):
        for key in self.scoring_dict.keys():
            score = 0
            key = list(key)
            if len(key) <= self.hand:
                if set(key) <= set(self.hand):
                    score += self.scoring_dict[key]




    def choose_scoring(self):
        if 5 not in self.hand or 1 not in self.hand:
            if not self.check_for_trips_quads():
                return 0
        else:
            s = self.generate_possibilities()

        for die in self.hand: #Choose which die to take if any.
            pass


    def take_turn(self, scores):
        pass

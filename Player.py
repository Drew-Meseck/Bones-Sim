import random
RNG = random.SystemRandom()


class Player():
    def __init__(self, i):
        self.id = i
        self.hand = []
        self.state = True
        self.score = 0
        self.scoring = []
        self.scoring_dict = {
            1: 100,
            5: 50,
            (1,1,1): 1000,
            (1,1,1,1): 2000,
            (2,2,2): 200,
            (2,2,2,2): 1200,
            (3,3,3): 300,
            (3,3,3,3): 1300,
            (4,4,4): 400,
            (4,4,4,4): 1400,
            (5,5,5): 500,
            (5,5,5,5): 1500,
            (6,6,6): 600,
            (6,6,6,6): 1600
        }
    
    def state_true(self):
        self.state = True

    def state_false(self):
        self.state = False
    
    def generate_hand(self):
        self.hand = sorted([RNG.randint(1,6) for i in len(self.hand)])

    def choose_scoring(self):
        for die in self.hand: #Choose which die to take if any.
            if 

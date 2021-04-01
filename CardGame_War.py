import shuffle
class Card:
    def __init__(self,rank):
        self.rank=rank

class Deck:
    def __init__(self):
        self.cards=[]

    def generate_deck(self):
        #pass
    def shuffle_deck(self,totaldec):
        #pass
    
class Game:
    def __init__(self,player1_cards,player2_cards):
        self.player1_cards=player1_cards
        self.player2_cards=player2_cards
        self.player1_cards_ontable=[]
        self.player2_cards_ontable=[]
        self.round=0

    def play(self):
        self.round+=1
        while self.player1_cards and self.player2_cards:
            #pass
            

if __name__=="__main__":
    # generate deck
    # play game 


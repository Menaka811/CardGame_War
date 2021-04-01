import random
class Card:
    def __init__(self,rank):
        self.rank=rank

class Deck:
    def __init__(self):
        self.cards=[]

    def generate_deck(self,suites,number_of_cardtypes):
        for s in range(suites):
            for cardtype in range(1,number_of_cardtypes+1):
                self.cards.append(Card(cardtype))
        
    def shuffle_deck(self):
        random.shuffle(self.cards)
        return self.cards

    def split_deck(self):
        l=len(self.cards)//2
        return self.cards[:l],self.cards[l:]
    
class Game:
    def __init__(self,player1_cards,player2_cards):
        self.player1_cards=player1_cards
        self.player2_cards=player2_cards
        self.player1_cards_ontable=[]
        self.player2_cards_ontable=[]
        self.round_number=0

    def play(self):
        
        while self.player1_cards and self.player2_cards:
            self.round_number+=1
            card_p1 =self.player1_cards.pop()
            card_p2= self.player2_cards.pop()
            if card_p1.rank > card_p2.rank:
                self.player1_cards= [card_p1,card_p2]+ self.player1_cards_ontable+ self.player2_cards_ontable+ self.player1_cards
                self.player1_cards_ontable=[]
                self.player2_cards_ontable=[]
            elif card_p2.rank > card_p1.rank:
                self.player2_cards=[card_p2,card_p1]+ self.player2_cards_ontable+ self.player1_cards_ontable+ self.player2_cards
                self.player1_cards_ontable=[]
                self.player2_cards_ontable=[]               
            elif card_p1.rank == card_p2.rank:
                self.player1_cards_ontable.extend([card_p1]+self.player1_cards[-3:])
                self.player1_cards= self.player1_cards[:-3]
                self.player1_cards.append(self.player1_cards_ontable.pop())

                self.player2_cards_ontable.extend([card_p2]+self.player2_cards[-3:])
                self.player2_cards= self.player2_cards[:-3]
                self.player2_cards.append(self.player2_cards_ontable.pop())
            print("round",self.round_number)
            print("Number of cards for player1", len(self.player1_cards))
            print("Number of cards of player1 on table", len(self.player1_cards_ontable))
            print("Number of cards for player2", len(self.player2_cards))
            print("Number of cards of player2 on table", len(self.player2_cards_ontable))
            print("------------")
        if len(self.player1_cards)==0:
            print("Player2 is the Winner")
        elif len(self.player2_cards)==0:
            print("Player1 is the Winner")
            

if __name__=="__main__":
    deck= Deck()
    deck.generate_deck(4,13)
    deck.shuffle_deck()
    cards_p1,cards_p2=deck.split_deck()
    game= Game(cards_p1,cards_p2)
    game.play()
    # play game 


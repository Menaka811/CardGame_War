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


    def compare_faceup_cards(self,rank1,rank2):
        if rank1> rank2:
            return 1
        elif rank2> rank1:
            return -1
        elif rank1 == rank2:
            return 0

    def is_stack_empty(self,s):
        if len(s)==0:
            return True
        elif len(s)>0:
            return False

    def play(self):
        while True:
            self.round_number+=1
            while True:

                if not self.is_stack_empty(self.player1_cards) or not self.is_stack_empty(self.player2_cards):
                    card_p1 =self.player1_cards.pop()
                    card_p2= self.player2_cards.pop()
                    print("Current Player1 Faceup Card Value: ",card_p1.rank)
                    print("Current PLayer2 Faceup Card Value: ",card_p2.rank)
                    comp= self.compare_faceup_cards(card_p1.rank,card_p2.rank)

                if comp == 1:
                    self.player1_cards= [card_p1,card_p2]+ self.player1_cards_ontable+ self.player2_cards_ontable+ self.player1_cards
                    self.player1_cards_ontable=[]
                    self.player2_cards_ontable=[]
                    break
                elif comp == -1:
                    self.player2_cards=[card_p2,card_p1]+ self.player2_cards_ontable+ self.player1_cards_ontable+ self.player2_cards
                    self.player1_cards_ontable=[]
                    self.player2_cards_ontable=[]    
                    break           
                elif comp == 0:
                    print("********* IN WAR **************")
                    if len(self.player1_cards)<=3:
                        self.player1_cards_ontable.extend([card_p1]+self.player1_cards[:])
                        self.player1_cards=[]
                        self.player1_cards.append(self.player1_cards_ontable.pop())
                    else:
                        self.player1_cards_ontable.extend([card_p1]+self.player1_cards[-3:])
                        self.player1_cards= self.player1_cards[:-3]
                        #self.player1_cards.append(Card(3))
                        #self.player1_cards.append(self.player1_cards_ontable.pop())
                    if len(self.player2_cards)<=3:
                        self.player2_cards_ontable.extend([card_p2]+self.player2_cards[:])
                        self.player2_cards=[]
                        self.player2_cards.append(self.player2_cards_ontable.pop())
                    else:
                        self.player2_cards_ontable.extend([card_p2]+self.player2_cards[-3:])
                        self.player2_cards= self.player2_cards[:-3]
                        #self.player2_cards.append(Card(3))
                        #self.player2_cards.append(self.player2_cards_ontable.pop())
                    break

            print("After Round Number: ",self.round_number)
            print("Number of Cards for Player1: ", len(self.player1_cards))
            print("Number of Cards of Player1 on table: ", len(self.player1_cards_ontable))
            print("Number of Cards for Player2: ", len(self.player2_cards))
            print("Number of Cards of Player2 on table: ", len(self.player2_cards_ontable))
            print("---------------------------------------------------")
            if self.is_stack_empty(self.player1_cards):
                print("Player2 is the Winner")
                break

            elif self.is_stack_empty(self.player2_cards):
                print("Player1 is the Winner")
                break

               

if __name__=="__main__":
    deck= Deck()
    deck.generate_deck(4,13)
    deck.shuffle_deck()
    cards_p1,cards_p2=deck.split_deck()
    game= Game(cards_p1,cards_p2)
    game.play()
    # play game 


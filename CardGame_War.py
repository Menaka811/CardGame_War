import random
class Card:
    def __init__(self,rank):
        self.rank=rank

class Deck:
    def __init__(self):
        self.cards=[]

    def generate_deck(self,suits,number_of_cardtypes):
        for s in range(suits):
            for cardtype in range(1,number_of_cardtypes+1):
                self.cards.append(Card(cardtype))
        
    def shuffle_deck(self):
        random.shuffle(self.cards)
        return self.cards

    def split_deck(self,n):
        l=len(self.cards)//n
        return self.cards[:l],self.cards[l:]
    
class Game:
    def __init__(self,player1_cards,player2_cards):
        self.player1_cards=player1_cards
        self.player2_cards=player2_cards
        self.player1_cards_ontable=[]
        self.player2_cards_ontable=[]
        self.round_number=0

        ''' 
        Number of cards used to place on table play during WAR.
        Hardcoded as 3, but can be changed if you want to change the rules of the game
        '''
        self.min_card_count_war=3

    def compare_faceup_cards(self,rank1,rank2):
        # 
        if rank1> rank2:
            return "player1"
        elif rank2> rank1:
            return "player2"
        elif rank1 == rank2:
            return "war"

    def is_stack_empty(self,s):
        if len(s)==0:
            return True
        elif len(s)>0:
            return False

    def has_mincards(self,cards):
        # Checks if the player has min number of cards to play in WAR. 
        if len(cards)<=self.min_card_count_war:
            return False
        elif len(cards)>self.min_card_count_war:
            return True

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

                if comp == "player1":
                    self.player1_cards= [card_p1,card_p2]+ self.player1_cards_ontable+ self.player2_cards_ontable+ self.player1_cards
                    self.player1_cards_ontable=[]
                    self.player2_cards_ontable=[]
                    break
                elif comp == "player2":
                    self.player2_cards=[card_p2,card_p1]+ self.player2_cards_ontable+ self.player1_cards_ontable+ self.player2_cards
                    self.player1_cards_ontable=[]
                    self.player2_cards_ontable=[]    
                    break           
                elif comp == "war":
                    print("********* IN WAR **************")
                    if not self.has_mincards(self.player1_cards):
                        self.player1_cards_ontable.extend([card_p1]+self.player1_cards[:])
                        self.player1_cards=[]
                        self.player1_cards.append(self.player1_cards_ontable.pop())
                    else:
                        self.player1_cards_ontable.extend([card_p1]+self.player1_cards[-self.min_card_count_war:])
                        self.player1_cards= self.player1_cards[:-self.min_card_count_war]

                    if not self.has_mincards(self.player2_cards):
                        self.player2_cards_ontable.extend([card_p2]+self.player2_cards[:])
                        self.player2_cards=[]
                        self.player2_cards.append(self.player2_cards_ontable.pop())
                    else:
                        self.player2_cards_ontable.extend([card_p2]+self.player2_cards[-self.min_card_count_war:])
                        self.player2_cards= self.player2_cards[:-self.min_card_count_war]

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
    cards_p1,cards_p2=deck.split_deck(2)
    game= Game(cards_p1,cards_p2)
    game.play()
    # play game 


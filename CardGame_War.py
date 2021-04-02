import random
class Card:
    def __init__(self,suit,rank):
        self.rank=rank
        self.suit=suit

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit

class Deck:
    def __init__(self):
        self.cards=[]

    def generate_deck(self,suits,number_of_cardtypes):
        suits=['C','D','H','S'] # Clubs,Diamonds,Spades,Hearts
        for s in suits:
            for cardtype in range(1,number_of_cardtypes+1):
                self.cards.append(Card(s,cardtype))
        
    def shuffle_deck(self):
        random.shuffle(self.cards)
        return self.cards

    def split_deck(self,n):
        # Can be extended for more players
        l=len(self.cards)//n
        return self.cards[:l],self.cards[l:]

class Player:
    def __init__(self,name,cards,cards_on_table=[]):
        self.name=name
        self.cards=cards
        self.cards_on_table=cards_on_table

    def get_name(self):
        return self.name

    def get_cards(self):
        return self.cards
        
    def get_cards_on_table(self):
        return self.cards_on_table


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
        # Can be extended for more players
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

    def is_end_of_game(self):

        if self.round_number >1000:
            print("Game is taking too long. Might as well Exit and start New game")
            return True

        if self.is_stack_empty(self.player1_cards):
            print("Player2 is the Winner")
            return True

        elif self.is_stack_empty(self.player2_cards):
            print("Player1 is the Winner")
            return True

        return False


    def play(self):
        
        while True:
            self.round_number+=1
            while True:
                if not self.is_stack_empty(self.player1_cards) or not self.is_stack_empty(self.player2_cards):
                    card_p1 =self.player1_cards.pop()
                    card_p2= self.player2_cards.pop()
                    rank1,suit1= card_p1.get_rank(),card_p1.get_suit()
                    rank2,suit2=card_p2.get_rank(),card_p2.get_suit()
                    print("Current Player1 Faceup Card Value: ",str(rank1)+ str(suit1))
                    print("Current PLayer2 Faceup Card Value: ",str(rank2)+ str(suit2))
                    comp= self.compare_faceup_cards(rank1,rank2)

                    if comp == "player1":
                        self.player1_cards= [card_p1,card_p2]+ self.player1_cards_ontable+ self.player2_cards_ontable+ self.player1_cards # The order is not specified by the game rules
                        self.player1_cards_ontable=[]
                        self.player2_cards_ontable=[]
                        break
                    elif comp == "player2":
                        self.player2_cards=[card_p2,card_p1]+ self.player2_cards_ontable+ self.player1_cards_ontable+ self.player2_cards # The order is not specified by the game rules
                        self.player1_cards_ontable=[]
                        self.player2_cards_ontable=[]    
                        break           
                    elif comp == "war":
                        print("*********** IN WAR **************")

                        '''
                        If the player does not have min cards to play WAR. All the player's cards on placed on table and
                        the top card on the table is used to play the round.
                        If the player runs out of card,the top card on the table is used to play the round
                        '''
                        if not self.has_mincards(self.player1_cards):
                            self.player1_cards_ontable.extend([card_p1]+self.player1_cards[:])
                            self.player1_cards=[]
                            self.player1_cards.append(self.player1_cards_ontable.pop())
                        else:
                            self.player1_cards_ontable.extend([card_p1]+self.player1_cards[-3:]) 
                            self.player1_cards= self.player1_cards[:-3]

                        if not self.has_mincards(self.player2_cards):
                            self.player2_cards_ontable.extend([card_p2]+self.player2_cards[:])
                            self.player2_cards=[]
                            self.player2_cards.append(self.player2_cards_ontable.pop())
                        else:
                            self.player2_cards_ontable.extend([card_p2]+self.player2_cards[-3:])
                            self.player2_cards= self.player2_cards[:-3]

                        break

            print("After Round Number: ",self.round_number)
            print("Number of Cards for Player1: ", len(self.player1_cards))
            print("Number of Cards of Player1 on table: ", len(self.player1_cards_ontable))
            print("Number of Cards for Player2: ", len(self.player2_cards))
            print("Number of Cards of Player2 on table: ", len(self.player2_cards_ontable))
            print("---------------------------------------------------")

            if self.is_end_of_game():
                break



if __name__=="__main__":
    deck= Deck()
    deck.generate_deck(4,13) # 52 Cards
    deck.shuffle_deck()
    cards_p1,cards_p2=deck.split_deck(2)
    game= Game(cards_p1,cards_p2)
    game.play()



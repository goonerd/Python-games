# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand=[]	# create Hand object

    def __str__(self):
        hand = ""
        for i in range(len(self.hand)):
            hand+= self.hand[i].__str__()+" "
        return "Hand contains "+hand	# return a string representation of a hand

    def add_card(self, card):
            # add a card object to a hand
        self.hand.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        value=0
        has_ace=False
        for i in range(len(self.hand)):
            rank=self.hand[i].get_rank()
            value+=VALUES.get(rank)
            if rank=='A':
                has_ace=True
        if has_ace==True:
            if value+10 <=21:
                return value+10
            else:
                return value
            
        else:
            return value
                    
        if not ranks:
            return value
            
        # compute the value of the hand, see Blackjack video
        
   
    def draw(self, canvas, pos):
            # draw a hand on the canvas, use the draw method for cards
        for card in self.hand:
            
            card.draw(canvas,pos)
            pos[0]=pos[0]+CARD_SIZE[0]+18

# define deck class 
class Deck:
    def __init__(self):
        self.deck=[]	# create a Deck object
        for i in range(len(SUITS)):
            for j in range(len(RANKS)):
                self.deck.append(Card(SUITS[i],RANKS[j]))
                

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)    # use random.shuffle()

    def deal_card(self):
    # deal a card object from the deck
        dealt_card= random.choice(self.deck)
        self.deck.remove(dealt_card)
        return dealt_card
        
    def __str__(self):
            # return a string representing the deck
        deck=""
        for i in range(len(self.deck)):
            deck+= self.deck[i].__str__()+" "
        return "Deck contains "+deck       		
            


#define event handlers for buttons
def deal():
    global outcome, in_play, deck1,player,dealer

    # your code goes here
    deck1=Deck()
    deck1.shuffle()
    player=Hand()
    dealer=Hand()
    Card1=deck1.deal_card()
    Card2=deck1.deal_card()
    Card3=deck1.deal_card()
    Card4=deck1.deal_card()
    player.add_card(Card1)
    player.add_card(Card2)
    dealer.add_card(Card3)
    dealer.add_card(Card4)
    in_play = True
    #print "Player's",player
    #print "Dealer's",dealer
    outcome="Hit or Stand?"
    

def hit():
        # replace with your code below
    global player, outcome,in_play,score
    # if the hand is in play, hit the player
    if in_play:
        if player.get_value()<=21:
             
             player.add_card(deck1.deal_card())
             print player
             if player.get_value()>21:
                 outcome="You have busted"
                 in_play=False
                 score-=1
    #if dealer.get_value<=21:
    #     dealer.add_card()
    #     if dealer.get_value>21:
    #         print"You have busted"			 
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
        # replace with your code below
    global player,dealer,outcome,in_play,score
    if player.get_value()>21:
         outcome = "You have busted!"
         in_play=False
         score-=1
    else:
        print dealer
        if in_play:		
            while dealer.get_value()<17:
                dealer.add_card(deck1.deal_card())
                print dealer
            if dealer.get_value()>21:
                outcome = "Dealer has busted"
                in_play=False
                score+=1
            else:
                if player.get_value()<=dealer.get_value():
                    outcome= "Dealer wins!"
                    in_play=False
                    score-=1
                elif player.get_value()> dealer.get_value():
                    outcome="Player Wins!" 
                    in_play=False
                    score+=1
            
                
             
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score
     
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    #card = Card("S", "A")
    #card.draw(canvas, [300, 300])
    canvas.draw_text(outcome,[200,300],36,'Black')
    player.draw(canvas,[100,400])
    dealer.draw(canvas,[100,100])
    if in_play:
        canvas.draw_image(card_back,CARD_BACK_CENTER,CARD_BACK_SIZE,[136,148],CARD_BACK_SIZE)
    canvas.draw_text("Score = "+str(score),[400,100],36,'Black')
    canvas.draw_text("Blackjack",[200,50],48,'Red')
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric

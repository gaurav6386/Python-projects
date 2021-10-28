# Mini-project #6 - Blackjack
#Gaurav Pandey

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
outcome1=""
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
        #canvas.draw_image(card_back, [CARD_BACK_CENTER[0],CARD_BACK_CENTER[1]], CARD_BACK_SIZE, [100 +CARD_BACK_CENTER[0], 170 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
        if in_play:
            canvas.draw_image(card_back, [CARD_BACK_CENTER[0],CARD_BACK_CENTER[1]], CARD_BACK_SIZE, [100 +CARD_BACK_CENTER[0], 170 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
        
                  
# define hand class
class Hand:
    def __init__(self):
        self.card=[]

    def __str__(self):
        card_str=""
        for i in range(len(self.card)):
            card_str+=self.card[i].__str__()
        return card_str	                  # returns a string representation of a hand

    def add_card(self, card):
        
        self.card.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        value_of_hand=0
        
        for i in range(len(self.card)):                
            value_of_hand+=VALUES[self.card[i].get_rank()]
        if 'A' in self.__str__():
            if value_of_hand+10<=21:
                return value_of_hand+10
            else:
                return value_of_hand
        else:
            return value_of_hand
        # compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        for i in range(len(self.card)):
            self.card[i].draw(canvas,pos)
            pos[0]+=100        
        # draw a hand on the canvas, use the draw method for cards
 
        
# define deck class 
class Deck:
    def __init__(self):
#        self.cards=[]
#        for i in range(4):
#            col=[]
#            for j in range(13):
#                col.append(Card(SUITS[i],RANKS[j]))
#            self.cards.append(col)
       #List comprehension                
        self.cards = [[Card(SUITS[i],RANKS[j]) for j in range(13)] for i in range(4)]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        global player_hand,dealer_hand,outcome,player_i,player_j,dealer_i,dealer_j
        outcome="Hit or Stand?"
        player_hand=Hand()
        dealer_hand=Hand()
        in_play=True
        player_i,player_j,dealer_i,dealer_j=([] for i in range(4))
        
        #Following algorithm deals new card from the deck to player and the dealer
        choices=list(range(13))
        random.shuffle(choices)
        while len(choices)>9:
            player_i.append(random.randrange(0,4))
            player_j.append(choices.pop())
            dealer_i.append(random.randrange(0,4))
            dealer_j.append(choices.pop())
        #Uncomment the following line for testing
        #print "(",player_i[0],player_j[0],") (",dealer_i[0],dealer_j[0],") (",player_i[1],player_j[1],") (",dealer_i[1],dealer_j[1],")"
        
        for i in range(2):
            player_hand.add_card(self.cards[player_i[i]][player_j[i]])
            dealer_hand.add_card(self.cards[dealer_i[i]][dealer_j[i]])
        #Uncomment the following line for testing
        #print "Player hand has "+player_hand.__str__()+" and Dealer hand has "+dealer_hand.__str__()
            
        # deal a card object from the deck
    
    def __str__(self):
        str=""
        for i in range(4):
            for j in range(13):
                str+=str(self.cards[i][j].__str__())
        return str

#define event handlers for buttons
def deal():
    global outcome,outcome1, in_play,deck,player_hand,dealer_hand   
    outcome1=""
    deck=Deck()
    deck.shuffle()
    deck.deal_card()
    in_play = True
    

def hit():
    global deck,player_hand,dealer_hand,card,in_play,outcome,outcome1,score
    card=Card(SUITS[random.randrange(0,4)],RANKS[random.randrange(0,13)])
    while (card.__str__() in player_hand.__str__() or card.__str__() in dealer_hand.__str__()):
        card=Card(SUITS[random.randrange(0,4)],RANKS[random.randrange(0,13)])
    if in_play:
        player_hand.add_card(card)
        if player_hand.get_value()<=21:
            outcome="Hit or Stand?"
        else:
            score-=1
            outcome1="You went bust and lose!"
            outcome="New deal?"
            in_play=False
    else:
        score-=1
        outcome1="You lose!"
        outcome="New deal?"
    #Uncomment the following line for testing
    #print "Player hand has "+player_hand.__str__()+" and Dealer hand has "+dealer_hand.__str__()
        
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global in_play,score,player_hand,dealer_hand,outcome,outcome1
    while in_play:
        if dealer_hand.get_value()<17:
            card=Card(SUITS[random.randrange(0,4)],RANKS[random.randrange(0,13)])
            while (card.__str__() in player_hand.__str__() or card.__str__() in dealer_hand.__str__()):
                card=Card(SUITS[random.randrange(0,4)],RANKS[random.randrange(0,13)])
            dealer_hand.add_card(card)
        else:
            if dealer_hand.get_value()>21:
                outcome1="Dealer went bust. You won!"
                outcome="New deal?"
                score+=1
                in_play=False
            else:
                if player_hand.get_value()<=dealer_hand.get_value():
                    outcome1="You lose!"
                    outcome="New deal?"
                    in_play=False
                    score-=1
                else:
                    outcome1="You won!"
                    outcome="New deal?"
                    score+=1
                    in_play=False
                    
     
    #Uncomment the following for testing
    #print "Player hand has "+player_hand.__str__()+" and Dealer hand has "+dealer_hand.__str__()    
                    
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global player_hand,dealer_hand,outcome, in_play,outcome1
    canvas.draw_text("BLACKJACK",[80,60],40,"Fuchsia")
    canvas.draw_text("Dealer",[100,120],30,"Black")
    canvas.draw_text(outcome1,[200,120],30,"Black")
    canvas.draw_text("Score: "+str(score),[410,60],35,"Black")
    dealer_hand.draw(canvas,[100,170])
    canvas.draw_text("Player",[100,350],30,"Black")
    player_hand.draw(canvas,[100,400])
    canvas.draw_text(outcome,[210,350],30,"Black")
    

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
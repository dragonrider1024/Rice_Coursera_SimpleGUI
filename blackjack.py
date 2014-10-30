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
        #pass	# create Hand object
        self.handcardlist = []

    def __str__(self):
        #pass	# return a string representation of a hand
        handstring = "Hand contains "
        for card in self.handcardlist:
            handstring += str(card) + ' '
        return handstring            

    def add_card(self, card):
        #pass	# add a card object to a hand
        self.handcardlist.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        #pass	# compute the value of the hand, see Blackjack video
        value = 0
        hasAces = False
        for card in self.handcardlist:
            if card.get_rank() == 'A':
                hasAces = True
            value += VALUES[card.get_rank()]
        if hasAces and (value + 10) <= 21:
            value += 10
        return value
            
        
   
    def draw(self, canvas, pos):
        #pass	# draw a hand on the canvas, use the draw method for cards
        for i in range(len(self.handcardlist)):
            self.handcardlist[i].draw(canvas, [pos[0] + i * CARD_SIZE[0], pos[1]])
        
        
# define deck class 
class Deck:
    def __init__(self):
        #pass	# create a Deck object
        self.deckcardlist = []
        for suit in SUITS:
            for rank in RANKS:
                self.deckcardlist.append(Card(suit, rank))
        

    def shuffle(self):
        # shuffle the deck 
        #pass    # use random.shuffle()
        random.shuffle(self.deckcardlist)

    def deal_card(self):
        #pass	# deal a card object from the deck
        card = self.deckcardlist.pop()
        return card
    
    def __str__(self):
        #pass	# return a string representing the deck
        deckstring ="Deck contains "
        for card in self.deckcardlist:
            deckstring += str(card) + ' '
        return deckstring

# global object for deck and player/dealer hand.
objdeck = Deck()
playerhand = Hand()
dealerhand = Hand()
    
#define event handlers for buttons
def deal():
    global outcome, in_play, playerhand, dealerhand, score, objdeck

    if in_play:
        outcome = "New Deal?"
        print "Player lost, deal in play"
        in_play = False
        score -= 1
    # your code goes here
    else:
        in_play = True
        outcome = "Hit or Stand?"
        objdeck = Deck()
        objdeck.shuffle()
        playerhand = Hand()
        dealerhand = Hand()
        card1 = objdeck.deal_card()
        playerhand.add_card(card1)
        card2 = objdeck.deal_card()
        dealerhand.add_card(card2)
        card3 = objdeck.deal_card()
        playerhand.add_card(card3)
        card4 = objdeck.deal_card()
        dealerhand.add_card(card4)

def hit():
    #pass	# replace with your code below
 
    # if the hand is in play, hit the player
    global score, in_play, outcome
    if in_play and playerhand.get_value() <= 21:
        card = objdeck.deal_card()
        playerhand.add_card(card)
        if playerhand.get_value() > 21:
            outcome = "New Deal?"
            print "Player have busted"
            in_play = False
            score -= 1
        # if busted, assign a message to outcome, update in_play and score
        
       
def stand():
    #pass	# replace with your code below
    global score, outcome, in_play
    if playerhand.get_value() > 21:
        outcome = "New Deal?"
        print "Player have busted"
        in_play = False
    else:
        if in_play:
            while dealerhand.get_value() < 17:
                card = objdeck.deal_card()
                dealerhand.add_card(card)
            if dealerhand.get_value() > 21:
                outcome = "New Deal?"
                print "Dealer have busted"
                in_play = False
                score += 1
            else:
                if playerhand.get_value() <= dealerhand.get_value():
                    outcome = "New Deal?"
                    print "Dealer wins"
                    in_play = False
                    score -= 1
                else:
                    outcome = "New Deal?"
                    print "Player wins"
                    in_play = False
                    score += 1
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("BlackJack", [225, 50], 40, 'Red')
    canvas.draw_text(outcome, [250, 200], 20, 'Red')
    canvas.draw_text(str(score), [500, 100], 40, 'Red')
    #card = Card("S", "A")
    #card.draw(canvas, [300, 300])
    dealerhand.draw(canvas, [100, 250])
    playerhand.draw(canvas, [100, 350])
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_SIZE, [100 + CARD_CENTER[0], 250 + CARD_CENTER[1]], CARD_SIZE)
    


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

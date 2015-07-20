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
printis = ""

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
        self.hands = []        	# create Hand object
    def get_hands(self):
        return self.hands

    def __str__(self):
        ans = ""	# return a string representation of a hand
        for i in self.hands:
            ans += i.suit + i.rank + " "
        return "Hand Contains " + ans
    
    def add_card(self, card):
        self.hands.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        result = 0
        for i in self.hands:
            result += VALUES[i.rank]
        for i in self.hands:
            if "A" == i.rank:
                if result <= 11:
                    result += 10
        return result       
       
   
    def draw(self, canvas, pos):
        for i in self.hands:	# draw a hand on the canvas, use the draw method for card
            if self.hands.index(i) < 5:
                pos1 = [pos[0] + self.hands.index(i) * CARD_SIZE[0], pos[1]]
                i.draw(canvas, pos1)
 
    
        
# define deck class 
class Deck:
    def __init__(self):
        self.decks = []
        for i in SUITS:	# create a Deck object
            for j in RANKS:
                card = Card(i, j)
                self.decks.append(card)

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.decks)    # use random.shuffle()

    def deal_card(self):
        choosen_card = random.choice(self.decks)
        self.decks.remove(choosen_card)
        return choosen_card
    
    def __str__(self):
        ans = ""
        for i in self.decks:# return a string representing the deck
            ans += i.suit + i.rank + " "                   
        return "Deck contains " + ans	



#define event handlers for buttons
def deal():  
    global outcome, in_play, dealer, player, printis, score
    outcome = Deck()
    outcome.shuffle()
    dealer = Hand()
    player = Hand()
    dealer.add_card(outcome.deal_card())
    player.add_card(outcome.deal_card())
    dealer.add_card(outcome.deal_card())
    player.add_card(outcome.deal_card())
    printis = "Hit or stand?"
    # your code goes here
    if in_play == True:
        printis = "You loses! New deal?"
        in_play = False
        score -= 1
    in_play = True
    

def hit():
    # replace with your code below
    global dealer, player, outcome, in_play, printis, score
    # if the hand is in play, hit the player
    if player.get_value() <= 21:
        player.add_card(outcome.deal_card())
    # if busted, assign a message to outcome, update in_play and score
    if player.get_value() > 21 and in_play == True:
        print "You have busted"
        printis = "You have busted! New deal?"
        in_play = False
        score -= 1
def stand():
    # replace with your code below
    global dealer, player, outcome, in_play, printis, score
    if not in_play:
        print "You have busted"
        printis = "You have busted! New deal?"
        in_play = False
    else:
        while dealer.get_value() < 17:
            dealer.add_card(outcome.deal_card())
        if dealer.get_value() > 21:
            print "The dealer have busted"
            printis = "The dealer have busted! New deal?"
            score += 1
        elif dealer.get_value() >= player.get_value():
            print "The dealer wins"
            printis = "You loses! New deal?"
            score -= 1
        else:
            print "The player wins"
            printis = "You wins! New deal?"
            score += 1
        in_play = False
        
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    
    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    global dealer, player, in_play, printis, score
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text(printis,(20,25),24,"white")
    canvas.draw_text("Blackjack",(450,40),30,"red")
    canvas.draw_text("Score: " + str(score),(350,500),40,"yellow")
    #card = Card("S", "A")
    player.draw(canvas, [50,150])
    dealer.draw(canvas, [50,300])
    if in_play == True:
        card_loc = (CARD_CENTER[0] , CARD_CENTER[1] )
        canvas.draw_image(card_back, card_loc, CARD_SIZE, [50 + CARD_CENTER[0], 300 + CARD_CENTER[1]], CARD_SIZE)
        
  
    

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
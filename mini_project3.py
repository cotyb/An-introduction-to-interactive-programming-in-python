# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math


# helper function to start and restart the game
def new_game():
    range100()   
    


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    print "New game. Range is from 0 to 100" 
    global secret_number
    secret_number = random.randrange(0,100)
    global count
    count = 7
    print "Number of remaining guesses is 7\n"
    # remove this when you add your code    
    #pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    print "New game. Range is from 0 to 1000" 
    global secret_number
    secret_number = random.randrange(0,1000)
    global count
    count = 10
    print "Number of remaining guesses is 10\n"
    #pass
    
def input_guess(guess):
    # main game logic goes here	
    global count 
    count = count - 1
    guess = int(guess)
    print "Guess was %d" %guess
    print "Number of remaining guesses is %d" %count
    # remove this when you add your code
    if count == 0:
        print "You lose the game!\n"
        new_game()
    elif guess > secret_number:
        print "Lower!\n"
    elif guess < secret_number:
        print "Higher!\n"
    else:
        print "Correct!\n"
        new_game()

    
# create frame
frame = simplegui.create_frame("Guess the number",200,200,300)
frame.add_input("Enter a guess",input_guess,300)
# register event handlers for control elements and start frame
frame.add_button("Range:0-100",range100,300)
frame.add_button("Range:0-1000",range1000,300)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric

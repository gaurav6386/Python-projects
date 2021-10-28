import simplegui
import math
import random

HIGH_NUMBER=100
# helper function to start and restart the game
def new_game():
    '''
    We will initialize global variables used in our code 
    here
    '''
    global LOW_NUMBER,HIGH_NUMBER,n,secret_number
    LOW_NUMBER=0
    secret_number = random.randrange(LOW_NUMBER,HIGH_NUMBER)
    n = math.ceil(math.log((HIGH_NUMBER-LOW_NUMBER+1),2))
    print "New game. Range is ["+str(LOW_NUMBER)+","+str(HIGH_NUMBER)+")"
    print "Number of remaining guesses is ",n

# define event handlers for control panel
def range100():
    '''
    Event handler of button that changes the range to 
    [0,100) and starts a new game
    '''
    global HIGH_NUMBER
    HIGH_NUMBER = 100
    new_game()

def range1000():
    '''
    Event handler of button that changes the range to 
    [0,1000) and starts a new game
    '''
    global HIGH_NUMBER
    HIGH_NUMBER = 1000
    new_game()
    
def input_guess(guess):
    '''
    Main game logic goes here
    '''
    global secret_number,n
    n = n-1
    guess = int(guess)
    print "Guess was ",guess
    print "Number of remaining guesses is ",n
    if guess<secret_number:
        print "Higher"
    elif guess>secret_number:
        print "Lower"
    else:
        print "Correct!"
        print
        new_game()

# create frame
frame  = simplegui.create_frame("Guess the number", 300, 300)

# register event handlers for control elements and start frame
frame.add_button("Range[0,100]", range100)
frame.add_button("Range[0,1000]", range1000)
frame.add_input("Enter the Number", input_guess, 100)

# call new_game 
new_game()

# always remember to check your completed program against the grading rubric

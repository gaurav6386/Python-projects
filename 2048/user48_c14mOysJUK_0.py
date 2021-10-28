import random
# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    
    global number
    # convert name to number using if/elif/else
    if name.lower() == 'rock':
        number=0
    elif name.lower()=='spock':
        number=1
    elif name.lower()=='paper':
        number=2
    elif name.lower()=='lizard':
        number=3
    elif name.lower()=='scissors':
        number=4
    else:
        print "Invalid name!"
    # don't forget to return the result!
    return number

def number_to_name(number):
    # delete the following pass statement and fill in your code below
    global name
    
    # convert number to a name using if/elif/else
    if number==0:
        name='rock'
    elif number==1:
        name='spock'
    elif number==2:
        name='paper'
    elif number==3:
        name='lizard'
    elif number==4:
        name='scissors'
    else:
        print "Invalid Number"
    # don't forget to return the result!
    return name

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    global player_number
    # print out the message for the player's choice
    print "Player chooses "+player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number= name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number= random.randrange(0,5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice= number_to_name(comp_number)
    # print out the message for computer's choice
    print "Computer chooses "+comp_choice
    # compute difference of comp_number and player_number modulo five
    diff = (comp_number-player_number)%5
    # use if/elif/else to determine winner, print winner message
    if diff>0:
        if diff<3:
            print "Computer wins!"
        else:
            print "Player wins!"
    elif diff<0:
        if diff>-3:
            print "Player wins!"
        else:
            print "Computer wins!"
    else:
        print "Player and computer tie!"
            
    # print a blank line to separate consecutive games
    print
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric



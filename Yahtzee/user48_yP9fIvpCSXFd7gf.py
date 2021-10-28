"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
import random
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    sum_arr=[]
    if len(hand)>0:
        for values in set(hand):
            sum_arr.append(values*hand.count(values))  
        #print sum_arr
        return max(sum_arr)
    else:
        return 0

def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given 
    that there are num_free_dice to be rolled, each with
    num_die_sides.
    This function computes the expected value of the 
    scores for the possible Yahtzee hands that result from
    holding some dice and rolling the remaining free dice.
        
    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    
    new_roll_seq=list(gen_all_sequences([num+1 for num in range(num_die_sides)],num_free_dice))
    total_score=0.0
    for new_roll in new_roll_seq:
        total_score+=score(held_dice+new_roll)
    #print len(new_roll_seq)
    exp_value= total_score/len(new_roll_seq)
    
    return exp_value

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    
    all_holds=[()]
    for num in hand:
        temp_hold=[]
        temp_hold.append(num)
        temp_hold=tuple(temp_hold)
        all_holds.append(temp_hold)
    print all_holds
    
    def hold_set_append(all_holds):
        '''
        To generate all the possible hold_set where each
        element has pairing of more than one.
        '''
        temp_hold=[]
        for i_ndx in range(len(all_holds)):
            for j_ndx in range(i_ndx+1,len(all_holds)):
                temp_arr_1=list(all_holds[i_ndx])
                temp_arr_1.append(list(all_holds[j_ndx])[0])
                temp_hold.append(tuple(temp_arr_1))
                for k_ndx in range(j_ndx+1,len(all_holds)):
                    temp_arr_2=[num for num in temp_arr_1]
                    temp_arr_2.append(list(all_holds[k_ndx])[0])
                    temp_hold.append(tuple(temp_arr_2))
                    #print temp_arr_2
                    #print temp_hold
                    for l_ndx in range(k_ndx+1,len(all_holds)):
                        #print k+1,len(all_holds)
                        temp_arr_3=[num for num in temp_arr_2]
                        temp_arr_3.append(list(all_holds[l_ndx])[0])
                        temp_hold.append(tuple(temp_arr_3))
                        #print temp_arr_3
                        for m_ndx in range(l_ndx+1,len(all_holds)):
                            #print k+1,len(all_holds)
                            temp_arr_4=[num for num in temp_arr_3]
                            temp_arr_4.append(list(all_holds[m_ndx])[0])
                            temp_hold.append(tuple(temp_arr_4))
                            #print temp_arr_4   
                            for n_ndx in range(m_ndx+1,len(all_holds)):
                                temp_arr_5=[num for num in temp_arr_4]
                                temp_arr_5.append(list(all_holds[n_ndx])[0])
                                temp_hold.append(tuple(temp_arr_5))
                                #For increasing the range
#                                for p_ndx in range(n_ndx+1,len(all_holds)):
#                                    temp_arr_6=[num for num in temp_arr_5]
#                                    temp_arr_6.append(list(all_holds[p_ndx])[0])
#                                    temp_hold.append(tuple(temp_arr_6))
                                
        all_holds+=temp_hold
        return all_holds       
    all_holds= hold_set_append(all_holds)
    all_holds=set(all_holds)
    return all_holds


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    
    best_hold=()
    held_dice_set=gen_all_holds(hand)
    print len(held_dice_set),sorted(held_dice_set)
    max_score=0.0
    exp_score=0.0
    for held_dice in held_dice_set:
        num_free_dice=tuple([t for t in hand if t not in held_dice])
        exp_score=expected_value(held_dice,num_die_sides,len(num_free_dice))
        if max_score<exp_score:
            max_score=exp_score
            best_hold=held_dice    
    return (max_score, best_hold)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (2,3,4,5,6,6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
run_example()

#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
                                       
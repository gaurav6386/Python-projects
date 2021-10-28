"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1        # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.

def mc_trials(board, player):
    empty = provided.EMPTY
    win=0
    while empty:
        i=random.randint(0,2)
        j=random.randint(0,2)
        board.move(i, j, player)
        player= provided.switch_player(player)
        if board.check_win() != None:
            empty=0
        
      
        

def mc_update_scores(scores, board, player):
    if board.check_win()==provided.PLAYERX:
        for i in range(3):
            for j in range(3):
                if board.square(i,j)==provided.PLAYERX:
                    scores[i][j]=board.square(i,j)
                else:
                    scores[i][j]=-board.square(i,j)
    elif board.check_win()==provided.PLAYERO:
        for i in range(3):
            for j in range(3):
                if board.square(i,j)==provided.PLAYERXO:
                    scores[i][j]=board.square(i,j)
                else:
                    scores[i][j]=-board.square(i,j)
    
    elif board.check_win()==provided.DRAW:
        for i in range(3):
            for j in range(3):
                scores[i][j]=0
    else:
        return _
    

def get_best_move(board, score):
    pass

def mc_move(board, player, trials):
    print provided.DRAW
#    print provided.PLAYERX
#    print provided.PLAYERO
    print board
    print provided.EMPTY
    return [random.randint(0,2), random.randint(0,2)]
    

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

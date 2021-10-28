"""
Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move
"""
import random
import math

class SolitaireMancala:

    def __init__(self):
        self._store = [0]

    def set_board(self, configuration):
        self._store = configuration[:]

    def __str__(self):
        return str(self._store[::(-1)])

    def get_num_seeds(self, house_num):
        return self._store[house_num]

    def is_game_won(self):
        return (sum(self._store[1:]) == 0)

    def is_legal_move(self, house_num):
        return ((house_num == self._store[house_num]) and (house_num > 0))

    def apply_move(self, house_num):
        if self.is_legal_move(house_num):
            for index in range(house_num):
                self._store[index] += 1
            self._store[house_num] = 0

    def choose_move(self):
        move = 0
        for index in range((len(self._store) - 1)):
            if (self.is_legal_move((index + 1)) and (move == 0)):
                move = (index + 1)
        #print move
        return move

    def plan_moves(self):
        moves = []
        count = 0
        temp_store = self._store[:]
        while (count < 10):
            move = self.choose_move()
            if (move > 0):
                moves.append(move)
                self.apply_move(move)
            else:
                break
            count += 1
        self._store = temp_store[:]
        return moves    
    
    
import user48_ZgeepfBBEM_17 as poc_mancala_testsuite
poc_mancala_testsuite.run_suite(SolitaireMancala) 


# Import GUI code once you feel your code is correct
# import poc_mancala_gui
# poc_mancala_gui.run_gui(SolitaireMancala())

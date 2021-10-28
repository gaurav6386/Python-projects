"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def shift(line):
    """
    shift the non-zero elements of the line to left if 
    there zero is present in between
    """
    newlist =[]
    count=0
    for values in line:
        if values>0:
            newlist.append(values)
            count+=1
        
    for _ in range(count, len(line)):
        newlist.append(0)
    return newlist

def mergetiles(shifted_line):
    """
    merge the left shifted list
    """
    newline=[]
    count=0
    if len(shifted_line)==1:
        newline.append(shifted_line[0])
    else:
        index=1
        while index< len(shifted_line):
            if shifted_line[index-1]==shifted_line[index]:
                num = shifted_line[index-1]+shifted_line[index]
                count+=1
                index+=2    
            else:
                num =shifted_line[index-1]
                count+=1
                index+=1
            newline.append(num)
        #print count
        if index ==len(shifted_line):
            newline.append(shifted_line[index-1])
            count+=1
        
        for index in range(count,len(shifted_line)):
            newline.append(0)

    return newline

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    
    shifted_line= shift(line)
    merged_tiles= mergetiles(shifted_line)
    
    #print shifted_line
    
    return merged_tiles
    
    
class TwentyFortyEight:
    """
    Class to run the game logic.
    """
    def __init__(self, grid_height, grid_width):
        self._grid=[]
        self._row = grid_height
        self._col = grid_width
        self._initial_tiles ={UP: [(0,num_j) for num_j in range(self._col)],
                      DOWN: [(self._col-1,num_j) for num_j in range(self._col)],
                      LEFT:[(num_i,0) for num_i in range(self._row)],
                      RIGHT:[(num_i,self._col-1) for num_i in range(self._row)]}
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[ 0 for _ in range(self._col)]
                    for _ in range(self._row)]
        #create two random tiles on the new grid 
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        #string_grid=""
        #for num_i in range(self._row):
        #    string_grid += str(self._grid[num_i][0:self._col])+"\n" 
        
        return self._grid

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._row

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._col
    
    def move_up(self, iterate):
        """
        Move the tiles in upward direction
        """
        for (_,num_j) in iterate:
            temp=[]
            for num_k in range(self._row):
                temp.append(self._grid[num_k][num_j])
            temp = merge(temp)
            #print temp
            for num_k in range(self._row):
                self._grid[num_k][num_j]=temp[num_k]
        self.new_tile()
        
    def move_down(self,iterate):
        """
        MOves the tiles in Downward direction
        """
        for (_,num_j) in iterate:
            temp=[]
            for num_k in range(self._row):
                temp.append(self._grid[num_k][num_j])
            temp = temp[::-1]   #reverse the list
            temp = merge(temp)
            temp = temp[::-1]
            #print temp
            for num_k in range(self._row):
                self._grid[num_k][num_j]=temp[num_k]
        self.new_tile()
        
    def move_left(self, iterate):
        """
        Move the tile in Left direction
        """
        for (num_i,_) in iterate:
            temp=[]
            for num_k in range(self._col):
                temp.append(self._grid[num_i][num_k])
            temp = merge(temp)
            #print temp
            for num_k in range(self._col):
                self._grid[num_i][num_k]=temp[num_k]
        self.new_tile()
        
    def move_right(self, iterate):
        """
        Moves the tiles in Right direction
        """
        for (num_i,_) in iterate:
            temp=[]
            for num_k in range(self._col):
                temp.append(self._grid[num_i][num_k])
            temp = temp[::-1]
            temp = merge(temp)
            temp = temp[::-1]
            #print temp
            for num_k in range(self._col):
                self._grid[num_i][num_k]=temp[num_k]
        self.new_tile()
        
    
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        iterate = self._initial_tiles[direction]
        if direction==UP:
            self.move_up(iterate)
            
        elif direction==DOWN:
            self.move_down(iterate)
            
        elif direction==LEFT:
            self.move_left(iterate)
            
        elif direction==RIGHT:
            self.move_right(iterate)
            
            

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """        
        rand_list = [2]*90+[4]*10
        rand_i = random.randrange(0,self._row)
        rand_j = random.randrange(0,self._col)
        if self._grid[rand_i][rand_j]==0:
            self._grid[rand_i][rand_j]=random.choice(rand_list)
        else:
            self.new_tile()

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]

obj = TwentyFortyEight(5, 4)
poc_2048_gui.run_gui(obj)
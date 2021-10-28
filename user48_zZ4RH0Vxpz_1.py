"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    newlist =[]
    # replace with your code
    for values in line:
        if values>0:
            newlist.append(values)
        else:
            pass
    for i in range(0,len(list)-1):
        
        if newlist[i]==0:
            newlist.append(0)
    print newlist
    return []

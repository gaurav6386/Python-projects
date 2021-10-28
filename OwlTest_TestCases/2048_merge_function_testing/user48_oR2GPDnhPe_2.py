"""
Merge function for 2048 game.
"""
import poc_simpletest.py

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
        print count
        if index ==len(shifted_line):
            newline.append(shifted_line[index-1])
            count+=1
        
        for index in range(count,len(shifted_line)):
            newline.append(0)

    return newline

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    
    # replace with your code
    shifted_line= shift(line)
    merged_tiles= mergetiles(shifted_line)
    
    print shifted_line
    
    return merged_tiles
output = merge([8,4,4,2,2,8])
print output

#def run_suite():
#    suite= poc_simpletest.TestSuite()
#    for i in range(1,100):
#        line=[]
#        for j in range(0,i):
#            line.append(random.randrange(10))
#        ideal_funct=merge(line)
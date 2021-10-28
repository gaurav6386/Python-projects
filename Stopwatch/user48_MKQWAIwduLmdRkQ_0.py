# Testing template for format function in "Stopwatch - The game"
import math

###################################################
# Student should add code for the format function here
def format(num):
    d=num%10
    k=num%600
    c=((num%600-d)/10)%10
    b=(num%600-(num%600)%100)/100
    a=(num-num%600)/600
    return str(a) + ":" + str(b) + "" +str(c) + "." + str(d)    
#if we use print statement in the above function none will
#be printed after each output this is because there is two 
#print statement. first is inside the function and the
#second is outside the function. When function not returns
#it retirns none value.
        



###################################################
# Test code for the format function
# Note that function should always return a string with 
# six characters

                     
print format(0)
print format(7)
print format(17)
print format(60)
print format(63)
print format(214)
print format(599)
print format(600)
print format(602)
print format(667)
print format(1325)
print format(4567)
print format(5999)

###################################################
# Output from test

#0:00.0
#0:00.7
#0:01.7
#0:06.0
#0:06.3
#0:21.4
#0:59.9
#1:00.0
#1:00.2
#1:06.7
#2:12.5
#7:36.7
#9:59.9


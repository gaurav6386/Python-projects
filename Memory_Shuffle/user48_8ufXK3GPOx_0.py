# implementation of card game - Memory

import simplegui
import random
# helper function to initialize globals
def new_game():
    global list,exposed,state,temp_exposed_index,turn
    list1= [i for i in range(8)]
    list2= [i for i in range(8)]
    list= list1+list2
    state=0
    turn=0
    label.set_text("Turns = "+str(turn))
    temp_exposed_index=[]
    exposed=[False for i in range(16)]
    random.shuffle(list)
    
# FOR TESTING PURPOSE UNCOMMENT THE FOLLOWING LINE
#    print list

     
# define event handlers
def mouseclick(pos):
    global state, list, temp_exposed_index,turn
    count=0
    for i in range(16):
        if (not exposed[i]) and (pos[0]>50*i and pos[0]<50*i+50):
            if state ==0:
                turn=1
                state=1
                temp_exposed_index.append(i)
            elif state==1:
                state=2
                temp_exposed_index.append(i)
            else:
                turn+=1
                #UNCOMMENT FOR TESTING PURPOSE
                #print temp_exposed_index
                state=1
                if not (list[temp_exposed_index[0]]==list[temp_exposed_index[1]]):
                    #UNCOMMENT FOR TESTING PURPOSE
                    #print temp_exposed_index
                    exposed[temp_exposed_index[0]]=False
                    exposed[temp_exposed_index[1]]=False
                    temp_exposed_index.pop()
                    temp_exposed_index.pop()
                    temp_exposed_index.append(i)
                else:
                    temp_exposed_index.pop()
                    temp_exposed_index.pop()
                    temp_exposed_index.append(i)
            label.set_text("Turns = "+str(turn))
            #print i,state,list[i]
            exposed[i]=True
        if exposed[i]:
            count+=1
    if count==16:
        label.set_text("Congrats! You finished the puzzle in "+str(turn)+" turns.")
        
    
    
    
    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global list,exposed
    for i in range(16):
        if not exposed[i]:
            canvas.draw_polygon([[i*50,0],[i*50+50,0],[i*50+50,100],[i*50,100]],1,"Red","Green")
        else:
            canvas.draw_text(str(list[i]),[10+i*50,65],50,"White")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric
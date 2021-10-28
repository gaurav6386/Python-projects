#import required modules
import simplegui
import math

# define global variables
_num = 0
success_stop=0
total_stop=0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(_num):
    milli_sec=_num%10
    k=_num%600
    c=((_num%600-milli_sec)/10)%10
    b=(_num%600-(_num%600)%100)/100
    a=(_num-_num%600)/600
    return str(a) + ":" + str(b) + "" +str(c) + "." + str(milli_sec)


# define event handlers for buttons; "Start", "Stop", "Reset"
def start_timer():
    global timer
    timer.start()
    
def stop_timer():
    global timer,total_stop,success_stop
    if timer.is_running():
        total_stop+=1
        if _num%10==0:
            success_stop+=1
    timer.stop()
    
def reset_timer():
    global timer,_num,total_stop,success_stop
    timer.stop()
    _num=0
    total_stop=0
    success_stop=0
    format(_num)
    timer= simplegui.create_timer(100,timer_handler)
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global _num
    _num +=1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(_num),[100,170],40,'White')
    canvas.draw_text(str(success_stop)+"/"+str(total_stop),[250,30],25,'White')
    
# create frame
frame = simplegui.create_frame('Stopwatch',300,300)

# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, timer_handler)
frame.add_button('Start', start_timer)
frame.add_button('Stop', stop_timer)
frame.add_button('Reset',reset_timer)

# start frame
frame.start()

# Please remember to review the grading rubric

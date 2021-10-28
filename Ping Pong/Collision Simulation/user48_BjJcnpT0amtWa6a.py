# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor is tested to run in recent versions of
# Chrome, Firefox, Safari, and Edge.

import simplegui
WIDTH=600
HEIGHT=400
RADIUS=10

ball_pos=[10,20]
vel=[3,0.7]

# define event handler

def draw(canvas):
    ball_pos[0]+=vel[0]
    ball_pos[1]+=vel[1]
 
    canvas.draw_polygon([(50,50),(180,50),(180,140),(50,140)],2,"Yellow","White")
    canvas.draw_circle(ball_pos,RADIUS,1, "Red","White")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("collision_simulation", WIDTH,HEIGHT)

#register event handler

#frame.set_keyup_handler(key)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()

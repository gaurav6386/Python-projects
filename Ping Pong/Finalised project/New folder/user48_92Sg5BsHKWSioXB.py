# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 900
HEIGHT = 700       
BALL_RADIUS = 20
PAD_WIDTH = 15
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos=[WIDTH/2,HEIGHT/2]
    if direction:
        ball_vel=[random.randrange(3, 6),-random.randrange(1, 3)]
    else:
        ball_vel=[-random.randrange(3, 6),-random.randrange(1, 3)]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(LEFT)
    score1=0
    score2=0
    paddle1_pos=[HALF_PAD_WIDTH,HEIGHT/2]
    paddle2_pos=[WIDTH-HALF_PAD_WIDTH,HEIGHT/2]
    paddle1_vel=0
    paddle2_vel=0    
    
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos, ball_vel
            
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]
    if ball_pos[1]<BALL_RADIUS:
        ball_vel[1]=-ball_vel[1]
    elif ball_pos[1]>HEIGHT-BALL_RADIUS:
        ball_vel[1]=-ball_vel[1]
    
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1,"Red","White")
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[1]+paddle1_vel>PAD_HEIGHT/2 and paddle1_pos[1]+paddle1_vel<HEIGHT-PAD_HEIGHT/2:
        paddle1_pos[1]+=paddle1_vel
    if paddle2_pos[1]+paddle2_vel>PAD_HEIGHT/2 and paddle2_pos[1]+paddle2_vel<HEIGHT-PAD_HEIGHT/2:
        paddle2_pos[1]+=paddle2_vel
    
    # draw paddles
    canvas.draw_polyline([(PAD_WIDTH/2+2,paddle1_pos[1]-PAD_HEIGHT/2),(PAD_WIDTH/2+2,paddle1_pos[1]+PAD_HEIGHT/2)],PAD_WIDTH-2, "White")
    canvas.draw_polyline([(WIDTH-PAD_WIDTH/2-2,paddle2_pos[1]-PAD_HEIGHT/2),(WIDTH-PAD_WIDTH/2-2,paddle2_pos[1]+PAD_HEIGHT/2)],PAD_WIDTH-2, "White")
    
    # determine whether paddle and ball collide
    #Condition for hitting the ball with paddle1
    if ball_pos[0]<=(BALL_RADIUS+PAD_WIDTH) and abs(paddle1_pos[1]-ball_pos[1])<(PAD_HEIGHT/2+BALL_RADIUS):
        ball_vel[0]=-ball_vel[0]
        ball_vel[0]=1.1*ball_vel[0]
        ball_vel[1]=1.1*ball_vel[1]
    elif ball_pos[0]<=(BALL_RADIUS+PAD_WIDTH) and not(abs(paddle1_pos[1]-ball_pos[1])<PAD_HEIGHT/2+BALL_RADIUS):
        score2+=1
        spawn_ball(RIGHT)
    #condition for hitting the ball with paddle2
    if ball_pos[0]>=WIDTH-BALL_RADIUS-PAD_WIDTH and (abs(paddle2_pos[1]-ball_pos[1])<PAD_HEIGHT/2+BALL_RADIUS):
        ball_vel[0]=-ball_vel[0]
        ball_vel[0]=1.1*ball_vel[0]
        ball_vel[1]=1.1*ball_vel[1]
    elif ball_pos[0]>=WIDTH-BALL_RADIUS-PAD_WIDTH and not(abs(paddle2_pos[1]-ball_pos[1])<PAD_HEIGHT/2+BALL_RADIUS):
        score1+=1
        spawn_ball(LEFT)
    
    # draw scores
    canvas.draw_text(str(score1), [WIDTH/4, 80], 60,"White")
    canvas.draw_text(str(score2), [3*WIDTH/4, 80], 60,"White")
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    _vel=10
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel-=_vel
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel+=_vel
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel-=_vel
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel+=_vel
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    _vel=10
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel+=_vel
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel-=_vel
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel+=_vel
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel-=_vel

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.add_button("Restart",new_game)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()

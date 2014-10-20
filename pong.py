# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]
score1 = 0
score2 = 0
paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
paddle_vel = 5
paddle1_vel = 0
paddle2_vel = 0
keydown1 = False
keyup1 = False
keydown2 = False
keyup2 = False

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == RIGHT:
        ball_vel[0] = random.randrange(120,240) / 60
        ball_vel[1] = - random.randrange(60, 180) / 60
    elif direction == LEFT:
        ball_vel[0] = - random.randrange(120,240) / 60
        ball_vel[1] = - random.randrange(60, 180) / 60

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    spawn_ball(RIGHT)
    
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH or ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if paddle1_pos < ball_pos[1] < paddle1_pos + PAD_HEIGHT and ball_vel[0] < 0:
            ball_vel[0] *= -1.1
            ball_vel[1] *= 1.1
        elif paddle2_pos < ball_pos[1] < paddle2_pos + PAD_HEIGHT and ball_vel[0] > 0:
            ball_vel[0] *= -1.1
            ball_vel[1] *= 1.1
        else:
            if ball_vel[0] > 0:
                score1 += 1
            else:
                score2 += 1
            spawn_ball(ball_vel[0] < 0)
    
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
            
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos <= HEIGHT - PAD_HEIGHT and paddle1_vel > 0) or (paddle1_pos >= 0 and paddle1_vel < 0) :
        paddle1_pos += paddle1_vel    
    elif (paddle2_pos <= HEIGHT - PAD_HEIGHT and paddle2_vel > 0) or (paddle2_pos >= 0 and paddle2_vel < 0) :
        paddle2_pos += paddle2_vel 
    
    # draw paddles
    c.draw_polygon([[0, paddle1_pos], [PAD_WIDTH, paddle1_pos],[PAD_WIDTH, paddle1_pos + PAD_HEIGHT ],[0, paddle1_pos + PAD_HEIGHT]],1, "White", "White") 
    c.draw_polygon([[WIDTH, paddle2_pos], [WIDTH - PAD_WIDTH, paddle2_pos], [WIDTH - PAD_WIDTH, paddle2_pos + PAD_HEIGHT], [WIDTH, paddle2_pos + PAD_HEIGHT]],1, "White", "White")
    
    # draw scores
    c.draw_text(str(score1), [250, 80], 40, "Green")    
    c.draw_text(str(score2), [WIDTH - 270, 80], 40, "Green")  
        
def keydown(key):
    global paddle1_vel, paddle2_vel, keydown1, keydown2, keyup1, keyup2
    
    if key == simplegui.KEY_MAP["down"]:
        keydown2 = True
        paddle2_vel = paddle_vel    
    elif key == simplegui.KEY_MAP["up"]:
        keyup2 = True
        paddle2_vel = -paddle_vel  
        
    if key == simplegui.KEY_MAP["w"]:
        keyup1 = True
        paddle1_vel = -paddle_vel     
    elif key == simplegui.KEY_MAP["s"]:
        keydown1 = True
        paddle1_vel = paddle_vel 
   
def keyup(key):
    global paddle1_vel, paddle2_vel, keydown1, keydown2, keyup1, keyup2
    
    if key == simplegui.KEY_MAP["down"]:
        if keydown2 == True: 
            keydown2 = False
            paddle2_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        if keyup2 == True:
            keyup2 = False
            paddle2_vel = 0
            
    elif key == simplegui.KEY_MAP["w"]:
        if keyup1 == True:
            keyup1 = False
            paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        if keydown1 == True: 
            keyup1 = False
            paddle1_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)

# start frame
new_game()
frame.start()

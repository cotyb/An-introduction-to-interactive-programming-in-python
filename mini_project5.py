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


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    horizontal = random.randrange(12, 24)
    vertical = random.randrange(6, 18)
    if direction == RIGHT:
        ball_vel = [horizontal / 10, -vertical /10]
    
    if direction == LEFT:
        ball_vel = [-horizontal / 10, -vertical / 10]


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = [HALF_PAD_WIDTH, HEIGHT / 2]
    paddle2_pos = [WIDTH - 1 - HALF_PAD_WIDTH, HEIGHT / 2]
    paddle1_vel = [0, 0]
    paddle2_vel = [0, 0]
    score1 = 0
    score2 = 0
    spawn_ball(1)

def draw(canvas):
    
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
   
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1] < BALL_RADIUS or ball_pos[1] > HEIGHT - 1 - BALL_RADIUS:
        ball_vel[0] = ball_vel[0]
        ball_vel[1] = -ball_vel[1]
    # draw ball
    canvas.draw_circle((ball_pos[0], ball_pos[1]), BALL_RADIUS, 1, "White","White")
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[1] + paddle1_vel[1] > HALF_PAD_HEIGHT and paddle1_pos[1]  + paddle1_vel[1] < HEIGHT - 1 - HALF_PAD_HEIGHT:
        paddle1_pos[1] += paddle1_vel[1]
    
    if paddle2_pos[1] + paddle2_vel[1] > HALF_PAD_HEIGHT and paddle2_pos[1] + paddle2_vel[1] < HEIGHT - 1 - HALF_PAD_HEIGHT:
        paddle2_pos[1] += paddle2_vel[1]
    
    
    # draw paddles
    point1_1 = (paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT)
    point1_2 = (paddle1_pos[0] + HALF_PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT)
    point1_3 = (paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT)
    point1_4 = (paddle1_pos[0] + HALF_PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT)
    point2_1 = (paddle2_pos[0] - HALF_PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT)
    point2_2 = (paddle2_pos[0] + HALF_PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT)
    point2_3 = (paddle2_pos[0] - HALF_PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT)
    point2_4 = (paddle2_pos[0] + HALF_PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT)
    canvas.draw_polygon([point1_1, point1_2, point1_4, point1_3], 1, "white", "white")
    canvas.draw_polygon([point2_1, point2_2, point2_4, point2_3], 1, "white", "white")
    # determine whether paddle and ball collide  
    if ball_pos[0] < BALL_RADIUS + PAD_WIDTH:
        if ball_pos[1] <= paddle1_pos[1] + HALF_PAD_HEIGHT and ball_pos[1] >= paddle1_pos[1] - HALF_PAD_HEIGHT:
            ball_vel[0] = -(ball_vel[0] * 1.1)
        else:
            spawn_ball(RIGHT)
            score2 += 1
    elif ball_pos[0] > WIDTH - 1 - BALL_RADIUS - PAD_WIDTH:
        if ball_pos[1] <= paddle2_pos[1] + HALF_PAD_HEIGHT and ball_pos[1] >= paddle2_pos[1] - HALF_PAD_HEIGHT:
            ball_vel[0] = -(ball_vel[0] * 1.1)
        else:
            spawn_ball(LEFT)
            score1 += 1
    # draw scores
    canvas.draw_text(str(score1),(150,50),50,"Red")
    canvas.draw_text(str(score2),(450,50),50,"Red")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel[1] = -2
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel[1] = 2
    elif key == simplegui.KEY_MAP["s" and "w"]:
        paddle1_vel[1] = 0
   
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] = -2
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = 2
    elif key == simplegui.KEY_MAP["up" and "down"]:
        paddle2_vel[1] = 0
        
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel[1] = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel[1] = 0
    elif key == simplegui.KEY_MAP["s" and "w"]:
        paddle1_vel[1] = 0
        
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = 0
    elif key == simplegui.KEY_MAP["up" and "down"]:
        paddle2_vel[1] = 0

def button_handler():
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button = frame.add_button("Restart", button_handler, 100)


# start frame
new_game()
frame.start()


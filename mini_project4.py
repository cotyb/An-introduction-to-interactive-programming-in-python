# template for "Stopwatch: The Game"
import simplegui
# define global variables
current_time = 0
total_count = 0
hit_count = 0
is_running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global d
    a = t / 600
    b = t % 600 / 100
    c = t % 600 % 100 / 10
    d = t % 600 % 100 % 10
    return str(a) + ":" + str(b) + str(c) + "." + str(d)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start_handler():
    timer.start()
    global is_running
    is_running = True
    
    

def Stop_handler():
    timer.stop()
    global d, hit_count, total_count, is_running
    if is_running:
        total_count += 1
        if d == 0:
            hit_count += 1
        
    is_running = False

def Reset_handler():
    global current_time, hit_count, total_count, is_running
    timer.stop()
    is_running = False
    hit_count = 0
    total_count = 0
    current_time = 0
    

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global current_time
    current_time += 1
    print current_time

# define draw handler
def draw_handler(canvas):
    global current_time, hit_count, total_count
    canvas.draw_text(format(current_time),(70,120),60,"red")
    canvas.draw_text(str(hit_count) + "/" +str(total_count),(15,40),30,"red")
    
    
# create frame
frame = simplegui.create_frame("Stopwatch",300,200)
button1 = frame.add_button("Start",Start_handler,200)
button2 = frame.add_button("Stop",Stop_handler,200)
button3 = frame.add_button("Reset",Reset_handler,200)

timer = simplegui.create_timer(100,timer_handler)

frame.set_draw_handler(draw_handler)
# register event handlers


# start frame
frame.start()

# Please remember to review the grading rubric

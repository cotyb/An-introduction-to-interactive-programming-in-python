# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global cards_list, exposed_list, state, count
    count = 0
    state = 0
    cards_list1 = []
    exposed_list = []
    for i in range(8):
        cards_list1.append(random.randrange(0,8))
        exposed_list.append(False)
        exposed_list.append(False)
    cards_list = cards_list1 + cards_list1
    random.shuffle(cards_list)
    

     
# define event handlers
def mouseclick(pos):
    global count
    count += 1
    # add game state logic here
    global state, click_index1, click_index2
    if state == 0:
        if pos[1] >= 0 and pos[1] <=100:
            click_index1 = pos[0] / 50
            exposed_list[click_index1] = True
        state = 1
    elif state == 1:
        if pos[1] >= 0 and pos[1] <=100:
            click_index2 = pos[0] / 50
            exposed_list[click_index2] = True
        state = 2
    elif state == 2:
        if cards_list[click_index1] != cards_list[click_index2]:
            exposed_list[click_index1] = False
            exposed_list[click_index2] = False
            state = 1
            click_index1 = pos[0] / 50
            exposed_list[click_index1] = True
        else:
            state = 1
            click_index1 = pos[0] / 50
            exposed_list[click_index1] = True
       
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cards_list, exposed_list, count
    for i in range(16):
        if exposed_list[i] == True:
            canvas.draw_text(str(cards_list[i]),(18 + 50*i,60),36,"Red")
        else:
            canvas.draw_polygon([(i*50,0),(i*50,100),(i*50+50,100),(i*50+50,0)],2,"Black","Green")
    label.set_text("Turns = %d" %count)

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
# implementation of card game - Memory

import simplegui
import random

card = range(0, 8) * 2
exposed = [False for x in range(len(card))]
card_width = 0
half_card_width = 0
card_height = 0
half_card_height = 0
state = 0
prev_index = 0
prevprev_index = 0
turns = 0
counter = 0

# helper function to initialize globals
def new_game():
    global card, card_width, card_height, half_card_width, half_card_height, turns, counter, state
    random.shuffle(card)
    l = len(card)
    for i in range(l):
        exposed[i] = False
    card_width = 800 / l
    card_height = 100
    half_card_width = card_width / 2
    half_card_height = card_height / 2
    turns = 0
    counter = 0
    state = 0
    label.set_text("Turns = "+ str(turns))
#    pass  

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, prev_index, prevprev_index, counter, turns
    if pos[0] > 0 and pos[0] < 800 and pos[1] >0 and pos[1] < 100:
        k = int (pos[0] / card_width)
        if not exposed[k]:
            exposed[k] = True
            counter += 1
            turns = counter / 2
            label.set_text("Turns = " + str(turns))
            
            if state == 2:
                if card[prev_index] != card[prevprev_index]:
                    exposed[prev_index] = False
                    exposed[prevprev_index] = False
                
            if state == 0:
                state = 1
                prev_index = k
            elif state == 1:
                state = 2
                prevprev_index = prev_index
                prev_index = k
            else:
                state = 1
                prev_index = k
                    
    
#    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    l = len(card)
    for i in range(l):
        if exposed[i]:
            canvas.draw_text(str(card[i]), [card_width * i + half_card_width - 12, half_card_height + 12], 50, 'White')
        else:
            canvas.draw_polygon([(card_width * i, 0), (card_width * (i + 1), 0), (card_width * (i + 1), card_height), (card_width * i, card_height)], 1, 'Yellow', 'Green')
#    pass


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

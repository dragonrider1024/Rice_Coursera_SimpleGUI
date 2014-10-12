# template for "Stopwatch: The Game"
import simplegui
# define global variables

time = 0
x = 0
y = 0
isrunning = False


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

def format(t):
    da = t / 600
    tmpbc = t % 600
    dbc = tmpbc / 10
    dd = tmpbc % 10
    a = str(da)
    d= str(dd)
    if dbc < 10:
        bc = '0' + str(dbc)
    else:
        bc = str(dbc)
    return a + ':' + bc + '.' + d

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button_handler():
    global isrunning
    timer.start()
    isrunning = True
    
    
def stop_button_handler():
    global x, y, isrunning
    if isrunning:
        if time % 10 ==0:
            x += 1
        y += 1
    timer.stop()
    isrunning = False
    
    
def reset_button_handler():
    timer.stop()
    global time, x, y, isrunning
    time = 0
    isrunning = False
    x = 0
    y = 0
    
    

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 1


# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(time), [130,150], 30, 'White')
    canvas.draw_text(str(x)+'/'+str(y), [250,40],30, 'White')
    
# create frame
frame = simplegui.create_frame("Stopwatch", 300,300)

# register event handlers
timer = simplegui.create_timer(100,timer_handler)
frame.set_draw_handler(draw_handler)
frame.add_button('Start', start_button_handler)
frame.add_button('Stop', stop_button_handler)
frame.add_button('Reset', reset_button_handler)

# start frame
frame.start()


# Please remember to review the grading rubric


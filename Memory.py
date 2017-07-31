# implementation of card game - Memory

import simplegui
import random

MEMORY=range(1,9)*2
random.shuffle(MEMORY)
point=[900,900]
exposed=[False]*16
state=0
turns=0
# helper function to initialize globals
def new_game():
    global exposed,turns
    exposed=[False]*16
    state=turns=0	

# define event handlers
def mouseclick(pos):
    # add game state logic here
    global point,exposed,state,card1,card2,index_1,index_2,turns
    
    point=pos
    x=point[0]/50
    
    if exposed[x]==False:
        
        if state==0:
            exposed[x]=True
            card1=MEMORY[x]
            index_1=x
            state=1
            
        elif state==1:
            exposed[x]=True
            card2=MEMORY[x]
            index_2=x
            state=2
            
        else :
            
            if card2!=card1:
                exposed[index_1]=False
                exposed[index_2]=False
                
            exposed[x]=True
            card1=MEMORY[x]
            index_1=x
                
            state=1
            turns+=1
            label.set_text("Turns= "+str(turns))
            
            
# cards are logically 50x100 pixels in size    
def draw(canvas):
    x=point[0]/50
    
    for x in range(0,16):
        if exposed[x]:
            canvas.draw_text(str(MEMORY[x]),(50*x,80),100,'White')
        else:
            canvas.draw_polygon([(0+50*x, 0), (50+50*x, 0), (50+50*x, 100),(0+50*x,100)], 5, 'Black', 'Green')
        
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


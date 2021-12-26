# Tamsin Rogers
# CS 152
# October 30, 2019
# Lab 8
# Exploring Zelle graphics


import graphicsPlus as gr
import time
import random

def test1():
	#create a GraphWin window
	win = gr.GraphWin("test window", 500, 500, False)
	
	#wait for a mouse click
	pos = win.getMouse()
	print(pos)
	print(pos.getX(), pos.getY())
	#close the window
	win.close()
	
#draw a circle whenever the user clicks in the window
def test2():

	#create a window
	win = gr.GraphWin("test window 2", 500, 500, False)
	
	#create a list to store the circles
	shapes = []
	
	#a forever loop
	while True:
		
		#see if the user has clicked
		click = win.checkMouse()
		if click != None:
			print(click)
			c = gr.Circle(click, 10)
			c.setFill(gr.color_rgb(random.randint(0,255), random.randint(0,255), random.randint(0,255),))
			shapes.append(c)
			c.draw(win)
		
		key = win.checkKey()
		if key == "q":
			break
		
		for item in shapes:
			item.move(random.randint(-5,5), random.randint(-5,5))
			
		time.sleep(0.033) #30 loops per second
		win.update() #call the update function
		
	win.close()
	
if __name__ == "__main__":
	test2()
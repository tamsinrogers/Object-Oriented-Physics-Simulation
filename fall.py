# template written by Bruce A. Maxwell
# updated by Tamsin Rogers
# November4, 2019
# CS 152 
# Project 8: Object-Oriented Physics Simulation
# run this program from the Terminal by entering "python3 collisions.py"
# this program creates a simulation in which a ball falls and collides with blocks

#import the graphicsPlus, random, and time packages, and the physics_objects file, which contains the class definitions
import graphicsPlus as gr
import physics_objects as pho
import random
import time

"""The main function simulates a ball object falling down the screen and then respawning at the center point"""
#main function for implementing the test code
def main():
    win = gr.GraphWin("Falling", 500, 500, False)                   # create a graphics window
    ball = pho.Ball(win)                                            # create a ball
    ball.setPosition(25, 25)                                        # move the ball to the center of the screen
    ball.setVelocity((random.randint(0,10)), random.randint(0,10))  # give the ball a random velocity
    ball.setAcceleration(0,-20)                                     # set the acceleration to (0, -20)
    ball.update(.01)                                                #update the ball using the update function 
    ball.draw()                                                     #draw the ball
    
    #draw the bottom row of blocks
    block = pho.Block( win, dx = 6, dy = 3 )                        
    block.setPosition(0, 1)                                       
    block.draw()
    block2 = pho.Block( win, dx = 6, dy = 3 )
    block2.setPosition(6, 1)
    block2.draw()
    block3 = pho.Block( win, dx = 6, dy = 3 )
    block3.setPosition(12, 1)
    block3.draw()
    block4 = pho.Block( win, dx = 6, dy = 3 )
    block4.setPosition(18, 1)
    block4.draw()
    block5 = pho.Block( win, dx = 6, dy = 3 )
    block5.setPosition(24, 1)
    block5.draw()
    block6 = pho.Block( win, dx = 6, dy = 3 )
    block6.setPosition(30, 1)
    block6.draw()
    block7 = pho.Block( win, dx = 6, dy = 3 )
    block7.setPosition(36, 1)
    block7.draw()
    block8 = pho.Block( win, dx = 6, dy = 3 )
    block8.setPosition(42, 1)
    block8.draw()
    block9 = pho.Block( win, dx = 6, dy = 3 )
    block9.setPosition(48, 1)
    block9.draw()
    
    #create a list of the blocks blocks
    wall = [block, block2, block3, block4, block5, block6, block7, block8, block9]

    #assign the variable key to the built in checkKey function
    key = win.checkKey()
     
    #initialize a green "Clear" textbox
    textbox = gr.Text( gr.Point( 250, 100 ), "Clear" )
    textbox.draw(win)                          

    while True:
        ball.update(0.033)                                                      #call the ball's update method with a dt of 0.033
        time.sleep( 0.033 )                                                     #have the animation go at the same speed
        key = win.checkKey()
        if win.checkMouse():                                                    #if the user clicked the mouse, exit the window
            break       
        if ball.getPosition()[0] > win.getWidth() or ball.getPosition()[1] < 0: #if the ball is outside the window
            ball.setPosition(25, 25)                                            #reposition the ball to the center of the window
            ball.setVelocity(random.randint(0,10), random.randint(0,10))        #give the ball a random velocity
            ball.update(.01)
        for i in wall:                                                          #for each of the wall blocks
            if i.collision(ball):                                               #if the ball collides with a block
                i.undraw()     
                textbox.setText("Collision!")                                   #flash a "Collision!" textbox                                        #undraw that block
                ball.setPosition(25,25)                                         #reset the ball's position and velocity
                ball.setVelocity(random.randint(0,10), random.randint(0,10))
                time.sleep( 0.06 )
                ball.update(.01)
                win.update()
                time.sleep( 0.2 )
                
            else:                                                               #if no collision is happening
                textbox.setText("Clear")                                        #keep the "Clear" textbox
        win.update()    
               
    win.close()                                                                 #close the window

if __name__ == "__main__":
    main()
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
    ball.randomcolor()                                              #fill the ball by running the randomcolor function
    ball.update(.01)                                                #update the ball using the update function 
    ball.draw()                                                     #draw the ball
    
    win.setBackground("lightcyan")									#set the color of the background of the window to light cyan
    
    #draw the bottom row of blocks and color them grey
    block = pho.Block( win, dx = 6, dy = 3 )                        
    block.setPosition(0, 1)
    block.blockcolor()                                              
    block.draw()
    block2 = pho.Block( win, dx = 6, dy = 3 )
    block2.setPosition(6, 1)
    block2.blockcolor()
    block2.draw()
    block3 = pho.Block( win, dx = 6, dy = 3 )
    block3.setPosition(12, 1)
    block3.blockcolor()
    block3.draw()
    block4 = pho.Block( win, dx = 6, dy = 3 )
    block4.setPosition(18, 1)
    block4.blockcolor()
    block4.draw()
    block5 = pho.Block( win, dx = 6, dy = 3 )
    block5.setPosition(24, 1)
    block5.blockcolor()
    block5.draw()
    block6 = pho.Block( win, dx = 6, dy = 3 )
    block6.setPosition(30, 1)
    block6.blockcolor()
    block6.draw()
    block7 = pho.Block( win, dx = 6, dy = 3 )
    block7.setPosition(36, 1)
    block7.blockcolor()
    block7.draw()
    block8 = pho.Block( win, dx = 6, dy = 3 )
    block8.setPosition(42, 1)
    block8.blockcolor()
    block8.draw()
    block9 = pho.Block( win, dx = 6, dy = 3 )
    block9.setPosition(48, 1)
    block9.blockcolor()
    block9.draw()
    
    #create a list of the blocks blocks
    wall = [block, block2, block3, block4, block5, block6, block7, block8, block9]
    
    #create instructional text boxes
    textbox3 = gr.Text( gr.Point( 250, 50 ), "Project 8" )
    textbox3.setSize(30)
    textbox3.draw(win)
    textbox4 = gr.Text( gr.Point( 100, 225 ), "Press the left arrow to move left" )
    textbox4.setSize(12)
    textbox4.draw(win)
    textbox5 = gr.Text( gr.Point( 400, 225 ), "Press the right arrow to move right" )
    textbox5.setSize(12)
    textbox5.draw(win)
    textbox6 = gr.Text( gr.Point( 250, 300 ), "Press space to set \n the color of the ball") 
    textbox6.setSize(12)
    textbox6.draw(win)

    #assign the variable key to the built in checkKey function
    key = win.checkKey()
     
    #initialize a green "Clear" textbox
    textbox = gr.Text( gr.Point( 250, 100 ), "Clear" )
    textbox.setTextColor("green")
    textbox.setStyle('bold')
    textbox.setSize(30)
    textbox.draw(win)

    flickering = True   #set the flickering flag to True
    collisions = 0      #start the number of collisions at 0                                    

    while True:
        ball.update(0.033)                                                      #call the ball's update method with a dt of 0.033
        time.sleep( 0.033 )                                                     #have the animation go at the same speed
        key = win.checkKey()
        if win.checkMouse():                                                    #if the user clicked the mouse, exit the window
            break
        if key == 'Left':                                                       #if the user clicked the left arrow button, move the ball to the left
            ball.moveLeft()
        if key == 'Right':                                                      #if the user clicked the right arrow button, move the ball to the right
            ball.moveRight()                
        if ball.getPosition()[0] > win.getWidth() or ball.getPosition()[1] < 0: #if the ball is outside the window
            ball.setPosition(25, 25)                                            #reposition the ball to the center of the window
            ball.setVelocity(random.randint(0,10), random.randint(0,10))        #give the ball a random velocity
            ball.update(.01)
        if key == 'space':                                                      #if the user clicked the space key
            flickering = False                                                  #set the flickering flag to False
        if flickering:                                                          #if the flickering flag is true
            ball.randomcolor()                                                  #keep calling the randomcolor function for the ball
        for i in wall:                                                          #for each of the wall blocks
            if i.collision(ball):                                               #if the ball collides with a block
                i.redblock()                                                    #flash a red block
                win.update()
                time.sleep( 0.2 )
                i.undraw()                                                      #undraw that block
                ball.setPosition(25,25)                                         #reset the ball's position and velocity
                ball.setVelocity(random.randint(0,10), random.randint(0,10))
                time.sleep( 0.06 )
                ball.update(.01)
                textbox.setText("Collision!")                                   #flash a red "Collision!" textbox
                textbox.setTextColor("red")
                win.update()
                time.sleep( 0.2 )
                collisions = collisions+1
                
            else:                                                               #if no collision is happening
                textbox.setText("Clear")                                        #keep the green "Clear" textbox
                textbox.setTextColor("green")
        win.update()    
        if collisions > 10:                                                     #if the ball has collided with all of the blocks in the wall
            ball.undraw()                                                       #undraw the ball
            textbox.undraw()                                                    #undraw the instructional textboxes
            textbox3.undraw()
            textbox4.undraw()
            textbox5.undraw()
            textbox6.undraw()
            gameover = gr.Text( gr.Point( 250, 400 ), "YOU WIN!" )              #display a "YOU WIN!" textbox
            gameover.setTextColor("black")
            gameover.setStyle('bold')
            gameover.setSize(30)
            gameover.draw(win)
            win.update()
            time.sleep( 0.2 )                  
        win.update()                                      
    win.close()                                                                 #close the window

if __name__ == "__main__":
    main()
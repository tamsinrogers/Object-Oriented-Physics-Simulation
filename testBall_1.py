# Bruce A. Maxwell
# Fall 2015
# CS 151S Project 8
#
# Physics simulation project
# Test file for the Ball class
#
# modified Spring '19 by Eric Aaron

# test the get/set methods
# test the setPosition method
#
import graphicsPlus as gr
import physics_objects as pho
import time
import random

def main():

    # create a GraphWin
    win = gr.GraphWin( "Ball test", 500, 500, False)

    # create a default Ball object and draw it into the window
    ball = pho.Ball(win)
    
    p = ball.getPosition()
    print( 'Position: ', p[0], p[1])
    ball.setPosition(30,30)
    p = ball.getPosition()
    print("New Position: ", p[0], p[1])

    v = ball.getVelocity()
    print( 'Velocity: ', v[0], v[1])
    ball.setVelocity( 10, 10 )
    v = ball.getVelocity()
    print( 'New Velocity: ', v[0], v[1])

    ## add other get/set test cases here ##
    
    m = ball.getMass()
    print("Mass: ", m)
    ball.setMass(20)
    m = ball.getMass()
    print("New Mass: ", m)
    
    """r = ball.getRadius()
    print("Radius: ", r)
    ball.setRadius(20)
    r = ball.getRadius()
    print("New Radius: ", r)"""
    
    a = ball.getAcceleration()
    print("Acceleration: ", a[0], a[1])
    ball.setAcceleration(10,10)
    a = ball.getAcceleration()
    print("New Acceleration: ", a[0], a[1])

    
    
    ball.draw()

    #add some motion here.   Uncomment the code below to make it run
    dt = 0.1
    while win.checkMouse() == None:
        ball.update(dt)
        time.sleep(dt)
        ball.setVelocity( random.randint(-10,10), random.randint(-10,10) )
        win.update()

    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
    
    
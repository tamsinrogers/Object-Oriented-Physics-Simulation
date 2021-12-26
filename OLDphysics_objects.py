import graphicsPlus as gr
import random
import time

class Ball:

    """This function initializes the attributes of the ball object.  Self and win are the 
    only non optional arguments."""
    def __init__(self, win, mass=1, radius=1.5):
        
        self.mass = mass
        self.radius = radius
        self.position = [0,0]
        self.velocity = [0,0]
        self.acceleration = [0,0]
        self.win = win
        self.scale = 10
        self.vis = [ gr.Circle( gr.Point(self.position[0]*self.scale, win.getHeight()-self.position[1]*self.scale), self.radius * self.scale ) ]

    """This function draws the ball object in the window."""
    def draw(self):
        for i in self.vis:
            i.draw(self.win)
    
    """"This function undraws the ball object in the window."""
    def undraw(self):
        for i in self.vis:
            i.undraw()
    
    """This function returns the height of the window."""
    def getHeight(self):
        return self.height
    
    """This function returns the width of the window."""
    def getWidth(self):
        return self.width
    
    """This function returns the mass of the ball object."""
    def getMass(self):              
        return self.mass
        
    """This function returns the radius of the ball object as a scalar value."""    
    def getRadius(self):            
        return self.radius
        
    """This function returns a 2 element tuple with the x,y position of the ball object.""" 
    def getPosition(self):          
        return self.position[:]
        
    """This function returns a 2 element tuple with the x and y velocities."""
    def getVelocity(self):          
        return self.velocity[:]
        
    """This function returns a 2 element acceleration with the x and y accelerations."""    
    def getAcceleration(self):      # returns a 2-element tuple with the x and y acceleration values.
        return self.acceleration[:]
    
    """This function sets the mass of the ball object."""   
    def setMass(self, m):
        self.mass = m
    
    """This function sets the x,y position of the ball object.   The px and py variables 
    are the new x,y values.  The x coordinate of p is assigned to the x coordinate in self.pos, 
    and the y coordinate of p is assigned to the y coordinate in self.pos."""   
    def setPosition(self, px, py):  # px and py are the new x,y values
        self.position[0] = px       # assign to the x coordinate in self.pos the x coordinate of p
        self.position[1] = py       # assign to the y coordinate in self.pos the y coordinate of p
        for i in self.vis:
            c = i.getCenter()
            dx = (self.scale*px)-(c.getX())
            dy = (self.win.getHeight()-(self.scale*py)-(c.getY()))
            i.move(dx, dy)
    
    """This function sets the x,y velocity of the ball object.   The vx and vy variables 
    are the new x,y values.  The x coordinate of v is assigned to the x coordinate in self.velocity, 
    and the y coordinate of v is assigned to the y coordinate in self.velocity."""  
    def setVelocity(self, vx, vy): # vx and vy are the new x and y velocities
        self.velocity[0] = vx
        self.velocity[1] = vy
    
    """This function sets the x,y acceleration of the ball object.   The ax and ay variables 
    are the new x,y values.  The x coordinate of a is assigned to the x coordinate in self.acceleration, 
    and the y coordinate of a is assigned to the y coordinate in self.acceleration."""  
    def setAcceleration(self, ax, ay): # ax and ay are new x and y accelerations.
        self.acceleration[0] = ax
        self.acceleration[1] = ay
    
    """This function fills the area of the ball with a random color, and sets its outline to a different random color and a width of 3."""  
    def randomcolor(self):
        for i in self.vis:
            i.setFill(gr.color_rgb(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
            i.setOutline(gr.color_rgb(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
            i.setWidth(8)
    
    """This function moves the ball object in the left x direction."""       
    def moveLeft(self):
        self.setPosition(self.position[0]-3, self.position[1])
        self.velocity[0] = -(self.velocity[0])
    
    """This function moves the ball object in the right x direction."""
    def moveRight(self):
        self.setPosition(self.position[0]+1, self.position[1])
        
    """This function adjusts the position, velocity, and vis values of the ball object through 
    dependence on its current acceleration and force values.  It takes one argument (dt), 
    which is the time step that indicates how much time to run the simulation for."""
    def update(self, dt):
        # update the x position using x_new = x_old + x_vel*dt + 0.5*x_acc * dt*dt
        self.position[0] = self.position[0] + self.velocity[0]*dt + 0.5*self.acceleration[0] * dt*dt
        # update the y position using y_new = y_old + y_vel*dt + 0.5*y_acc * dt*dt 
        self.position[1] = self.position[1] + self.velocity[1]*dt + 0.5*self.acceleration[1] * dt*dt
        # assign to dx the x velocity times dt times the scale factor (self.scale)
        dx = self.velocity[0]*dt*self.scale
        # assign to dy the negative of the y velocity times dt times the scale factor (self.scale)
        dy = -(self.velocity[1]*dt*self.scale)
        # for each item in self.vis
        for i in self.vis:
            # call the move method of the graphics object with dx and dy as arguments.
            i.move(dx, dy)
        # update the x velocity by adding the acceleration times dt to its old value
        self.velocity[0] = self.velocity[0]+(self.acceleration[0]*dt)
        # update the y velocity by adding the acceleration times dt to its old value
        self.velocity[1] = self.velocity[1]+(self.acceleration[1]*dt)

class Block:

    """This function initializes the attributes of the block object.  Self, win, and position 
    are the only non optional arguments."""
    def __init__(self, win, dx=0, dy=0):
        self.win = win
        self.dx = dx
        self.dy = dy
        self.position = [0,0]
        self.velocity = [0,0]
        self.acceleration = [0,0]
        self.scale = 10
        self.vis = [gr.Rectangle(gr.Point((self.position[0]-self.dx/2)*self.scale, (self.position[1]-self.dy/2)*self.scale), gr.Point((self.position[0]+self.dx/2)*self.scale, (self.position[1]+self.dy/2)*self.scale))]
    
    """This function draws the block object in the window."""
    def draw(self):
        for i in self.vis:
            i.draw(self.win)
     
    """This function undraws the block object in the window."""       
    def undraw(self):
        for i in self.vis:
            i.undraw()
     
    """This function returns a 2 element tuple with the x,y position of the block object."""       
    def getPosition(self):          # returns a 2-element tuple with the x, y position.
        return self.position[:]
    
    """This function sets the x,y position of the block object.   The px and py variables 
    are the new x,y values.  The x coordinate of p is assigned to the x coordinate in self.pos, 
    and the y coordinate of p is assigned to the y coordinate in self.pos."""       
    def setPosition(self, px, py):  # px and py are the new x,y values
        self.position[0] = px       # assign to the x coordinate in self.pos the x coordinate of p
        self.position[1] = py       # assign to the y coordinate in self.pos the y coordinate of p
        for i in self.vis:
            c = i.getCenter()
            dx = (self.scale*px)-(c.getX())
            dy = (self.win.getHeight()-(self.scale*py)-(c.getY()))
            i.move(dx, dy)
            
    """This function returns a 2 element tuple with the x and y velocities."""
    def getVelocity(self):          # returns a 2-element tuple with the x and y velocities.
        return self.velocity[:]
    
    """This function sets the x,y velocity of the block object.   The vx and vy variables 
    are the new x,y values.  The x coordinate of v is assigned to the x coordinate in self.velocity, 
    and the y coordinate of v is assigned to the y coordinate in self.velocity."""     
    def setVelocity(self, vx, vy): # vx and vy are the new x and y velocities
        self.velocity[0] = vx
        self.velocity[1] = vy
    
    """This function returns a 2 element tuple with the x and y accelerations."""    
    def getAcceleration(self):      # returns a 2-element tuple with the x and y acceleration values.
        return self.acceleration[:]
    
    """This function sets the x,y acceleration of the block object.   The ax and ay variables 
    are the new x,y values.  The x coordinate of a is assigned to the x coordinate in self.acceleration, 
    and the y coordinate of a is assigned to the y coordinate in self.acceleration."""  
    def setAcceleration(self, ax, ay): # ax and ay are new x and y accelerations.
        self.acceleration[0] = ax
        self.acceleration[1] = ay
    
    """This function uses the graphics setFill function to fill the block object with the color 
    grey, the setOutline function to set the color of the outline to black, and the setWidth 
    function to set the width of the block's outline to 2."""    
    def blockcolor(self):
        for i in self.vis:
            i.setFill("grey")
            i.setOutline("black")
            i.setWidth(2)
    
    """This function uses the graphics setFill function to fill the block object red."""
    def redblock(self):
        for i in self.vis:
            i.setFill("red")
    
    """This function physically removes a given block."""        
    def remove(self):
    	return list.pop(self)
    
    """This function adjusts the position, velocity, and vis values of the block object through 
    dependence on its current acceleration and force values.  It takes one argument (dt), 
    which is the time step that indicates how much time to run the simulation for."""   
    def update(self, dt):
        # update the x position using x_new = x_old + x_vel*dt + 0.5*x_acc * dt*dt
        self.position[0] = self.position[0] + self.velocity[0]*dt + 0.5*self.acceleration[0] * dt*dt
        # update the y position using y_new = y_old + y_vel*dt + 0.5*y_acc * dt*dt 
        self.position[1] = self.position[1] + self.velocity[1]*dt + 0.5*self.acceleration[1] * dt*dt
        # assign to dx the x velocity times dt times the scale factor (self.scale)
        dx = self.velocity[0]*dt*self.scale
        # assign to dy the negative of the y velocity times dt times the scale factor (self.scale)
        dy = self.velocity[1]*dt*self.scale
        # for each item in self.vis
        for i in self.vis:
            # call the move method of the graphics object with dx and dy as arguments.
            i.move(dx, -dy)
        # update the x velocity by adding the acceleration times dt to its old value
        self.velocity[0] = self.velocity[0]+(self.acceleration[0]*dt)
        # update the y velocity by adding the acceleration times dt to its old value
        self.velocity[1] = self.velocity[1]+(self.acceleration[1]*dt)
    
    """This function checks if a ball object has collided with a block object by using the 
    ball's getPosition and getRadius functions.  If it is colliding, the function returns True.  
    If it is not colliding, the function returns false."""
    def collision(self, ball):
        if (abs(ball.position[1]-self.position[1]))<(ball.radius+(self.dy)/2):  #if the ball is colliding with the block
            if (abs(ball.position[0]-self.position[0]))<(ball.radius+(self.dx)/2):
                return True
        else:
            return False

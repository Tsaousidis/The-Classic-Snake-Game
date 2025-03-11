
from turtle import Turtle

def draw_boundary():
    # Create a Turtle object to draw the boundary
    boundary = Turtle()
    boundary.hideturtle()
    boundary.color("white")
    boundary.penup()

    # Start drawing the boundary from the top-left corner (coordinates -290, 270)
    boundary.goto(-290, 270)
    boundary.pendown()
    
    # Draw the rectangular boundary with dimensions 580x560 (width x height)
    for _ in range(2):
        boundary.forward(580)  
        boundary.right(90)
        boundary.forward(560)  
        boundary.right(90)

    boundary.penup() # Lift the pen again after finishing the drawing


from turtle import Turtle

# Define constants for starting positions, movement distance, and direction angles
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.next_direction = self.head.heading()

    def create_snake(self):
        # Create the snake with its initial starting positions
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        # Create a new segment and add it to the snake's list of segments 
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)  

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        # Add a new segment to the snake, extending its length
        self.add_segment(self.segments[-1].position())

    def move(self):
        # Move the snake by moving each segment towards the previous segment's position
        self.head.setheading(self.next_direction)
        # Move the last segment to the position of the second-to-last segment
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)  

    def up(self):
        # Change the snake's direction to up if it's not already heading down
        if self.head.heading() != DOWN:
            self.next_direction = UP

    def down(self):
        # Change the snake's direction to down if it's not already heading up
        if self.head.heading() != UP:
            self.next_direction = DOWN

    def left(self):
        # Change the snake's direction to left if it's not already heading right
        if self.head.heading() != RIGHT:    
            self.next_direction = LEFT

    def right(self):
        # Change the snake's direction to right if it's not already heading left
        if self.head.heading() != LEFT:
            self.next_direction = RIGHT
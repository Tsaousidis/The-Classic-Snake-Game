
from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        # Generate random x and y coordinates for the food within the game boundaries
        random_x = randint(-280, 280)
        random_y = randint(-280, 240)
        self.goto(random_x, random_y)
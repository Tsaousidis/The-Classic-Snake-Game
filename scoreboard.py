
from turtle import Turtle

# Constants for scoreboard alignment and font style
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("pink")
        self.penup()
        self.goto(0, 270)        
        self.hideturtle()
        self.update_scoreboard()
    
    # Display the current score at the top of the screen
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT) 

    # Display "GAME OVER" message at the center of the screen
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)                   
    
    # Increase the score by 1, clear the previous score, and update the scoreboard
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
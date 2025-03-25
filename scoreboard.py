
from turtle import Turtle

# Constants for scoreboard alignment and font style
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Udemy_100_days_of_code/Github_pushed/The_Classic_Snake_Game/High_score.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.color("pink")
        self.penup()
        self.goto(0, 270)        
        self.hideturtle()
        self.update_scoreboard()
    
    # Display the current score at the top of the screen
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT) 

    def reset(self):
        if self.score > self.high_score:  
            self.high_score = self.score
            with open("Udemy_100_days_of_code/Github_pushed/The_Classic_Snake_Game/High_score.txt", mode="w") as data:
                data.write(f"{self.high_score}")
                
        self.score = 0
        self.update_scoreboard()                
    
    # Increase the score by 1, clear the previous score, and update the scoreboard
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
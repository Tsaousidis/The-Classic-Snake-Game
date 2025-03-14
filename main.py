
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from boundary import draw_boundary
import time

def main():
    # Set up the game screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("The Snake Game")
    screen.tracer(0)

    # Draw game boundaries on the screen
    draw_boundary()

    # Create the snake, food, and scoreboard objects
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    # Set up key bindings for snake movement
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    # Main game loop
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Check if the snake collides with the food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Check if the snake collides with the walls
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 270 or snake.head.ycor() < -290:
            scoreboard.reset()
            snake.reset()

        # Check if the snake collides with its own tail
        for segment in snake.segments[1:]:
            if segment == snake.head:
                pass            
            elif snake.head.distance(segment) < 10:
                scoreboard.reset()
                snake.reset()

    screen.exitonclick()
    
# Start the game if this file is executed directly
if __name__ == "__main__":
    main()
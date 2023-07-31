from turtle import Screen           # Import all the relevant modules with relevant classes.
from snake import Snake             # Importing a class that creates a snake on screen.
from food import Food               # Imports the food class which the snake is to controlled to eat.
from scoreboard import Scoreboard   # Scoreboard to keep score and end the game based on the game ending conditions
import time                         # Time module to delay or speed up loops

# Screen Setup.
screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)
screen.bgcolor('black')
screen.title('Snake')

# Object instances of classes.
snake = Snake()
food = Food()
scoreboard = Scoreboard()
snake.create_snake()

# Setting up event listeners to listen to user input and make changes accordingly.
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Initiate a flag to control the while loop.
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    if snake.segments[0].distance(food) <= 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    if snake.segments[0].xcor() >= 290 or snake.segments[0].xcor() <= -290 or snake.segments[0].ycor() >= 290 or snake.segments[0].ycor() <= -290:
        scoreboard.reset_score()
        snake.reset_snake()
        snake.create_snake()
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            snake.reset_snake()
            snake.create_snake()
            scoreboard.reset_score()

screen.exitonclick()

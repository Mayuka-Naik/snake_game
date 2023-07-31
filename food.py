from turtle import Turtle
import random
x_coordinate = random.randint(-280, 280)
y_coordinate = random.randint(-280, 280)


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('blue')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed('fastest')
        self.goto(x_coordinate, y_coordinate)

    def refresh(self):
        new_x_coordinate = random.randint(-280, 280)
        new_y_coordinate = random.randint(-280, 280)
        self.goto(new_x_coordinate, new_y_coordinate)

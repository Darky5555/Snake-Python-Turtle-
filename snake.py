from turtle import *
import random

def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.penup()
    pen.goto(-240, 240)
    pen.pendown()
    pen.color('light blue')
    pen.begin_fill()
    pen.goto(240, 240)
    pen.goto(240, -240)
    pen.goto(-240, -240)
    pen.goto(-240, 240)
    pen.end_fill()

class Head(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.penup()
        self.goto(0, 0)
        self.direction = "up"
        self.alive = True

    def up(self):
        if self.direction != "down":
            self.setheading(90)
            self.direction = "up"

    def down(self):
        if self.direction != "up":
            self.setheading(270)
            self.direction = "down"

    def left(self):
        if self.direction != "right":
            self.setheading(180)
            self.direction = "left"

    def right(self):
        if self.direction != "left":
            self.setheading(0)
            self.direction = "right"

    def move(self):
        self.forward(20)
        if self.xcor() > 240 or self.xcor() < -240 or self.ycor() > 240 or self.ycor() < -240:
            self.hideturtle()
            self.alive = False


class Segment(Turtle):
    def __init__(self, body):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.penup()
        self.goto(body[-1].xcor(), body[-1].ycor())


class Apple(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.goto(random.randint(-230, 230), random.randint(-230, 230))

    def relocate(self):
        self.goto(random.randint(-230, 230), random.randint(-230, 230))


screen = Screen()
screen.bgcolor("black")
screen.setup(520, 520)
playing_area()

head = Head()
body = []
body.append(head)
body.append(Segment(body))

apple = Apple()

screen.listen()
screen.onkey(head.up, "Up")
screen.onkey(head.down, "Down")
screen.onkey(head.left, "Left")
screen.onkey(head.right, "Right")

def game_loop():
    if head.alive:
        for i in range(len(body) - 1, 0, -1):
            x = body[i - 1].xcor()
            y = body[i - 1].ycor()
            body[i].goto(x, y)

        head.move()

        if head.distance(apple) < 20:
            apple.relocate()
            body.append(Segment(body))

        for segment in body[1:]:
            if head.distance(segment) < 20:
                head.hideturtle()
                head.alive = False

    screen.ontimer(game_loop, 150)

game_loop()
screen.exitonclick()

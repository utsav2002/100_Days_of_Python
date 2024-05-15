from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def forwards():
    timmy.setheading(0)
    timmy.forward(10)

def backwards():
    timmy.backward(10)

def clock_wise():
    timmy.right(10)

def anti_clock_wise():
    timmy.left(10)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()
    

screen.listen()
screen.onkey(key="w", fun=forwards)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="a", fun=anti_clock_wise)
screen.onkey(key="d", fun=clock_wise)
screen.onkey(key="c", fun=clear)


screen.exitonclick()

from turtle import Turtle, Screen

def start():
    timmy = Turtle()
    timmy.shape("turtle")
    timmy.color("blue")
    timmy.forward(100)

    my_screen = Screen()
    print(my_screen.canvheight)
    my_screen.exitonclick()


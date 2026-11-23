from turtle import Turtle, Screen
from tkinter import *

# drawing line following the arrow sof the computer
my_turtle = Turtle()
screen = Screen()
screen.title("Sketch")


def go_left():
    my_turtle.left(10)


def move():
    my_turtle.forward(10)

def go_right():
    my_turtle.right(10)

def clear_screen():
    my_turtle.goto(0,0)
    my_turtle.setheading(360)
    my_turtle.clear()


canvas = screen.getcanvas()
button = Button(master=canvas.master, text="Clean", command=clear_screen)
button.pack()


screen.onkey(move, "Up")
screen.onkey(go_left, "Left")
screen.onkey(move, "Down")
screen.onkey(go_right, "Right")


screen.listen()


my_turtle.getscreen()._root.mainloop()

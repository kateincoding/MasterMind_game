#!/usr/bin/python3
import turtle

turtle.bgcolor("black")
turtle.pensize(2)
colors = ["green", "red", "blue", "yellow", "magenta",
          "black", "white", "cyan"]


class Balls():
    """Drawing with turtle"""

    def __init__(self):
        turtle.screensize(400, 400)
        self.turtle = turtle.Turtle()

    def draw_aptems(self, colors="", axis=0, coor=0):
        self.colors = colors
        self.axis = axis
        self.coor = coor
        coor = self.coor
        axis = self.axis
        print("Drawing...")
        for color in self.colors:
            self.turtle.speed(10)
            self.turtle.setpos(axis, coor)
            self.turtle.showturtle()
            self.turtle.begin_fill()
            self.turtle.color(color)
            self.turtle.pendown()
            self.turtle.circle(36)
            self.turtle.end_fill()
            self.turtle.penup()
            print(self.turtle.position())
            axis = axis + 100
        return(1)
    def draw_separator(self):
        axis = 0
        coor = -400
        for i in range(2):
            self.turtle.speed(2)
            self.turtle.color("yellow")
            self.turtle.setpos(axis, coor)
            self.turtle.begin_fill()
            self.turtle.pendown()
            self.turtle.left(90)
            self.turtle.forward(800)
            self.turtle.right(90)
            self.turtle.forward(20)
            self.turtle.right(180)
            self.turtle.end_fill()
            coor = self.turtle.position()[1]
            axis = self.turtle.position()[0]
            self.turtle.penup()



    def draw_pins(self, colors="", axis=0, coor=0):
        self.colors = colors
        self.axis = axis
        self.coor = coor + 54
        coor = self.coor
        axis = self.axis
        print("Drawing...")
        for count, color in enumerate(self.colors):
            self.turtle.speed(5)
            self.turtle.setpos(axis, coor)
            self.turtle.showturtle()
            self.turtle.begin_fill()
            self.turtle.color(color)
            self.turtle.pendown()
            for i in range(5):
                self.turtle.speed(1)
                self.turtle.forward(72)
                self.turtle.right(144)
            self.turtle.end_fill()
            self.turtle.penup()
            print(self.turtle.position())
            axis = axis + 100
        return(1)

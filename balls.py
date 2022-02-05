#!/usr/bin/python3
import turtle

turtle.bgcolor("black")
turtle.pensize(2)
colors = ["green", "red", "blue", "yellow", "magenta",
          "black", "white", "cyan"]


class Balls():
    """Drawing with turtle"""

    def __init__(self, level: int = 1):
        turtle.screensize(400, 400)
        self.turtle = turtle.Turtle()
        self.level = level

    def draw_aptems(self, colors="", axis=0, coor=0):
        self.colors = colors
        self.axis = axis
        self.coor = coor
        coor = self.coor
        axis = self.axis
        if self.level == 1:
            radius = 36
            distance = 100
        elif self.level == 2:
            distance = 70
            radius = 25
        else:
            radius = 25
            distance = 70
        for color in self.colors:
            print("Drawing...")
            self.turtle.speed(10)
            self.turtle.setpos(axis, coor)
            self.turtle.showturtle()
            self.turtle.begin_fill()
            self.turtle.color(color)
            self.turtle.pendown()
            self.turtle.circle(radius)
            self.turtle.end_fill()
            self.turtle.penup()
            axis = axis + distance
        return(1)

    def draw_separator(self):
        axis = 0
        coor = -400
        for i in range(2):
            print("Drawing...")
            self.turtle.speed(10)
            self.turtle.color("yellow")
            self.turtle.setpos(axis, coor)
            self.turtle.begin_fill()
            self.turtle.pendown()
            self.turtle.left(90)
            self.turtle.forward(800)
            self.turtle.right(90)
            self.turtle.forward(20)
            self.turtle.right(180)
            coor = self.turtle.position()[1]
            axis = self.turtle.position()[0]
            self.turtle.penup()

    def draw_pins(self, colors="", axis=0, coor=0):
        self.colors = colors
        self.axis = axis
        self.coor = coor + 54
        coor = self.coor
        axis = self.axis
        if self.level == 1:
            radius = 72
            distance = 100
        elif self.level == 2:
            radius = 66
            distance = 70
        else:
            radius = 55
            distance = 70
        print("Drawing...")
        for color in self.colors:
            print("Drawing...")
            self.turtle.speed(10)
            self.turtle.setpos(axis, coor)
            self.turtle.showturtle()
            self.turtle.begin_fill()
            self.turtle.color(color)
            self.turtle.pendown()
            for i in range(5):
                self.turtle.speed(10)
                self.turtle.forward(radius)
                self.turtle.right(144)
            self.turtle.end_fill()
            self.turtle.penup()
            axis = axis + distance
        return(1)

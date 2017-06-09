"""
turtle is a graphics module in all python versions.
here is an example to illustrate some turtle graphics basics
"""

import turtle

myTurtle = turtle.Turtle()
myWindow = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)           # move forward by "lineLen"
        myTurtle.right(90)                  # turn right at 90 degrees
        drawSpiral(myTurtle, lineLen - 2)   # recursion

drawSpiral(myTurtle, 100)
myWindow.exitonclick()                      # put the turtle into a wait mode, and exit on click
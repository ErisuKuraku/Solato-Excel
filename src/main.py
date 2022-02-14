import json
from turtle import *

planetOne = [1, 1, 10, "red"]
planetTwo = [2, 0.5, 30, "blue"]
planetThree = [3, 2, 25, "lime"]
planetFour = [4, 1.2, 10, "gray"]
planetFive = [4, 2.5, 10, "yellow"]
planetSix = [4, 2.2, 10, "purple"]
planets = [planetOne, planetTwo, planetThree, planetFour, planetFive, planetSix]

' ^^ Placeholder values, waiting for JSON template ^^ '

planetLength = len(planets)
distanceScale = 200

screen = Screen()
screen.tracer(0)
turtle = Turtle()
turtle.setheading(90)


def drawPlanet(t,p):
    t.fillcolor(p[3])
    t.forward(p[1] * distanceScale)
    t.begin_fill()
    t.pendown()
    t.circle(p[2])
    t.penup()
    t.goto(0, 0)
    t.end_fill()



def draw():
    turtle.clear()
    i = 0
    while i < planetLength:
        drawPlanet(turtle, planets[i])
        i += 1
    screen.update()
    turtle.left(1)
    screen.ontimer(draw, 200)

draw()

screen.mainloop()

import json
from turtle import *

planetOne = [1, 1, 10]
planetTwo = [2, 0.5, 30]
planets = [planetOne, planetTwo]
colour = "yellow"
planetLength = len(planets)
distanceScale = 200

' ^^ Placeholder values, waiting for JSON template ^^ '

screen = Screen()
screen.tracer(0)
turtle = Turtle()
turtle.setheading(90)


def drawPlanet(t,p,c):
    t.fillcolor(c)
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
        drawPlanet(turtle, planets[i], colour)
        i += 1
    screen.update()
    turtle.left(1)
    screen.ontimer(draw, 200)

draw()

screen.mainloop()

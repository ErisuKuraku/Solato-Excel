import json
from turtle import *

with open('solato_export.json') as json_file:
    planets = json.load(json_file)
    print("debug mode")
    print(planets)

    print(type(planets))
    print(type(planets[0]))

for planet in planets:
    print(planet['type'])

    print(planet['size'], planet['radius'], planet['colour'])



distanceScale = 200

screen = Screen()
screen.tracer(0)
turtle = Turtle()
turtle.setheading(90)

def drawPlanet(t,p):
    t.fillcolor(p['colour'])
    t.forward(p['size'] * distanceScale)
    t.begin_fill()
    t.pendown()
    t.circle(p['radius'])
    t.penup()
    t.goto(0, 0)
    t.end_fill()



def draw():
    turtle.clear()
    i = 0 
    while i < len(planets):
        drawPlanet(turtle, planets[i])
        i += 1
        screen.update()
        turtle.left(1)
        screen.ontimer(draw, 200)

draw()

screen.mainloop()

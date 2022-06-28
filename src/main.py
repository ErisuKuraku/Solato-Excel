import json
from turtle import *

with open('solato_export.json') as json_file:
    planets = json.load(json_file)
    print("debug mode")
    #print(planets)

    #print(type(planets))
    #print(type(planets[0]))

for planet in planets:
    print(planet['type'])

    print(planet['size'], planet['radius'], planet['colour'])



distanceScale = 200

screen = Screen()
screen.tracer(0)
t = Turtle()
t.setheading(90)

def drawPlanet(p):
    t.fillcolor(p['colour'])
    t.forward(p['radius'] * distanceScale)
    t.begin_fill()
    t.pendown()
    t.circle(p['size']*20)
    t.penup()
    t.goto(0, 0)
    t.end_fill()



def draw():
    t.clear()
    i = 0 
    while i < 6:
        drawPlanet(planets[i])
        i=i+1
        screen.update()
        t.left(1)
    screen.ontimer(draw, 200)

draw()


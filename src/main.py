import json
with open('src\solato_export.json') as json_file:
    planets = json.load(json_file)
    print("debug mode")
    print(planets)

    print(type(planets))
    
# from turtle import *

# planetLength = len(planets)
# distanceScale = 200

# screen = Screen()
# screen.tracer(0)
# turtle = Turtle()
# turtle.setheading(90)


# def drawPlanet(t,p):
#     t.fillcolor(p[3])
#     t.forward(p[1] * distanceScale)
#     t.begin_fill()
#     t.pendown()
#     t.circle(p[2])
#     t.penup()
#     t.goto(0, 0)
#     t.end_fill()



# def draw():
#     turtle.clear()
#     i = 0
#     while i < planetLength:
#         drawPlanet(turtle, planets[i])
#         i += 1
#     screen.update()
#     turtle.left(1)
#     screen.ontimer(draw, 200)

# draw()

# screen.mainloop()

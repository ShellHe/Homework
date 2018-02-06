import turtle
santa = turtle.Turtle()
wn = turtle.Screen()

path = [(45,150),(90,100)(90,100),(90,150),(45,100),(90,100),(90,100)]

for angle, dist in path:
    santa.left(angle)
    santa.forward(dist)

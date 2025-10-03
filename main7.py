import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()

num_sides=6
size_length=70
angle=360/6

for i in range(num_sides):
    polygon.forward(size_length)
    polygon.right(angle)

turtle.done()
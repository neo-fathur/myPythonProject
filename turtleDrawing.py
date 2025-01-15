import turtle

turtle.shape("turtle")

turtle.reset()
turtle.color("green") 

for i in range(10):
    turtle.forward(15)
    turtle.penup()
    turtle.forward(5)
    turtle.pendown()

for i in 20, 30, 40:
    turtle.left(i)
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)


turtle.reset()
turtle.color("green") 

def draw_shape(sides, length):
    for _ in range(sides):
        turtle.forward(length)
        turtle.left(360 / sides)

def repeat_shape(sides, length):
    for _ in range (sides):
        draw_shape(sides, length)
        turtle.forward(length)
        turtle.right(360 / sides)

repeat_shape(6, 100)

turtle.exitonclick()
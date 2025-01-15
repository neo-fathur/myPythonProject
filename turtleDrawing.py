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

def hexagon(size):
    for _ in range(6):
        turtle.forward(size)
        turtle.left(60)
for _ in range (6):
    hexagon(100)
    turtle.forward(100)
    turtle.right(60)

turtle.exitonclick()
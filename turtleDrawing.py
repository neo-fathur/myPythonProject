import turtle
turtle.shape("turtle")

turtle.reset()
turtle.speed(10)
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
turtle.speed(3)
turtle.color("green") 
turtle.fillcolor("yellow")

def draw_shape(sides, length):
    for _ in range(sides):
        turtle.forward(length)
        turtle.left(360 / sides)

def repeat_shape(sides, length):
    for _ in range (sides):
        turtle.pendown()
        turtle.begin_fill()
        draw_shape(sides, length)
        turtle.end_fill()
        turtle.penup()

        turtle.forward(length)
        turtle.right(360 / sides)

repeat_shape(7, 100)

turtle.goto(0, 250)
turtle.color('black')
turtle.write("Python is awesome!", align="center", font=(None, 16, "bold"))
turtle.goto(0, 280)



turtle.exitonclick()
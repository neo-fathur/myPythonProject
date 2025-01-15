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


turtle.reset()
turtle.color("green") 

def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(size)
    turtle.penup()
    turtle.end_fill()
    turtle.pendown()

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(500)

draw_circle(tommy, "green", 50, 25, 0)
draw_circle(tommy, "blue", 50, 0, 0)
draw_circle(tommy, "yellow", 50, -25, 0)

tommy.penup()
tommy.goto(0,-50)
tommy.color('black')
tommy.write("Let's Learn Python!", align="center", font=(None, 16, "bold"))
tommy.goto(0,-80)

turtle.exitonclick()
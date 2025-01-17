import turtle

turtle.reset()
turtle.speed(10)

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

repeat_shape(6, 100)

turtle.color('black')
turtle.goto(0, 250)
turtle.write("Python is awesome!", align="center", font=(None, 16, "bold"))
turtle.goto(0, 280)



turtle.reset()
turtle.shape("turtle")
def draw_spiral(radius):
    original_xcor = turtle.xcor()
    original_ycor = turtle.ycor()
    speed = 1
    while True:
        turtle.forward(speed)
        turtle.left(10)
        speed += 0.1
        if turtle.distance(original_xcor, original_ycor) > radius:
            break

draw_spiral(150)

turtle.exitonclick()
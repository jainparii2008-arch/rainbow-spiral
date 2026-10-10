
import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Rainbow Spiral")
screen.setup(width=900, height=900)
screen.colormode(1.0)

t = turtle.Turtle()
t.speed(0)
t.pensize(2)
t.hideturtle()

for i in range(360):
    color = colorsys.hsv_to_rgb(i / 360, 1, 1)
    t.pencolor(color)
    t.forward(i * 0.8)
    t.left(59)

turtle.done()

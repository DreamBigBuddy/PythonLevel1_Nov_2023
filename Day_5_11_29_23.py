import turtle

t = turtle.Turtle()

t.screen.colormode(255)

t.pensize(10)
t.color((66, 212, 245))
t.fillcolor("dark cyan")

t.begin_fill()
for i in range(4):
    t.forward(100)
    t.right(90)

t.end_fill()

t.clear()

t.circle(50, 360, 3)

t.penup()
t.goto(100, 100)
t.pendown()
t.forward(100)

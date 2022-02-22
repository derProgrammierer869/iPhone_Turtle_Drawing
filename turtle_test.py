import turtle
t = turtle.Turtle()
turtle.pensize(10)
turtle.speed(speed=0)

def border(t):
    t.begin_fill()
    t.penup()
    t.goto(-48,200)
    t.pendown()

    t.forward(100)
    t.circle(-25,90)

    t.forward(200)
    t.circle(-25,90)

    t.forward(100)
    t.circle(-25,90)

    t.forward(200)
    t.circle(-25,90)
    t.end_fill()
border(t)


def screen(t):
    t.begin_fill()
    t.fillcolor('white')
    t.penup()
    t.goto(-50,0)
    t.pendown()

    t.forward(105)
    t.left(90)

    t.forward(185)
    t.left(90)

    t.forward(105)
    t.left(90)

    t.forward(185)
    t.left(90)
    t.end_fill()
screen(t)


def draw_button(t):
    t.begin_fill()
    t.fillcolor('white')
    t.penup()
    t.goto(0, -43)
    t.pendown()
    t.circle(15)
    t.end_fill()
draw_button(t)


def draw_app(t, color, x, y):
    t.begin_fill()
    t.fillcolor(color)
    t.penup()
    t.goto(x,y)
    t.forward(20)
    t.left(90)
    
    t.forward(20)
    t.left(90)

    t.forward(20)
    t.left(90)

    t.forward(20)
    t.left(90)
    t.end_fill()
#row1
draw_app(t, 'green', -45, 150)
draw_app(t, 'red', -20, 150)
draw_app(t, 'yellow', 5, 150)
draw_app(t, 'grey', 30, 150)
#row2
draw_app(t, 'orange', -45, 125)
draw_app(t, 'blue', -20, 125)
draw_app(t, 'purple', 5, 125)
draw_app(t, 'red', 30, 125)
#row3
draw_app(t, 'pink', -45, 100)
draw_app(t, 'yellow', -20, 100)
draw_app(t, 'magenta', 5, 100)
draw_app(t, 'green', 30, 100)
#row4
draw_app(t, 'indigo', -45, 75)
draw_app(t, 'violet', -20, 75)
draw_app(t, 'yellow', 5, 75)
draw_app(t, 'black', 30, 75)
#row5
draw_app(t, 'turquoise', -45, 50)
draw_app(t, 'blue', -20, 50)
draw_app(t, 'violet', 5, 50)
draw_app(t, 'grey', 30, 50)
#row6
draw_app(t, 'red', -45, 15)
draw_app(t, 'orange', -20, 15)
draw_app(t, 'yellow', 5, 15)
draw_app(t, 'grey', 30, 15)
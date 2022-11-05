import turtle as t
def rectangle(horizontal, vertical, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for counter in range(1, 3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()

t.penup()
t.speed('slow')
t.bgcolor('#307D7E')
# feet
t.goto(-100, -150)
rectangle(50, 20, '#FFDA1F')
t.goto(-30, -150)
rectangle(50, 20, '#FFDA1F')
# legs
t.goto(-25, -50)
rectangle(15, 100, '#FF1F8F')
t.goto(-55, -50)
rectangle(-15, 100, '#FF1F8F')
# body
t.goto(-90, 100)
rectangle(100, 150, '#FF0000')
# arms
t.goto(-150, 70)
rectangle(60, 15, '#FF1F8F')
t.goto(-150, 110)
rectangle(15, 40, '#FF1F8F')
t.goto(10, 70)
rectangle(60, 15, '#FF1F8F')
t.goto(55, 110)
rectangle(15, 40, '#FF1F8F')
# neck
t.goto(-50, 120)
rectangle(15, 20, '#FF1F8F')
# head
t.goto(-85, 170)
rectangle(80, 50, '#FF0000')
# eyes
t.goto(-60, 160)
rectangle(30, 10, '#FFFFFF')
t.goto(-55, 155)
rectangle(5, 5, '#000000')
t.goto(-40, 155)
rectangle(5, 5, '#000000')
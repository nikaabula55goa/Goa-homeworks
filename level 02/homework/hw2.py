import turtle

# ეკრანის შექმნა
t = turtle.Turtle()
t.speed(10)

# მთავარი შენობა
t.penup()
t.goto(-100, -100)
t.pendown()
t.color("purple")
t.begin_fill()
for _ in range(4):
    t.forward(200)
    t.left(90)
t.end_fill()

# მარცხენა კოშკი
t.penup()
t.goto(-100, 100)
t.pendown()
t.color("blue")
t.begin_fill()
for _ in range(3):
    t.forward(60)
    t.left(120)
t.end_fill()

# მარჯვენა კოშკი
t.penup()
t.goto(40, 100)
t.pendown()
t.begin_fill()
for _ in range(3):
    t.forward(60)
    t.left(120)
t.end_fill()

# კარი
t.penup()
t.goto(-20, -100)
t.pendown()
t.color("red")
t.begin_fill()
for _ in range(2):
    t.forward(40)
    t.left(90)
    t.forward(60)
    t.left(90)
t.end_fill()

# ეკრანის შენარჩუნება
turtle.done()
from turtle import *

#we want to paint a palace

#step 1:  draw a squar

speed(100)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of squar

#drawing a door

forward(70)
color("yellow")
left(90)
forward(120)        #height of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

color("red")
right(150)
forward(200)
left(120)
forward(200)

penup()
goto(10, 120)
pendown()

color("orange")
right(150)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)

penup()
goto(140, 120)
pendown()

left(180)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

penup()
goto(5, 200)
pendown()

width(7)
color("purple")
right(90)
forward(200)

left(90)
forward(200)


left(90)
forward(200)
#end of squar


#drawing a door
penup()
goto(1, 1)
pendown()

left(180)
forward(60)

forward(70)
color("yellow")
right(90)
forward(120)        #height of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(5, 190)
pendown()

color("red")
right(150)
forward(200)
left(120)
forward(200)

penup()
goto(-5, 120)
pendown()

color("orange")
right(60)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)

penup()
goto(-140, 120)
pendown()

right(180)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

exitonclick()
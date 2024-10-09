from turtle import *

#we want to paint a hous 

#step 1:  draw a squar

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

exitonclick()
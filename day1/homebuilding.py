from turtle import *

speed(20)
penup()
goto(-150, -200)
pendown()

width(7)

forward(300)
left(90)

forward(300)
left(90)

forward(300)
left(90)

forward(300)

penup()
goto(150,100)
pendown()
color("yellow")

right(135)
begin_fill()
forward(212)
left(90)
forward(212)
end_fill()
#door
penup()
goto(50, -200)
pendown()
color("brown")
begin_fill()


right(135)
forward(100)

right(90)
forward(60)

right(90)
forward(100)
end_fill()

#window1

penup()
goto(-120, 50)
pendown()
width(3)
begin_fill()
forward(70)
left(90)
forward(80)
left(90)
forward(70)
left(90)
forward(80)
end_fill()
#wondow2
penup()
goto(120, 50)
pendown()
width(3)
begin_fill()
forward(80)
left(90)
forward(70)
left(90)
forward(80)
left(90)
forward(70)
end_fill()

#down window

penup()
goto(-120, -100)
pendown()
begin_fill()
right(90)
forward(80)
right(90)
forward(70)
right(90)
forward(80)
right(90)
forward(70)
end_fill()


#turttle goes home

penup()
goto(-290,-260)
pendown()

color("green")
shape("turtle")

right(90)
speed(1)
forward(370)
left(90)
forward(70)










exitonclick()
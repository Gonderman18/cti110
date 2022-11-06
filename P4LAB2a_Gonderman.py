import turtle

turtle.shape('turtle')          # First Turtle to manually Draw Shapes
turtle.speed(1)
turtle.pensize(3)
turtle.colormode(255)

turtle.color('red')
turtle.left(0)

turtle.forward(200)             # Red Square
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
#turtle.left(0)


turtle.penup()                  # picks pen up Moves down to make room
turtle.forward(200)

turtle.pendown()                # put ped back down change color to blue
turtle.color(0,0,250)
turtle.left(90)

turtle.left(60)                 # first blue triangle at bottom of page
turtle.forward(200)
turtle.right(120)
turtle.forward(200)
turtle.right(120)
turtle.forward(200)

turtle.left(180)                # pen back to right side of triangle base
turtle.forward(200)

turtle.penup()                  # picks pen up moves up to inside 1st blue Square
turtle.color(255,0,0)
turtle.left(90)
turtle.forward(220)


import turtle                   # New turtle for green square 
ks = turtle.Turtle()
ks.shape('classic')
ks.left(180)
ks.color("green")
ks.showturtle()
ks.speed(1)
ks.left(0)
ks.pensize(3)

for i in range(4):              #Green Square on the Left          
    ks.forward(200)    
    ks.left(90)
    


dg = turtle.Turtle()            # New turtle for orange Square
dg.shape('triangle')
dg.color('orange')
dg.pensize(3)
#dg.left(180)
dg.speed(1)                 
#dg.left(240)

dg.penup()
dg.goto(-200,10)
dg.pendown()


for i in range(3):             #Orange Triangle to the Left          
    dg.forward(200)
    dg.right(240)
    

turtle.exitonclick()

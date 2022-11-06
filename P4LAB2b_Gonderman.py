import turtle


turtle = turtle.Turtle()
turtle.color("green")
turtle.showturtle()
turtle.speed(1)
turtle.pensize(5)


turtle.penup()                # takes turtle to starting point
turtle.goto(-350,-100)

turtle.pendown()              # Draws the D
turtle.circle(180,180)
turtle.left(90)
turtle.goto(-350,-100)


turtle.penup()                # space between D and G
turtle.goto(100,-100)

turtle.pendown()              # draws the 1st half of the Bottom half of the G
turtle. left(90)
turtle.circle(180,90)
turtle.left(180)
turtle.circle(0,270)
turtle.forward(200)

turtle.penup()
turtle.goto(100,-100)

turtle.pendown()
turtle.forward(10)            # draws the 2nd half of the bottom of the G


turtle.penup()
turtle.goto(90,260)

turtle.pendown()              # drwas the Top half of the G
turtle.circle(180,180)


turtle.penup()
turtle.goto(200,100)

turtle.color('DarkOrange')        # Writes my initals  
style = ('Times New Roman', 90, 'normal')
turtle.write('DG', font=style, align='center')
turtle.showturtle()




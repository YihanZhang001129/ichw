import turtle

Mercury = turtle.Turtle()
Venus = turtle.Turtle()
Earth = turtle.Turtle()
Mars = turtle.Turtle()
Jupiter = turtle.Turtle()
Saturn = turtle.Turtle()

wn = turtle.Screen
wn.bgcolor("black")

Sun=turtle.Turtle()
Sun.color("yellow")
Sun.shape("circle")
Sun.goto(0,0)

Mercury.color('red')
Venus.color('green')
Earth.color('blue') 
Mars.color('white') 
Jupiter.color('purple') 
Saturn.color('orange') 

Mercury.penup()
Mercury.goto(0,-20)
Mercury.pendown()
Mercury.shape('circle')


Venus.penup()
Venus.goto(0,-40)
Venus.pendown()
Venus.shape('circle')


Earth.penup()
Earth.goto(0,-80)
Earth.pendown()
Earth.shape('circle')


Mars.penup()
Mars.goto(0,-140)
Mars.pendown()
Mars.shape('circle')


Jupiter.penup()
Jupiter.goto(0,-180)
Jupiter.pendown()
Jupiter.shape('circle')


Saturn.penup()
Saturn.goto(0,-240)
Saturn.pendown()
Saturn.shape('circle')

i = 0
while i <100000:
    Mercury.circle(20,10,None)
    Venus.circle(40,8,None)
    Earth.circle(80,6,None) 
    Mars.circle(140,4,None) 
    Jupiter.circle(180,3,None) 
    Saturn.circle(240,1,None) 
    i = i + 1

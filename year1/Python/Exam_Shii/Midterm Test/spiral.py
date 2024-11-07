import turtle

def draw_sq(n) :
    for _ in range(4):
        turtle.forward(n)
        turtle.left(90)

def draw_spiral(s):
    while s > 5:
        turtle.penup()
        turtle.backward(s / 2)
        turtle.right(90)
        turtle.forward(s / 2)
        turtle.left(90)
        #goto start point
        
        turtle.pendown()
        draw_sq(s)
        
        #roatet
        turtle.penup()
        turtle.goto(0,0)
        turtle.left(10)
        s = s * 0.75
        
draw_spiral(150)
    
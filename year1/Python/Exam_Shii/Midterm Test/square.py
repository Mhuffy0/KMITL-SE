import turtle

def draw_s(s) :
    for _ in range(4) :
        turtle.forward(s)
        turtle.left(90)
    #draw square
    
def draw_sg(s, g) :
    len = s
    draw_s(s)
    while len > 20 :
        turtle.penup()
        turtle.forward(g)
        turtle.left(90)
        turtle.forward(g)
        turtle.right(90)
        turtle.pendown()
        len = len - (g * 2)
        draw_s(len)

draw_sg(200, 20)
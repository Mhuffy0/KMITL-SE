import turtle 
pl = turtle.Turtle()

def draw_polygon(x,y,dhant = 4,size = 100):
    angle = ((dhant - 2)*180)/dhant
    pl.penup()
    pl.goto(x,y)
    pl.pendown()
    for i in range(dhant):
        pl.fd(size)
        pl.left(180-angle)
    
draw_polygon(0,0)
draw_polygon(10,10,5)
draw_polygon(10,10,5,200)
pl.hideturtle()

window = turtle.Screen()

turtle.done()
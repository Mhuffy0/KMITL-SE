from abc import ABC, abstractmethod
from turtle import Turtle, Screen, done

t1 = Turtle()
window = Screen()

class TwoDShape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Line(TwoDShape):
    def __init__(self,x =0 ,y=0):
        self.x =x
        self.y = y
    def draw(self):
        t1.penup()
        t1.goto(self.x, self.y)
        t1.pendown()
        t1.fd(100)

class Rectangle(TwoDShape):
    def __init__(self,x=0,y=0):
        self.x =x
        self.y = y
    def draw(self):
        t1.penup()
        t1.goto(self.x, self.y)
        t1.pendown()
        for i in range(2):
            t1.fd(100)
            t1.left(90)
            t1.fd(50)
            t1.left(90)

class Circle(TwoDShape):
    def __init__(self,x=0,y=0):
        self.x =x
        self.y = y
    def draw(self):
        t1.penup()
        t1.goto(self.x, self.y)
        t1.pendown()
        t1.circle(100)

class Square(TwoDShape):
    def __init__(self,x=0,y=0):
        self.x =x
        self.y = y
    def draw(self):
        t1.penup()
        t1.goto(self.x, self.y)
        t1.pendown()
        for i in range(4):
            t1.fd(100)
            t1.left(90)


l1 = Line(50,100)
r1 = Rectangle(-10,20)
c1 = Circle(-100,-100)
c2 = Circle(-200,20)
l2 = Line(100,-60)
sq1 = Square(100,50)

set = [r1, l1, c1, l2, c2, sq1]
for i in set:
    i.draw()

done()



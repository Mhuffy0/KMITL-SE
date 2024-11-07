import math
import turtle as tt
tt.pensize(10)

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def getArea(self):
        area = self.width + self.height
        print(f"area = {area}")
        area
        
    def getPerimeter(self):
        p = 2 * ( self.width + self.height )
        print(f"Perimeter = {p}")
        p
        
    def move(self, newX, newY):
        self.x = newX
        self.y = newY
        print(f"X,Y : ({self.x},{self.y})")
        
    def inersect(self, rec) :
        newrec = {}
        newrec[0] = min(self.x, rec[0])
        newrec[1] = min(self.y, rec[1])
        
        newrec[2] = min(self.x + self.width, rec[0] + rec[2])
        newrec[3] = min(self.y + self.height, rec[1] + rec[3])
        
        if newrec[2] <= 0 or newrec[3] <= 0:
            return None
        
        self.newrec = (newrec[0], newrec[1], newrec[2], newrec[3])
        self.rec = rec
        return self.newrec, self.rec
        
    def draw(self):
        tt.penup()
        tt.goto(self.x, self.y)
        
        tt.left(90)
        tt.pendown()
        for i in range(2) :
            tt.forward(self.height)
            tt.right(90)
            tt.forward(self.width)
            tt.right(90)
        tt.penup()
        tt.right(90)
        
        #rec2
        tt.goto(self.rec[0], self.rec[1])
        
        tt.pendown()
        tt.left(90)
        for j in range(2) :
            tt.forward(self.rec[3])
            tt.right(90)
            tt.forward(self.rec[2])
            tt.right(90)
        tt.penup()
        tt.right(90)

class Circle:
    def __init__(self, x, y, radius) :
        self.x = x
        self.y = y
        self.r = radius
        
    def getArea(self):
        self.area = math.pi * self.r**2
        self.area
        
    def getPerimeter(self):
        self.p = 2 * math.pi * self.r
        self.p
        
    def move(self, newX, newY):
        self.x = newX
        self.y = newY
        
    def draw(self):
        tt.penup()
        tt.goto(self.x, self.y)
        
        tt.pendown()
        tt.circle(self.r)
        tt.penup()
        
rec = Rectangle(50, 50, 100, 100)
rec2 = (30,50,100,100)

rec.getArea()
rec.getPerimeter()
rec.move(7,5)
rec.inersect(rec2)
rec.draw()

c = Circle(0,0,25)
c.draw()




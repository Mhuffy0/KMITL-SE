import math

class Point:
    def __init__(self, x = 0.0 , y = 0.0):
        self.x = x
        self.y = y
        
    def printinfo(self):
        print(f"X : {self.x}\nY : {self.y} ")
        
class Circle(Point):
    def __init__(self, x = 0.0 , y = 0.0 , radius = 0.0,area = 0.0):
        super().__init__(x,y)
        self.r = radius
        self.a = area
        
    def area(self):
        self.a = math.pi * self.r**2
        return self.a
        
    def printinfo(self):
        
        print(f"X : {self.x} \nY = {self.y} \nr : {self.r} \nArea : {self.a}")
    
obj = Circle(5,7,5)
obj.area()
obj.printinfo()  
from turtle import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle2D:
    def __init__(self, center_x, center_y, width, height):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height

    def __str__(self):
        return f"Center: ({self.center_x}, {self.center_y}), Width: {self.width}, Height: {self.height}"

def getRectangle(points):
    min_x = min(point.x for point in points)
    max_x = max(point.x for point in points)
    min_y = min(point.y for point in points)
    max_y = max(point.y for point in points)

    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2
    width = max_x - min_x
    height = max_y - min_y

    return Rectangle2D(center_x, center_y, width, height)

def draw(rect):
    penup()
    goto(rect.center_x - rect.width / 2, rect.center_y + rect.height / 2)
    pendown()
    #draw rect
    forward(rect.width) 
    right(90)
    forward(rect.height)
    right(90)
    forward(rect.width) 
    right(90)
    forward(rect.height)
    
    
points_input = input("Enter point (x1,y1,x2,y2....)\n")
points_data = list(map(float, points_input.split()))
points = [Point(points_data[i], points_data[i+1]) for i in range(0, len(points_data), 2)]


rectangle = getRectangle(points)
draw(rectangle)

print(rectangle)

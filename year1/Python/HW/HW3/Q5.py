import math

#input
x1 = int(input("Please input x1 : "))
y1 = int(input("Please input y1 : "))
x2 = int(input("Please input x2 : "))
y2 = int(input("Please input y2 : "))
x3 = int(input("Please input x3 : "))
y3 = int(input("Please input y3 : "))

#triangle formula
area = abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2) / 2.0))

#Output
print("The area of triangle is : ", area)

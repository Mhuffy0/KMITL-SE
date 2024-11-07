#Problem 1
def input_str(prompt): #ensure input is srting
    while True:
        user_input = input(prompt)
        if user_input: #check input is non-empty
            return user_input
        else:
            print("Invalid Please input a string.")

def input_pos(prompt): #positive number input function
    while True:
        try:
            value = float(input(prompt)) #try value into float type
            if value >= 0:
                return value 
            #check if value isnt negative
            else :
                print("Invalid value")
        except ValueError: #incase its not number
            print("Error. Input Number")

name = input_str("Please enter Employee's name : ")
work_hour = input_pos("Please enter worked hour in a week : ")
pay_rate = input_pos("Please enter Hourly pay rate : ")
federal_tax = input_pos("Please enter Federal tax withholding rate : ")
stats_tax = input_pos("Please enter State tax withholding rate : ")

print("")
#Calculations
gross_pay = work_hour * pay_rate
f_hold = gross_pay * federal_tax
s_hold = gross_pay * stats_tax
total = f_hold + s_hold

net_pay = gross_pay - total

print("\nEmployee Name : ", name)
print("Hour Worked : ", work_hour)
print("Pay Rate : ${:.2f}".format(pay_rate))
print("Gross Pay : ${:.2f}".format(gross_pay))
print("Deductions: ")
print(" Federal Witholding ({:.1%}) : ${:.2f}".format(federal_tax, f_hold))
print(" State Witholding ({:.1%}) : ${:.2f}".format(stats_tax, s_hold))
print(" Total Deduction : ${:.2f}".format(total))
print("Net Pay : ${:.2f}".format(net_pay))

#Problem 2 
def input_fourdigit(prompt): #function check input
    while True:
        try:
            user_input = input(prompt) #input as string so we can reverse it
            if user_input.isdigit() and len(user_input) == 4 : #check if it's digit and 4 numbers or not
                return user_input
            else:
                print("Please input 4 digits numbers.")
        except ValueError:
            print("Please input 4 digits numbers")

num = input_fourdigit("Enter 4 digits numbers : ")
reverse_num = num[::-1] #reversed the value
print("Reversed number = ",reverse_num)


#Problem 3

import turtle as tt

def draw_star(length):
    star = tt.Turtle()
    for _ in range(5):
        star.forward(length)
        star.right(144)
        
length = float(input("Enter the length of star : "))
draw_star(length)
tt.done
        
        
#Problem 4
import turtle as tt

def draw_ring(radius):
    color = ["blue", "black", "red", "yellow", "green"]
    position = [(-120, 0), (0, 0), (120, 0), (-60, -60), (60, -60)]
    
    for color, position in zip(color, position):
        tt.pensize(5)
        tt.penup()
        tt.goto(position)
        tt.pendown()
        tt.color(color)
        tt.circle(radius)
    
radius = float(input("Enter radius : "))
draw_ring(radius)

#Problem 5
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


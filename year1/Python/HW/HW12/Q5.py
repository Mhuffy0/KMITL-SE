import turtle as t 
from abc import ABC, abstractmethod

class Char(ABC):
    @abstractmethod
    def draw(self):
        t.goto(self.x, self.y)
    
    @abstractmethod
    def getW(self):
        return
    
class Char0(Char):
    def draw(self, x, y):
        t.penup()
        t.goto(x, y)
        #t.backward(20)
        t.pendown()
        
        #draw
        for i in range(2):
            t.forward(20)
            t.left(90)
            t.forward(40)
            t.left(90)
        
        t.penup()
        
    def getW(self):
        return 40
    
class Char1(Char):
    def draw(self, x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
        
        t.left(90)
        t.forward(40)
        
        t.left(135)
        t.forward(12)
        
        t.right(135)
        t.right(90)
        t.penup()
        
    def getW(self):
        return 17
    
class Char2(Char):
    def draw(self,x,y):
        t.penup()
        t.goto(x, y)
        
        t.left(90)
        t.forward(40)
        t.right(90)
        t.pendown()
        
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.left(90)
        t.forward(20)
        t.left(90)
        t.forward(20)
        
    def getW(self):
        return 35
    
class Char3(Char):
    def draw(self,x,y):
        t.penup()
        t.goto(x, y)
        t.pendown()
        
        t.forward(20)
        
        for i in range(2):
            t.left(90)
            t.forward(20)
            t.left(90)
            t.forward(20)
            t.right(180)
            t.forward(20)
    
    def getW(self):
        return 35
    
class Char4(Char):
    def draw(self,x,y):
        t.penup()
        t.goto(x, y)
        t.forward(20)
        t.pendown()
        
        t.left(90)
        t.forward(40)
        t.backward(20)
        t.left(90)
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.right(90)
        
        
    def getW(self):
        return 35
        
        
class Char5(Char):
    def draw(self,x,y):
        t.penup()
        t.goto(x, y)
        t.forward(20)
        t.left(90)
        t.forward(40)
        t.left(90)
        t.pendown()
        
        t.forward(20)
        t.left(90)
        t.forward(20)
        t.left(90)
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.right(90)
        t.forward(20)
        
        t.left(180)
        
    
    def getW(self):
        return 40
    
    
class Char6(Char):
    def draw(self,x,y):
        t.penup()
        t.goto(x,y)
        t.pendown()
        
        t.left(90)
        t.forward(40)
        t.right(90)
        t.forward(20)
        t.backward(20)
        t.left(90)
        t.backward(40/2)
        t.right(90)
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.left(180)
    
    def getW(self):
        return 30
    
class Char7(Char):
    def draw(self,x,y):
        t.penup()
        t.goto(x,y)
        
        t.left(90)
        t.forward(40)
        t.right(90)
        t.pendown()
        
        t.forward(20)
        t.right(90)
        t.right(45)
        t.forward(20)
        t.left(45)
        t.forward(25)
        t.left(90)
        
    def getW(self):
        return 30
    
class Char8(Char):
    def draw(self,x,y):
        t.penup()
        t.goto(x,y)
        t.pendown()
        
        t.left(90)
        t.forward(40)
        t.right(90)
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.backward(20)
        t.left(90)
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.left(180)
    
    def getW(self):
        return 30
    
class Char9(Char):
    def draw(self,x,y):
        t.penup()
        t.goto(x,y)
        
        t.forward(20)
        t.left(90)
        t.pendown()
        t.forward(40)
        t.left(90)
        for i in range(4):
            t.forward(20)
            t.left(90)
        t.right(180)
    
    def getW(self):
        return 30
    
#H 40
# width 20

# def drawNum(nums):
#     digits = {
#         0: Char0(),
#         1: Char1(),
#         #continue ja
#     }
    
#     x = 0
#     y = 0
    
#     curr_x = x
    
#     for ch in nums:
#         try:
#             digit = int(ch)
            
#         except ValueError :
#             print("what is this shiiii?")
#             continue
        
#         if digit in digits:
#             obj = digits[digit]
#             obj.draw(curr_x, y)#draw start
#             print(obj.getW())
            
#             # Update X pos
#             curr_x += obj.getW()
#         else:
#             print("What is this shi?")


def drawNum(nums):
    digits = {
        0: Char0(),
        1: Char1(),
        2: Char2(),
        3: Char3(),
        4: Char4(),
        5: Char5(),
        6: Char6(),
        7: Char7(),
        8: Char8(),
        9: Char9(),
    }
    
    x = 0
    y = 0
    
    curr_x = x 
    total_w = 0
    
    for ch in nums:
        try:
            digit = int(ch)
        except ValueError:
            print(f"tf is : {ch}")
            continue
        
        if digit in digits:
            obj = digits[digit]

            obj.draw(curr_x, y)

            print(f"Width {digit}: {obj.getW()}")
            total_w += obj.getW()
            curr_x += obj.getW()
        else:
            print("Err")
            
#main
t.speed(-1)
t.pensize(7)

objs = input("Enter Numbersss : ")
drawNum(objs)


t.done()
def text(s):
    abb = {
        'be': 'b', 
        'because': 'cuz',
        'see': 'c',
        'the': 'da',
        'okay': 'ok',
        'are': 'r',
        'you': 'u',
        'without': 'w/o',
        'why': 'y',
        'see you': 'cu',
        'ate': '8',
        'great': 'gr8',
        'mate': 'm8',
        'wait': 'w8',
        'later': 'l8r',
        'tomorrow': '2mro',
        'for': '4',
        'before': 'b4',
        'once': '1ce',
        'and': '&',
        'your': 'ur',
        'you’re': 'ur',
        'as far as I know': 'afaik',
        'as soon as possible': 'ASAP',
        'at the moment': 'atm',
        'be right back': 'brb',
        'by the way': 'btw',
        'for your information': 'FYI',
        'in my humble opinion': 'imho',
        'in my opinion': 'imo',
        'laughing out loud': 'lol',
        'oh my god': 'omg',
        'rolling on the floor laughing': 'rofl',
        'talk to you later': 'ttyl'
    }
    
    words = s.split()
    
    result = []
    i = 0
    while i < len(words):
        if i + 3 <= len(words) and ' '.join(words[i:i+4]) in abb:
            result.append(abb[' '.join(words[i:i+4])])
            i += 4
        elif i + 2 <= len(words) and ' '.join(words[i:i+3]) in abb:
            result.append(abb[' '.join(words[i:i+3])])
            i += 3
        elif i + 1 <= len(words) and ' '.join(words[i:i+2]) in abb:
            result.append(abb[' '.join(words[i:i+2])])
            i += 2
        else:
            result.append(abb.get(words[i], words[i]))
            i += 1
    
    return ' '.join(result)

def rev_text(s):
    rev_abb = {
        'b': 'be', 
        'cuz': 'because',
        'c': 'see',
        'da': 'the',
        'ok': 'okay',
        'r': 'are',
        'u': 'you',
        'w/o': 'without',
        'y': 'why',
        'cu': 'see you',
        '8': 'ate',
        'gr8': 'great',
        'm8': 'mate',
        'w8': 'wait',
        'l8r': 'later',
        '2mro': 'tomorrow',
        '4': 'for',
        'b4': 'before',
        '1ce': 'once',
        '&': 'and',
        'ur': 'your',
        'afaik': 'as far as I know',
        'ASAP': 'as soon as possible',
        'atm': 'at the moment',
        'brb': 'be right back',
        'btw': 'by the way',
        'FYI': 'for your information',
        'imho': 'in my humble opinion',
        'imo': 'in my opinion',
        'lol': 'laughing out loud',
        'omg': 'oh my god',
        'rofl': 'rolling on the floor laughing',
        'ttyl': 'talk to you later'
    }
    
    words = s.split()
    result = []
    i = 0
    while i < len(words):
        if i + 3 <= len(words) and ' '.join(words[i:i+4]) in rev_abb:
            result.append(rev_abb[' '.join(words[i:i+4])])
            i += 4
        elif i + 2 <= len(words) and ' '.join(words[i:i+3]) in rev_abb:
            result.append(rev_abb[' '.join(words[i:i+3])])
            i += 3
        elif i + 1 <= len(words) and ' '.join(words[i:i+2]) in rev_abb:
            result.append(rev_abb[' '.join(words[i:i+2])])
            i += 2
        else:
            result.append(rev_abb.get(words[i], words[i]))
            i += 1
    
    return ' '.join(result)

message = 'see you tomorrow at the moment mate as soon as possible'
abb = text(message)
print(abb)
print(rev_text(abb))


def composite(dict1, dict2):
    dict3 = {}
    for k,m in dict1.items():
        if m in dict2:
            dict3[k] = dict2[m]
    return dict3

dict1 = {'a': 'p', 'b': 'r', 'c': 'q', 'd': 'p', 'e': 'g'}
dict2 = {'p': '1', 'q': '2', 'r': '3'}
result = composite(dict1, dict2)
print(result)

from itertools import product

def cartersian(*s):
    return set(product(*s))

s1 = {1, 2, 3}
s2 = {'p', 'q'}
s3 = {'a', 'b', 'c'}
result = cartersian(s1, s2, s3)
print(result)

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
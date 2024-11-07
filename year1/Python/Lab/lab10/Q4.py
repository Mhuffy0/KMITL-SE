from collections import Counter
import turtle

t1 = turtle.Turtle()
t2 = turtle.Turtle()

def draw_chart(n, tx):
    for i in range(2):    
        t2.fd(10)
        t2.left(90)
        t2.fd(20*n)
        t2.left(90)
    t2.right(90)
    t2.penup()
    t2.fd(20)
    t2.left(90)
    t2.write(tx, align="left", font=("Arial", 12, "normal"))
    t2.fd(10)
    t2.left(90)
    t2.fd(20)
    t2.right(90)
    t2.pendown()
    t2.fd(20)

def histrogram(inp):    
    count = Counter(inp)

    co = []
    ls = []
    for num,counts in count.items():
        co.append(counts)
        ls.append(num)

    t1.left(90)
    t1.fd((max(co) * 20) + 10)
    t2.fd(20)
    for i in range(len(ls)):
        draw_chart(co[i],ls[i])

    turtle.done()

a = [1,2,2,1,3,4,6,5,3,4,5,6,4,3,5,4,5,3,4,4,3,3,4,3,3,4,4,4]
a.sort()
histrogram(a)
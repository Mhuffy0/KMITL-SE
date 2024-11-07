import turtle

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

inp = str(input("Enter some text: "))

ls = []
co = []
for i in inp:
    count = 0
    for j in inp:
        if i == j:
            count += 1
        else:
            continue
    if i in ls:
        continue
    else:
        ls.append(i)
        co.append(count)

t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.left(90)
t1.fd((max(co) * 20) + 10)
t2.fd(20)
for i in range(len(ls)):
    draw_chart(co[i],ls[i])

turtle.done()
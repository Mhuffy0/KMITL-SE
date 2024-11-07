inp1 = int(input("Input Integer: "))
out1 = str()
if inp1 == 0: 
    print("It's zero")
    quit
elif inp1 < 0:
    print("It's negative")
    quit
else:
    while inp1 >= 1:
        out1 = str(inp1%2) + out1[0:]
        inp1 = inp1//2
print(f"Your binary number is: {out1}")



inp2 = str(input("Input Binary: "))
sum = 0
count1 = 1
check = inp2
while len(check) > 0:
    if check[-1] in '01':
        check = str(check[0:len(check)-1])
    else: 
        break
if len(check) > 0:
    print("Not a binary number")
    quit
elif inp2[0] == '-':
    print("It is negative")
    quit
elif inp2 == "0":
    print("It is zero")
    quit
else:
    for i in inp2:
        if i not in "01":
            quit
        else:
            continue
    while count1 <= len(inp2):
        sum += 2**(count1-1) * int(inp2[-count1])
        count1 += 1
    print(f"Your number is: {sum}")
    
    
    inp = str(input("Enter some text: "))
print("-- Caracter Frequency Table -")
c = []
for i in inp:
    count = 0
    for j in inp:
        if i == j:
            count += 1
        else:
            continue
    per = round((count / len(inp)) *100,2)
    if i in c:
        continue
    else:    
        if per >= 10:
            print(f'{i}    {per}%')
        else:
            print(f'{i}     {per}%')
        c.append(i)
        
        
        
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



inp = str(input("Enter the first 9 digit of an ISBN-10 as a string: "))
num = 0 
for i in range(len(inp)):
    num += int(inp[i]) * (i+1)
checksum = num%11
if checksum == 10:
    checksum = 'X'

print(f"Your ISBN-10 number is {inp}"+f"{checksum}")
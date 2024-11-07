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
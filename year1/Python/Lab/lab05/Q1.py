print("Pattern A")
for i in range(1,6):
    for x in range(1, i+1):
        print("",format(x), end='')
    print()
    
print("Pattern B")
for i in range(6, 0, -1):
    for x in range(i, 0, -1):
        print("",format(x), end='')
    print()
    

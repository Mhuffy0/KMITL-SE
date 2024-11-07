line = int(input("Enter the number of lines : "))

if line % 2 == 0:
    for x in range(1, (line - (line // 2)) + 1):
        num = 1
        row = []
        for i in range(x):
            row.append(num)
            num *= 2
        row.reverse()
        for j in row:
                print(j, end=' ')
        print()
            
    for x in range((line - (line // 2)), 0,  -1):
        num = 1
        row = []
        for i in range(x):
            row.append(num)
            num *= 2
        row.reverse()
        for j in row:
                print(j, end=' ')
        print()
        
else:
    print("Test")
    for x in range(1, (line - ((line + 1) // 2)) + 1):
        num = 1
        row = []
        for i in range(x):
            row.append(num)
            num *= 2
        row.reverse()
        for j in row:
            print(j, end=' ')
        print()
            
    for x in range((line - ((line - 1) // 2)), 0,  -1):
        num = 1
        row = []
        for i in range(x):
            row.append(num)
            num *= 2
        row.reverse()
        for j in row:
            print(j, end=' ')
        print()
        

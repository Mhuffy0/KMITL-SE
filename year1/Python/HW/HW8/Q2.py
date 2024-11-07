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
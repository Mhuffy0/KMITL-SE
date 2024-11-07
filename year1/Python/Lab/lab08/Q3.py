short = str(input("short : "))
long = str(input("long : "))
found = False

for i in range(len(long) - len(short) + 1):
        if long[i:i+len(short)] == short:
            found = True
            break
        
print(found)
        
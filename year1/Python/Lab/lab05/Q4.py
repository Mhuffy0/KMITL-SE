i = 0
while i < 49:
    i += 1
    if i %3 == 0:
        continue
    if i == 1:
        print(i, end='')
    else :
        print(end=',')
        print(i, end='')
    
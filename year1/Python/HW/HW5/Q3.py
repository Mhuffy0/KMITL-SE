while True :
    try:
        num = int(input("Enter a num that >=1 : "))
        if num < 1:
            print("Enter >= 1")
            continue
        break
    except ValueError:
        print("Error")
        
n = num
while num > 0:
    for i in range(1, num + 1):
        print('*' * i)

    for i in range(num - 1, 1, -1):
        print('*' * i)
    num = num - 1
    
if n > 1:
    print("*")
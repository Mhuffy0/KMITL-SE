def rev(num):
    reversed_num = 0
    
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    print("Reversed Number is : " + str(reversed_num))
    
rev(6543)
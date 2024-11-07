inp = str(input("Enter the first 9 digit of an ISBN-10 as a string: "))
num = 0 
for i in range(len(inp)):
    num += int(inp[i]) * (i+1)
checksum = num%11
if checksum == 10:
    checksum = 'X'

print(f"Your ISBN-10 number is {inp}"+f"{checksum}")
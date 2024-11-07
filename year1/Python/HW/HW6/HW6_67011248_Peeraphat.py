#1
print("Please Enter the time")
try :
    hour = int(input("Hour : "))
    min = int(input("min : "))
    if min >= 0 and min <= 60 :
        if hour > 12 and hour <= 24 : 
            new_hour = hour - 12
            print(f"Hour : {new_hour:02d}"+f":{min:02d} PM")
        elif hour <= 12:
            new_hour = hour
            print(f"Hour : {new_hour:02d}"+f":{min:02d} AM")
        else :
            print("Err")
    else :
        print("Err")
except: 
    print("Err")
    
#2
try :
    num = int(input("Input num in range 0 - 999 : \n"))
except :
    print("Err")
    
ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
hundreds = ["", "hundred"]

if num == 0:
    0
    
word = ""

if num >= 100 :
    word += ones[num // 100] + " " + hundreds[1]
    num %= 100
    if num > 0 :
        word += " and "
     
if 10 < num < 20 :
     word += teens[num - 10]
else :
    word += tens[num // 10]
    if (num % 10) > 0 :
        if word :
            word += " - "
        word += ones[num % 10]

if 0 <= num <= 999:
    print(word)
else :
    print("I dont know.")
    
#3
try :
    amount = int(input("Enter money : \n"))
except :
    print("Err")
    
denom = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
count = {}

for den in denom:
    count[den] = amount // den
    amount %= den
    
print("\nnotes and coins :")
for den in denom:
    if count[den] > 0 :
        label = "notes" if den >= 20 else "coins"
        print(f"{den: > 4} Baht {label} : {count[den]}")
        
#4
def rev(num):
    reversed_num = 0
    
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    print("Reversed Number is : " + str(reversed_num))
    
rev(6543)

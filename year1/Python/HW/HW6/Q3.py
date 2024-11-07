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
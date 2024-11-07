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
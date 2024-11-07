score = float(input("Enter a score: "))
if score in range(0, 101):
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"
    print("Your grade:", grade)
else:
    print("Please enter your score between 1-100.")
        

    
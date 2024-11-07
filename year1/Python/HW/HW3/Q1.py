def input_str(prompt): #ensure input is srting
    while True:
        user_input = input(prompt)
        if user_input: #check input is non-empty
            return user_input
        else:
            print("Invalid Please input a string.")

def input_pos(prompt): #positive number input function
    while True:
        try:
            value = float(input(prompt)) #try value into float type
            if value >= 0:
                return value 
            #check if value isnt negative
            else :
                print("Invalid value")
        except ValueError: #incase its not number
            print("Error. Input Number")

name = input_str("Please enter Employee's name : ")
work_hour = input_pos("Please enter worked hour in a week : ")
pay_rate = input_pos("Please enter Hourly pay rate : ")
federal_tax = input_pos("Please enter Federal tax withholding rate : ")
stats_tax = input_pos("Please enter State tax withholding rate : ")

print("")
#Calculations
gross_pay = work_hour * pay_rate
f_hold = gross_pay * federal_tax
s_hold = gross_pay * stats_tax
total = f_hold + s_hold

net_pay = gross_pay - total

print("\nEmployee Name : ", name)
print("Hour Worked : ", work_hour)
print("Pay Rate : ${:.2f}".format(pay_rate))
print("Gross Pay : ${:.2f}".format(gross_pay))
print("Deductions: ")
print(" Federal Witholding ({:.1%}) : ${:.2f}".format(federal_tax, f_hold))
print(" State Witholding ({:.1%}) : ${:.2f}".format(stats_tax, s_hold))
print(" Total Deduction : ${:.2f}".format(total))
print("Net Pay : ${:.2f}".format(net_pay))
def input_fourdigit(prompt): #function check input
    while True:
        try:
            user_input = input(prompt) #input as string so we can reverse it
            if user_input.isdigit() and len(user_input) == 4 : #check if it's digit and 4 numbers or not
                return user_input
            else:
                print("Please input 4 digits numbers.")
        except ValueError:
            print("Please input 4 digits numbers")

num = input_fourdigit("Enter 4 digits numbers : ")
reverse_num = num[::-1] #reversed the value
print("Reversed number = ",reverse_num)

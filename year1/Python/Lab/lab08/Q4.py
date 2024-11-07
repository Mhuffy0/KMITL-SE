
first_name = str(input("First name : "))
last_name = str(input("Last name : "))
gender = str(input("Male (m) or Female (f) ?\n"))

match gender:
    case 'm':
        gender = 'M'
    case 'f':
        gender = 'F'

                
username = gender + last_name[0] + first_name[0:6]
print(username.upper())
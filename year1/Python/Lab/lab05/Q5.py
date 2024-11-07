while True:
        ch = input("Please enter a character : ")
        if len(ch) == 1 or ch.isnumeric():
            if ch == "\t":
                print("Bye see you tmrw.")
                break
            else :
                ascii_value = ord(ch)
                if 0x30 <= ascii_value <= 0x39:
                    print(f"{ch} is a numeric character.")

                elif 0x41 <= ascii_value <= 0x5A:
                    print(f"{ch} is a capital letter and its small-case letter is {chr(ascii_value + 32)}.")

                elif 0x61 <= ascii_value <= 0x7A:
                    print(f"{ch} is a small-case letter and its capital letter is {chr(ascii_value - 32)}.")

                else:
                    print(f"{ch} is a special character.")
        else : 
            print("Enter 1 character only.")
            continue


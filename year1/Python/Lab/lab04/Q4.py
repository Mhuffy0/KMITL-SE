def check_char_type(ch):
    ascii_value = ord(ch)

    if 0x30 <= ascii_value <= 0x39:
        print(f"{ch} is a numeric character.")

    elif 0x41 <= ascii_value <= 0x5A:
        print(f"{ch} is a capital letter and its small-case letter is {chr(ascii_value + 32)}.")

    elif 0x61 <= ascii_value <= 0x7A:
        print(f"{ch} is a small-case letter and its capital letter is {chr(ascii_value - 32)}.")

    else:
        print(f"{ch} is a special character.")

char = input("Please enter a character : ")
check_char_type(char)
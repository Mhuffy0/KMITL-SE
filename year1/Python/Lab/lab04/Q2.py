number = eval(input("Enter something : "))

if type(number) == float :
    mode = input("Display in (f)loating point or (s)cientific format?")
    if mode == "f":
        print("{:.2f}".format(number))
    elif mode == "s":
        print("{:.2e}".format(number))
    else:
        print("Invalid mode")
        
elif type(number) == int:
    mode = input("Display in (b)inary, (o)ctal, (h)exadecimal, or (d)ecimal? ")
    if mode == "b":
        print("Binary:", bin(int(number)).replace("0b", ""))
    elif mode == "o":
        print("Octal:", oct(int(number)).replace("0o", ""))
    elif mode == "h":
        print("Hexadecimal:", str(hex(int(number))).replace("0x", ""))
    elif mode == "d":
        print("Decimal:", float(number))
    else:
        print("Invalid mode")
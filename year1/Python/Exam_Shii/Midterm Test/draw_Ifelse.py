import turtle
print("Hello! Rust better")

while True :
    user = input("Turtle |>")
    if user == "fd":
            fd = int(input("please enter number :"))
            turtle.forward(fd)
    elif user =="back" :
            b = int(input("please enter number :"))
            turtle.backward(b)
        
    elif user == "lt" :
            fd = int(input("please enter number :"))
            turtle.left(fd)
        
    elif user == "rt" :
            fd = int(input("please enter number :"))
            turtle.right(fd)
        
    elif user == "pu" :
            print("penup!!")
            turtle.penup()
        
    elif user == "pd" :
            print("pendown")
            turtle.pendown()
            
    elif user == "reset" :
            turtle.reset()
            
    elif user == "quit" :
            print("exit fuck u....")
            break
        
    else:
            print("Err")
        
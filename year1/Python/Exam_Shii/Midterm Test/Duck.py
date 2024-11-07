import turtle
print("Hello! Rust better")

while True :
    user = input("Turtle |>")
    match user :
        case "fd" | "forward" | "Forward" :
            fd = int(input("please enter number :"))
            turtle.forward(fd)
        case "back" | "backward" | "Back" :
            b = int(input("please enter number :"))
            turtle.backward(b)
        
        case "lt" | "left" | "Left" :
            fd = int(input("please enter number :"))
            turtle.left(fd)
        
        case "rt" | "right" | "Right" :
            fd = int(input("please enter number :"))
            turtle.right(fd)
        
        case "pu" | "penup" | "Penup" :
            print("penup!!")
            turtle.penup()
        
        case "pd" | "pendown" | "Pendown" :
            print("pendown")
            turtle.pendown()
            
        case "reset" :
            turtle.reset()
            
        case "quit" | "Quit" :
            print("exit fuck u....")
            break
        
        case _ :
            print("Err")
        
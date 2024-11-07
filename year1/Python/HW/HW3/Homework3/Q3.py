import turtle as tt

def draw_star(length):
    star = tt.Turtle()
    for _ in range(5):
        star.forward(length)
        star.right(144)
        
length = float(input("Enter the length of star : "))
draw_star(length)
tt.done
        
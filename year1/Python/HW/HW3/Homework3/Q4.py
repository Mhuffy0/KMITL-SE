import turtle as tt

def draw_ring(radius):
    color = ["blue", "black", "red", "yellow", "green"]
    position = [(-120, 0), (0, 0), (120, 0), (-60, -60), (60, -60)]
    
    for color, position in zip(color, position):
        tt.pensize(5)
        tt.penup()
        tt.goto(position)
        tt.pendown()
        tt.color(color)
        tt.circle(radius)
    
radius = float(input("Enter radius : "))
draw_ring(radius)

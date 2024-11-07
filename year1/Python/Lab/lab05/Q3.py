import turtle as tt

n = int(input("Input N: "))
tb = 100 / n
window = tt.Screen()
colors = ["Black", "White"]

tt.speed(10)

for i in range(n): 
    for j in range(n):
        tt.fillcolor(colors[(i + j) % 2])
        tt.begin_fill()
        for k in range(4):
            tt.forward(tb)
            tt.right(90)
        tt.end_fill()
        tt.forward(tb)
    tt.goto(0,0 - i*(tb))

    tt.right(90)
    tt.forward(tb)
    tt.left(90)

tt.right(90)

tt.done()
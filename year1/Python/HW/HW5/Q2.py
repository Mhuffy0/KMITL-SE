import turtle as tt

tt.speed(0)
tt.hideturtle()

box_width = 40
box_height = 30
x_start = -140
y_start = 180
days_of_week = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month = 1
start_day = 1
x_position = x_start
y_position = y_start

while month <= 12:
    tt.penup()
    tt.goto(x_position, y_position + 2 * box_height)
    tt.pendown()
    j = 0
    while j < 2:
        tt.forward(7 * box_width)
        tt.right(90)
        tt.forward(3 * box_height)
        tt.right(90)
        j += 1

    tt.penup()
    tt.goto(x_position + 3.5 * box_width, y_position + 2.5 * box_height - 5)
    tt.pendown()
    tt.write(f"Month#{month}", align="center", font=("Arial", 8, "bold"))

    i = 0
    while i < 7:
        tt.penup()
        tt.goto(x_position + i * box_width + box_width / 2, y_position + box_height)
        tt.pendown()
        tt.write(days_of_week[i], align="center", font=("Arial", 10, "normal"))
        i += 1

    y = y_position
    day = 1
    while day <= days_in_month[month - 1]:
        i = 0
        while i < 7:
            x = x_position + i * box_width
            tt.penup()
            tt.goto(x, y)
            tt.pendown()
            j = 0
            while j < 2:
                tt.forward(box_width)
                tt.right(90)
                tt.forward(box_height)
                tt.right(90)
                j += 1
            if day <= days_in_month[month - 1] and (i >= start_day or day > 1):
                tt.penup()
                tt.goto(x + box_width / 2, y - box_height + 5)
                tt.pendown()
                tt.write(str(day), align="center", font=("Arial", 10, "normal"))
                day += 1
            i += 1
        start_day = 0
        y -= box_height

    x_position += 300
    if month % 2 == 0:
        x_position = x_start
        y_position -= 300

    if day > days_in_month[month - 1]:
        start_day = i % 7

    month += 1

tt.done()



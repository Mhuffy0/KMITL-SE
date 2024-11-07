NO 1
ef check_pos(p0, p1, p2):
    cross_product = ((p1[0] - p0[0]) * (p2[1] - p0[1]) - (p1[0] - p0[1] * (p2[0] - p0[0])))
    #check point formula 
    
    if cross_product > 0:
        return "p2 is on the left side of the line p0 p1"
    elif cross_product < 0:
        return "p2 is on the right side of the line p0 p1"
    else:
        return "p2 is on the line p0 p1"
    
p0 = tuple(map(int, input("Enter p0 cordinates in (X, Y) format : ").strip("()").split(",")))
p1 = tuple(map(int, input("Enter p1 cordinates in (X, Y) format : ").strip("()").split(",")))
p2 = tuple(map(int, input("Enter p2 cordinates in (X, Y) format : ").strip("()").split(",")))

result = check_pos(p0, p1, p2)
print("", result)

No 2
def is_inside(r1, r2):
    r1_left = r1['x'] - r1['width'] / 2
    r1_right = r1['x'] + r1['width'] / 2
    r1_top = r1['y'] + r1['height'] / 2
    r1_bottom = r1['y'] - r1['height'] / 2
    
    r2_left = r2['x'] - r2['width'] / 2
    r2_right = r2['x'] + r2['width'] / 2
    r2_top = r2['y'] + r2['height'] / 2
    r2_bottom = r2['y'] - r2['height'] / 2
    
    # Check if r2 is completely inside r1
    return (r2_left >= r1_left and r2_right <= r1_right and
            r2_top <= r1_top and r2_bottom >= r1_bottom)

def is_overlap(r1, r2):
    # Calculate
    r1_left = r1['x'] - r1['width'] / 2
    r1_right = r1['x'] + r1['width'] / 2
    r1_top = r1['y'] + r1['height'] / 2
    r1_bottom = r1['y'] - r1['height'] / 2
    
    r2_left = r2['x'] - r2['width'] / 2
    r2_right = r2['x'] + r2['width'] / 2
    r2_top = r2['y'] + r2['height'] / 2
    r2_bottom = r2['y'] - r2['height'] / 2
    
    # Check if there is an overlap
    return not (r1_left > r2_right or r1_right < r2_left or
                r1_top < r2_bottom or r1_bottom > r2_top)


#input
x1 = float(input("Enter x for center of first rectangle: "))
y1 = float(input("Enter y for center of first rectangle: "))
width1 = float(input("Enter width of first rectangle: "))
height1 = float(input("Enter height of first rectangle: "))

x2 = float(input("Enter x for center of second rectangle: "))
y2 = float(input("Enter y for center of second rectangle: "))
width2 = float(input("Enter width of second rectangle: "))
height2 = float(input("Enter height of second rectangle: "))
    
rect1 = {'x': x1, 'y': y1, 'width': width1, 'height': height1}
rect2 = {'x': x2, 'y': y2, 'width': width2, 'height': height2}
    
# Check if one rectangle is inside the other
if is_inside(rect1, rect2):
    print("The second rectangle is inside the first rectangle.")
elif is_inside(rect2, rect1):
    print("The first rectangle is inside the second rectangle.")
elif is_overlap(rect1, rect2):
    print("The rectangles overlap.")
else:
    print("The rectangles do not overlap and neither is inside the other.")
def check_pos(p0, p1, p2):
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
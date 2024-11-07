def find_depth(i):
    result = 0
    
    if type(i) == int:
        return 0
    
    elif type(i) == list:
        for k in i:
            find_depth(k)
            result+=1
        return result
    
print(find_depth([2,[3,[4]]]))
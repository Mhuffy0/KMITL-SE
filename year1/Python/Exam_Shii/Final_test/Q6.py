#find dup in 2 list

def find(list1, list2):
    result = []
    
    for i in list1:
        if i in list2:
            result.append(i)
            
    return result

list1 = [1,2,3,4,5]
list2 = [5,4,7,8]

print(find(list1,list2))
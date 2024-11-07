def remove_thirds(list):
    x = 0
    for i in range(0,len(list)):
        if (i+1) % 3 == 0 :
            list.pop(i-x)
            x += 1
            
list = [3,6,6,3,7,2,0,1,5,4]

remove_thirds(list)
print(list)
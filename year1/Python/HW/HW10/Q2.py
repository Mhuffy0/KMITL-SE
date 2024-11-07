def bub_sort(result):
    for j in range(0,len(result)-1):
        for i in range(0,len(result)-1):
            if result[i] > result[i+1]:
                result[i], result[i+1] = result[i+1], result[i]
            else:
                continue
    print(result)
    
bub_sort([3,2,9,7,8])
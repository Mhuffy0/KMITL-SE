def merge(l1, l2):
    nlist = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            nlist.append(l1[i])
            i += 1
        else:
            nlist.append(l2[j])
            j += 1

    while i < len(l1):
        nlist.append(l1[i])
        i += 1
        
    while j < len(l2):
        nlist.append(l2[j])
        j += 1

    #for i in range(n):
     #   for k in range(0, n - i - 1):
      #      if result[k] > result[k + 1]:
       #         result[k], result[k + 1] = result[k + 1], result[k]
                
    print(f"merge list is : {nlist}")
    
list1 = [1,5,16,61,111]
list2 = [2,4,5,6]

merge(list1, list2)
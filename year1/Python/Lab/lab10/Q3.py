def get_the_difference(a,b):
    nlist = []
    for i in a:
        if i in b:
            continue
        else:
            nlist.append(i)
    for i in b:
        if i in a:
            continue
        else:
            nlist.append(i)
    print(nlist)

get_the_difference([3,1,1,1,2,7], [4,1,1,2,2,5])
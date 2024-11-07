a = set([1,2,3,4])
b = set([1,2,4])
c = set([1,2,5])

#no oneliner me sad :C

def is_subset(sub,sup):
    for i in sub:
        if i in sup:
            continue
        else:
            return False
    return True
    
print(is_subset(b,a))
print(is_subset(c,a))
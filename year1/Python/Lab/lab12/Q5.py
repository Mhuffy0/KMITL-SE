def power(s):
    s = list(s)
    power_set = set()
    total = 2 ** len(s)
    
    for i in range(total):
        sub = []
        for j in range(len(s)):
            if i & (1 << j):
                sub.append(s[j])
        power_set.add(frozenset(sub))

    return power_set

s = {1, 2, 3}
result = power(s)
print(result)

#convert inside function into frozenset
#output to Set


#s_list = list(s)
#    n = len(s_list)
#    power_set = []
#    for i in range(1 << n):
#        subset = [s_list[j] for j in range(n) if (i & (1 << j)) > 0]
#        power_set.append(set(subset))
#    return power_set

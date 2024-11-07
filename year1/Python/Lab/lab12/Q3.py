def inv_dict(d):
    inverse = {}
    for key, v in d.items():
        if v not in inverse:
            inverse[v] = {key}
        else:
            inverse[v].add(key)
    print(inverse)
    
dict = {'a':1, 'b':2 ,'c':1, 'd':3, 'e':1, 'f':2 }
inv_dict(dict)

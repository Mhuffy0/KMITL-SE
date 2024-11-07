def composite(dict1, dict2):
    dict3 = {}
    for k,m in dict1.items():
        if m in dict2:
            dict3[k] = dict2[m]
    return dict3

dict1 = {'a': 'p', 'b': 'r', 'c': 'q', 'd': 'p', 'e': 'g'}
dict2 = {'p': '1', 'q': '2', 'r': '3'}
result = composite(dict1, dict2)
print(result)
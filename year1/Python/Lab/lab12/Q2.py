def find_duplicates(d):
    dupl = {}
    for key, v in d.items(): #check value and key in Dict
        if list(d.values()).count(v) > 1:
            dupl[key] = v
    print(dupl)

myDict = {'s5301':'Fred', 's5302':'Harry', 's5303':'John', 's5304':'Fred','s5307':'Harry','s5308':'Harry'}
find_duplicates(myDict)
# def find_w(w, list):
#     pos = [ i for i,v in enumerate(list) if w.lower() == v.lower()]
#     return pos if pos else 0

def find(w, list):
    word = w.lower()
    pos = []
    for i,v in enumerate(list):
        if word == v.lower():
            pos.append(i)
    if pos :
        return pos
    else :
        return 0
    
    
w = find("Python", ["pytHon", "ooo", "PYTHON"])

print(w)
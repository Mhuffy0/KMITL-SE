from itertools import product

def cartersian(*s):
    return set(product(*s))

s1 = {1, 2, 3}
s2 = {'p', 'q'}
s3 = {'a', 'b', 'c'}
result = cartersian(s1, s2, s3)
print(result)
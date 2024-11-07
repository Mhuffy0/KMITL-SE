def my_union(list1, list2):
    return list(set(list1 + list2))

def my_intersection(list1, list2):
    return list(set(list1) & set(list2))

def my_difference(list1, list2):
    return list(set(list1) - set(list2))

list1 = [3, 1, 2, 7]
list2 = [4, 1, 2, 5]

print("Union:", my_union(list1, list2)) 
print("Intersection:", my_intersection(list1, list2)) 
print("Difference:", my_difference(list1, list2)) 

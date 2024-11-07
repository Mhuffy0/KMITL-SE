from matplotlib import pyplot as plt
from collections import Counter

def pie_chart(inp):
    count = Counter(inp)

    co = []
    ls = []
    for num,counts in count.items():
        co.append(counts)
        ls.append(num)

    fig = plt.figure(figsize=(10, 7))
    plt.pie(co)

    plt.show()
    
data = [1,2,2,2,3,4,6,5,4,5,3,2,3,4,2,1,2,2,2,1,1,1,3]
pie_chart(data)

def bub_sort(result):
    for j in range(0,len(result)-1):
        for i in range(0,len(result)-1):
            if result[i] > result[i+1]:
                result[i], result[i+1] = result[i+1], result[i]
            else:
                continue
    print(result)
    
bub_sort([3,2,9,7,8])

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


def print_table(table):
    for r in table:
        print("\t".join(str(item) for item in r))

print_table([["X", "Y"], [0, 0], [10, 10], [200, 200]])
print("--------------------------------------------")
print_table([
    ["ID", "Name", "Surname"],
    ["001", "Guido", "Rossum"],
    ["002", "Donald", "Knuth"],
    ["003", "Gordon", "Moore"]
])


def isAnagram(str1, str2):
    return sorted(str1) == sorted(str2)

print(isAnagram("mango", "angom"))
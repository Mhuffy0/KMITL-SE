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
score = {'C++': 99.7,
             'C' : 96.7,
             'Java': 97,
             'Python': 100,
             'C#': 89.4
             }

def rank(score):
    lang = sorted(score.items(), reverse=True, key=lambda item: item[1])#lambda for compare value in item[1]
    ranked = {}
    rank = 1
    
    for subject,score in lang:
        ranked[rank] = subject
        rank +=1
        
    print(ranked)
    
rank(score)
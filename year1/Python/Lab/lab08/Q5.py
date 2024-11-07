def LCS(s1,s2):
    x = 0
    result = str()
    for i in range(len(s1)):
        for j in range(i+1, len(s1)+ 1):
            if s1[i:j] in s2:
                if len(s1[i:j]) > x:
                    result = s1[i:j]
                    x = len(s1[i:j])
    
    return result
    
print(LCS("ingenious", "intelligent"))
print(LCS("philosophically", "zoophilous"))
print(LCS("Love", "War"))
print(LCS("condition", "fictional"))
print(LCS("smart", "meter"))
print(LCS("back-end", "front-end"))


def count(expr):
    if not isinstance(expr, tuple):
        if isinstance(expr, int): #if its int then return 1 if not 0 and loop till no more
            return 1
        else:
            return 0
    
    return sum(count(sub_expr) for sub_expr in expr) #for numbers in expr tuple make it count and sum it

expr1 = (3, 4,'***',6,7)
expr2 = ((((2, '+', 4), '/', 3), '*', 2), '+', (3, '**', 4))
print(count(expr1))
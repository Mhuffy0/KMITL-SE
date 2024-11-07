# Define a recursive function `power(base, exponent)` that calculates the value of `base` raised to the
# power of `exponent`. Assume that both `base` and `exponent` are non-negative integers.
# Example:
# `power(2, 3)` -> 8
# `power(5, 0)` -> 1

def power(base, expo):
    if expo == 0:
        return 1    
    else :
        return base * power(base, expo - 1)
    
print(power(2,3))
print(power(5,0))

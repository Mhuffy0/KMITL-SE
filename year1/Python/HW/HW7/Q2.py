class Poly:
    def __init__(self, val):
        self.val = list(val)
    
    def __str__(self):
        terms = []
        degree = len(self.val) - 1
        for i, coef in enumerate(self.val):
            if coef != 0:
                power = degree - i
                if power == 0:
                    terms.append(f"{coef}")
                elif power == 1:
                    terms.append(f"{coef}x")
                else:
                    terms.append(f"{coef}x^{power}")
        return " + ".join(terms).replace("+ -", "- ")

    def print(self):
        print(self)
    
    def add(self, p):
        max_len = max(len(self.val), len(p.val))
        result = [0] * max_len
        
        for i in range(len(self.val)):
            result[max_len - len(self.val) + i] += self.val[i]
        for i in range(len(p.val)):
            result[max_len - len(p.val) + i] += p.val[i]
        
        return Poly(tuple(result))

    def scalar_multiply(self, n):
        result = [coef * n for coef in self.val]
        return Poly(tuple(result))

    def multiply(self, p):
        # Multiply two polynomials
        result = [0] * (len(self.val) + len(p.val) - 1)
        for i, coef1 in enumerate(self.val):
            for j, coef2 in enumerate(p.val):
                result[i + j] += coef1 * coef2
        return Poly(tuple(result))

    def power(self, n):
        result = Poly((1,))
        for _ in range(n):
            result = result.multiply(self)
        return result

    def diff(self):
        result = []
        degree = len(self.val) - 1
        for i, coef in enumerate(self.val):
            power = degree - i
            if power > 0:
                result.append(coef * power)
        return Poly(tuple(result))

    def integrate(self):
        # Integrate the polynomial
        result = []
        degree = len(self.coefficients)
        for i, coef in enumerate(self.coefficients):
            result.append(coef / (degree - i))
        result.append(0)
        return Poly(tuple(result))

    def eval(self, x):
        # Evaluate the polynomial with x = n
        result = 0
        degree = len(self.val) - 1
        for i, coef in enumerate(self.val):
            result += coef * (x ** (degree - i))
        return result

p = Poly((1, 0, -2))
p.print()
q = p.power(2)
q.print()
print(p.eval(3)) 

# Add p and q
r = p.add(q)
r.print()
r.diff().print() 

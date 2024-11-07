class Clock:
    def __init__(self, hour, min, sec):
        self.hour = hour
        self.min = min
        self.sec = sec
        
    def set_time(self, nh, nm, ns):
        self.hour = nh
        self.min = nm
        self.sec = ns
        
    def get_time(self):
        return (self.hour, self.min, self.sec)
    
    def tick(self):
        self.sec += 1
        if self.sec == 60:
            self.min += 1
            self.sec = 0
            if self.min == 60:
                self.hour += 1
                self.min = 0
                if self.hour == 24:
                    self.hour = 0
                    self.day = 1
                    print(f"{self.hour:02d}:{self.min:02d}:{self.sec:02d}")
    
    def display(self):
        if self.hour == 12 :
            self.new_hour = self.hour
            print(f"Hour : {self.new_hour:02d}"+f":{self.min:02d}:{self.sec:02d} PM")
            
        if self.hour > 12 and self.hour <= 24 : 
            self.new_hour = self.hour - 12
            print(f"Hour : {self.new_hour:02d}"+f":{self.min:02d}:{self.sec:02d} PM")
            
        if self.hour < 12:
            self.new_hour = self.hour
            print(f"Hour : {self.new_hour:02d}"+f":{self.min:02d}:{self.sec:02d} AM")
            
time = Clock(12,40,59)
time.tick()
time.display()
time.set_time(14,43,59)
time.display()


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


class LinearEquation:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
        
    def geta(self):
        return self.__a
    
    def getb(self):
        return self.__b
    
    def getc(self):
        return self.__c
    
    def getd(self):
        return self.__d
    
    def gete(self):
        return self.__e
    
    def getf(self):
        return self.__f
    
    def is_solable(self):
        return (self.__a * self.__d - self.__b * self.__c) != 0
    
    def get_x(self):
        if self.is_solable():
            return (self.__e * self.__d - self.__b * self.__f) / (self.__a * self.__d - self.__b * self.__c)
        else:
            None
            
    def get_y(self):
        if self.is_solable():
            return (self.__a * self.__f - self.__e * self.__c) / (self.__a * self.__d - self.__b * self.__c)
        
equation = LinearEquation(1,2,3,4,5,6)
if equation.is_solable():
    print(f"x= {equation.get_x()} \ny = {equation.get_y()}")
else:
    print("its not solvable")
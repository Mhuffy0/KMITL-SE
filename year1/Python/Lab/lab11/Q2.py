import math

class Calculator:
    def __init__(self,acc = 0.0):
        self.acc = acc
        
    def set_acc(self, a):
        self.acc = a
        
    def get_acc(self):
        return self.acc
        
    def add(self, x):
        self.acc = self.acc + x
        
    def sub(self, x):
        self.acc = self.acc - x
        
    def mul(self, x):
        self.acc = self.acc * x
        
    def divide(self, x):
        self.acc = self.acc / x
        
    def result(self):
        print(f"Result : {self.acc} ")
        
        
class Sci_calc(Calculator):
    def __init__(self, acc=0.0):
        super().__init__(acc)
        
    def square(self):
        self.acc = self.acc**2
    
    def exp(self, x):
        self.acc = self.acc ** x
    
    def fac(self):
        self.acc = math.factorial(self.acc)
        
    def result(self):
        print(f"Result : {self.acc:.1e}")
        
obj = Sci_calc(100)
obj.result()
obj.square()
obj.result()
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
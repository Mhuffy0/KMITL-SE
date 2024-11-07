import math

class QuadraticEquation :
    def __init__(self, a, b, c) -> None:
        self.__a = a
        self.__b = b
        self.__c = c
        
    def get(self) :
        print(f"{self.__a}")
        print(f"{self.__b}")
        print(f"{self.__c}")
        
    def getDiscriminant(self) -> int:
        value = (self.__b**2 ) - (4 * (self.__a * self.__c))
        print(f"{value}")
        if value > 0 :
            self.value = value
        else :
            self.value = 0

    def getRoot1(self) -> int:
        r1 = abs(self.__b) + math.sqrt(self.value)
        r1 = r1 / (2 * self.__a)
        print(f"{r1}")
        r1
    
    def getRoot2(self) -> int:
        r2 = abs(self.__b) - math.sqrt(self.value)
        r2 = r2 / (2 * self.__a)
        print(f"{r2}")
        r2
        
        
QE = QuadraticEquation(1, -3, 2)
QE.getDiscriminant()
QE.get()
QE.getRoot1()
QE.getRoot2()
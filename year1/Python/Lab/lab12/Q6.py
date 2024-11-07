from abc import *

class Transportation(ABC):
    def __init__(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = distance
        
    @abstractmethod
    def find_cost(self):
        pass

class Walk(Transportation):
    def __init__(self, start, end, distance):
        super().__init__(start,end,distance)
        self.start = start
        self.end = end
        self.distance = distance
        
    def find_cost(self):
        return 0
        
class Taxi(Transportation):
    def __init__(self, start, end, distance):
        super().__init__(start, end, distance)
        
    def find_cost(self):
        val = self.distance * 40
        return val
    
class Train(Transportation):
    def __init__(self, start, end, distance, station):
        super().__init__(start,end,distance)
        self.station = station
        
    def find_cost(self):
        cost = self.station*5
        return cost

w1 = Walk("KMITL", "Lawson", 0.6)
t2 = Taxi("Lawson", "Station", 5)
t3 = Train("Ladk", "Paya", 40, 6)
t4 = Taxi("Payathai", "Council", 3)

smth = [w1,t2,t3,t4]
for i in smth:
    cost = i.find_cost()
    start = i.start
    end = i.end
    print(f"from {start} to {end} cost " + str(cost) + " Baht")
    
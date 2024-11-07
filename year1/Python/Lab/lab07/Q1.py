class Time:
    def __init__(self, hour, min, sec) :
        self.hour = hour
        self.min = min
        self.sec = sec
        
    def print(self) :
        print(f"{self.hour:02d}:{self.min:02d}:{self.sec:02d}")
        
    
time1 = Time(12,30,0)
time1.print()
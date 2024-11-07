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
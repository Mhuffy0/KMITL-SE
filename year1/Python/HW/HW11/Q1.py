class Clock:
    def __init__(self, hour, min, sec):
        self.hour = hour
        self.min = min
        self.sec = sec
        
    def set_time(self, nh, nm, ns):
        self.hour = nh
        self.min = nm
        self.sec = ns
    
    def run(self):
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
                    
class AlarmClock(Clock):
    def __init__(self, hour, min, sec, alarm_h, alarm_m, alarm_s, alarm_on_off = bool):
        super().__init__(hour, min, sec)
        self.alarm_h = alarm_h
        self.alarm_m = alarm_m
        self.alarm_s = alarm_s
        self.trigger = alarm_on_off
        
    def set_AlarmTime(self, nh, nm, ns):
        self.alarm_h = nh
        self.alarm_m = nm
        self.alarm_s = ns
        
    def on(self):
        self.trigger = True
        
    def off(self):
        self.trigger = False
        
    def run(self):
        if self.trigger == True:
            while self.hour != self.alarm_h:
                self.sec += 1
                print(f"Time : {self.hour:02d}:{self.min:02d}:{self.sec:02d}") 
                if self.sec == 60:
                    self.min += 1
                    self.sec = 0
                    if self.min == 60:
                        self.hour += 1
                        self.min = 0
                        if self.hour == 24:
                            self.hour = 0
            if self.hour == self.alarm_h:
                print(f"Finished : {self.hour:02d}:{self.min:02d}:{self.sec:02d}") 
                    
obj = AlarmClock(12,00,00,6,30,10,True)
obj.run()
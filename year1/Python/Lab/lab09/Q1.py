from tkinter import *

class Counter:
    def __init__(self):
        w = Tk()
        w.title("Spinner")
        self.count = 0
        self.label = Label(w, text="0", font=("Impact", 30))
        self.label.grid(row=0, column=0)

        frame = Frame(w)
        frame.grid(row=0, column=2) 

        plus = Button(frame, text="+", command=self.add)
        minus = Button(frame, text="-", command=self.minus)
        reset = Button(frame, text="Reset", command=self.reset)

        plus.grid(row=0, column=1)  
        minus.grid(row=1, column=1) 
        reset.grid(row=2, column=1)  

        w.mainloop()
        
    def add(self):
        self.count += 1
        self.label["text"] = str(self.count)
        
    def minus(self):
        self.count -= 1
        self.label["text"] = str(self.count)
        
    def reset(self):
        self.count = 0
        self.label["text"] = str(self.count)

Counter()
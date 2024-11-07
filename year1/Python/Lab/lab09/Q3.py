from tkinter import *

class Draw(Canvas):
    def __init__(self, a, **b) :
                
        super().__init__(a, **b)
        self.bind("<Button-1>", self.save_posn)
        self.bind("<B1-Motion>", self.add_line)
        reset = Button(text="Reset", command=self.reset)
        reset.grid(row=1, column=0)
        
    def save_posn(self, event):
        self.lastx, self.lasty = event.x, event.y

    def add_line(self, event):
        self.create_line((self.lastx, self.lasty, event.x, event.y), width=15, capstyle='round')
        self.save_posn(event)
        
    def reset(self):
        self.delete("all")
    
    
root = Tk()
draw = Draw(root)
draw.grid(column= 0, row= 0)
root.mainloop()

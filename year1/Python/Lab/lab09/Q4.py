from tkinter import *
import tkinter.messagebox
import random

class Point:
    def __init__(self):
        self.w = Tk()
        self.canvas = Canvas(self.w, width=350, height=200, bg="white")
        self.canvas.pack(side="top", fill="both", expand=True)

        self.canvas.create_rectangle(50, 50, 350, 200)

        self.canvas.bind("<Button-1>", self.dot)
        self.w.mainloop()
        
    def dot(self, event) :
        if event.x >= 50 and event.x <= 350 and event.y >= 50 and event.y <= 200:
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = (r,g,b)
            
            self.canvas.create_oval(event.x + 10, event.y + 10, event.x - 10, event.y - 10, fill="#%02x%02x%02x" % color)
        else :
            self.warning()
            
    def warning(self):
        tkinter.messagebox.showinfo("Warning", "Mouse pointer is not in the rect!!") 
        
Point()
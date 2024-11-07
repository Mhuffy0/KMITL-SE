from tkinter import *

class Point:
    def __init__(self):
        self.w = Tk()
        self.canvas = Canvas(self.w, width=350, height=200, bg="white")
        self.canvas.pack(side="top", fill="both", expand=True)

        self.canvas.bind("<Button-1>", self.dot)
        self.canvas.bind("<Button-3>", self.remove) 
        self.w.mainloop()
        
    def dot(self, event):
        self.canvas.create_oval(event.x + 10, event.y + 10, event.x - 10, event.y - 10)
        
    def remove(self, event):
        ol = self.canvas.find_overlapping(event.x - 10, event.y - 10, event.x + 10, event.y + 10)
        for item in ol:
            self.canvas.delete(item)
Point()

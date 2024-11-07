from tkinter import *
import tkinter.messagebox 

class Currency :
    def __init__(self) :
        self.w = Tk()
        self.w.geometry("600x400")
        frame = Frame(self.w)
        frame.grid(row=2, column=1) 
        
        self.amount = IntVar()
        
        Label(self.w, text='Amount', font=('Impact',20,'bold')).grid(row=0)
        am = Entry(self.w, textvariable = self.amount, font=('Impact',10,'normal'))
        am.grid(row=0, column=1)
        
        
        usd = Button(frame, text="USD -> THB", command=self.usd)
        thb = Button(frame, text="THB -> USD", command=self.thb)
        
        usd.grid(row=0, column=0) 
        thb.grid(row=1, column=0) 
        mainloop()
        
    def usd(self):
        temp = int(self.amount.get())
        self.new_amount = temp * 30.0
        tkinter.messagebox.showinfo("USD -> THB" , f"{temp} USD = {self.new_amount:.2f} THB") 
        mainloop()
    
    def thb(self):
        temp = int(self.amount.get())
        self.new_amount = temp / 30.0
        tkinter.messagebox.showinfo("THB -> USD", f"{temp} THB = {self.new_amount:.2f} USD") 
        mainloop()
        
    
    
Currency()
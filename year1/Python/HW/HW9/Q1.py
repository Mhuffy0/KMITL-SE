import tkinter as tk
from tkinter import messagebox

class MobilePhoneUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Mobile Phone")
        
        self.display_var = tk.StringVar()

        self.display = tk.Entry(root, textvariable=self.display_var, font=('Arial', 24), bd=12, insertwidth=2, width=14, borderwidth=4)
        self.display.grid(row=0, column=0, columnspan=3)

        button_texts = [
            ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
            ('*', 4, 0), ('0', 4, 1), ('#', 4, 2),
        ]

        for (text, row, col) in button_texts:
            self.create_button(text, row, col)
        
        self.talk_button = tk.Button(root, text='Talk', padx=20, pady=20, font=('Arial', 18), command=self.talk)
        self.talk_button.grid(row=5, column=0, columnspan=2)
        
        self.delete_button = tk.Button(root, text='<', padx=20, pady=20, font=('Arial', 18), command=self.delete_last_char)
        self.delete_button.grid(row=5, column=2)

    def create_button(self, value, row, col):
        button = tk.Button(self.root, text=value, padx=20, pady=20, font=('Arial', 18), command=lambda: self.button_click(value))
        button.grid(row=row, column=col)

    def button_click(self, value):
        current = self.display_var.get()
        self.display_var.set(current + value)

    def delete_last_char(self):
        current = self.display_var.get()
        self.display_var.set(current[:-1])

    def talk(self):
        current_number = self.display_var.get()
        messagebox.showinfo("Dialing", f"Dialing <<{current_number}>>")


root = tk.Tk()
app = MobilePhoneUI(root)
root.mainloop()

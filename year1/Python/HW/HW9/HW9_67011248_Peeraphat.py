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


import tkinter as tk

class VehicleInventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vroom Ventory")

        # Left sidebar
        sidebar = tk.Frame(root, bg='gray', width=200)
        sidebar.grid(row=0, column=0, rowspan=2, sticky="ns")

        buttons = ["Vehicles", "Images", "Video", "Reviews", "History"]
        for i, btn_text in enumerate(buttons):
            btn = tk.Button(sidebar, text=btn_text, font=('Arial', 14), width=15, height=2)
            btn.grid(row=i, column=0, pady=10, padx=10)

        # Top navigation buttons
        topbar = tk.Frame(root, bg='lightgray', height=50)
        topbar.grid(row=0, column=1, sticky="ew", padx=10, pady=10)

        vehicle_btn = tk.Button(topbar, text="Vehicles", bg='green', fg='white', font=('Arial', 14), width=10)
        vehicle_btn.grid(row=0, column=0, padx=20)

        sales_btn = tk.Button(topbar, text="Sales", bg='green', fg='white', font=('Arial', 14), width=10)
        sales_btn.grid(row=0, column=1, padx=20)

        profile_btn = tk.Button(topbar, text="Profile", bg='green', fg='white', font=('Arial', 14), width=10)
        profile_btn.grid(row=0, column=2, padx=20)

        # Main area
        main_frame = tk.Frame(root, bg="white", padx=10, pady=10)
        main_frame.grid(row=1, column=1, sticky="nsew")

        # Vehicle details form
        title_label = tk.Label(main_frame, text="Vehicle Details", font=('Arial', 24, 'bold'), bg="white")
        title_label.grid(row=0, column=0, columnspan=4, pady=20)

        labels = [
            "Vehicle Type", "Manufacturer", "Generation", "Engine Size", "Add Images", "Model", "Trim", "Fuel", "Transmission"
        ]
        for i, label in enumerate(labels[:4]):
            tk.Label(main_frame, text=label, font=('Arial', 14), bg="white").grid(row=i+1, column=0, padx=10, pady=10, sticky="w")
            tk.Entry(main_frame, width=20, font=('Arial', 14)).grid(row=i+1, column=1, padx=10, pady=10)

        for i, label in enumerate(labels[4:]):
            tk.Label(main_frame, text=label, font=('Arial', 14), bg="white").grid(row=i+1, column=2, padx=10, pady=10, sticky="w")
            tk.Entry(main_frame, width=20, font=('Arial', 14)).grid(row=i+1, column=3, padx=10, pady=10)

        # Transmission Checkboxes
        tk.Checkbutton(main_frame, text="Automatic", font=('Arial', 14), bg="white").grid(row=5, column=2, padx=10, pady=10, sticky="w")
        tk.Checkbutton(main_frame, text="Manual", font=('Arial', 14), bg="white").grid(row=6, column=2, padx=10, pady=10, sticky="w")

        # Save Button
        save_btn = tk.Button(main_frame, text="Save", bg='green', fg='white', font=('Arial', 18), width=10)
        save_btn.grid(row=7, column=3, pady=20)


root = tk.Tk()
root.geometry("800x600")
app = VehicleInventoryApp(root)
root.mainloop()


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

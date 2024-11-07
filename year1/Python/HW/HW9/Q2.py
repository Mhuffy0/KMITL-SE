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

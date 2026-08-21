import tkinter as tk
from tkinter import messagebox, ttk


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversion & Interest Calculator")
        self.root.geometry("820x620")
        self.root.minsize(700, 540)
        self.root.configure(bg="#edf1f5")
        self.entries = {}
        self.setup_styles()
        self.build_ui()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Page.TFrame", background="#edf1f5")
        style.configure("Card.TFrame", background="#ffffff")
        style.configure("Title.TLabel", background="#ffffff", foreground="#173c5b", font=("Georgia", 28))
        style.configure("Subtitle.TLabel", background="#ffffff", foreground="#687782", font=("Segoe UI", 11))
        style.configure("Section.TLabel", background="#ffffff", foreground="#173c5b", font=("Segoe UI", 10, "bold"))
        style.configure("Field.TLabel", background="#ffffff", foreground="#405365", font=("Segoe UI", 10))
        style.configure("Result.TFrame", background="#173c5b")
        style.configure("ResultLabel.TLabel", background="#173c5b", foreground="#c7d6e1", font=("Segoe UI", 9, "bold"))
        style.configure("ResultValue.TLabel", background="#173c5b", foreground="#ffffff", font=("Georgia", 24))
        style.configure("Primary.TButton", background="#173c5b", foreground="#ffffff", padding=(20, 11), font=("Segoe UI", 10, "bold"))
        style.configure("Secondary.TButton", background="#ffffff", foreground="#173c5b", padding=(20, 11), font=("Segoe UI", 10))

    def build_ui(self):
        page = ttk.Frame(self.root, style="Page.TFrame", padding=32)
        page.pack(fill="both", expand=True)

        header = ttk.Frame(page, style="Card.TFrame", padding=(34, 28, 34, 25))
        header.pack(fill="x")
        ttk.Label(header, text="FINANCE & UNIT TOOLS", style="Section.TLabel").pack(anchor="w")
        ttk.Label(header, text="Conversion Calculator", style="Title.TLabel").pack(anchor="w", pady=(7, 4))
        ttk.Label(header, text="Choose a calculation and enter the required details.", style="Subtitle.TLabel").pack(anchor="w")

        body = ttk.Frame(page, style="Page.TFrame")
        body.pack(fill="both", expand=True, pady=(16, 0))
        body.columnconfigure(0, weight=1)
        body.columnconfigure(1, weight=1)
        body.rowconfigure(0, weight=1)

        form = ttk.Frame(body, style="Card.TFrame", padding=34)
        form.grid(row=0, column=0, sticky="nsew", padx=(0, 8))
        ttk.Label(form, text="CALCULATION DETAILS", style="Section.TLabel").pack(anchor="w", pady=(0, 24))
        ttk.Label(form, text="Calculation Type", style="Field.TLabel").pack(anchor="w", pady=(0, 5))
        self.choice = ttk.Combobox(form, values=("Celsius to Fahrenheit", "Kilometers to Miles", "INR to USD", "Simple Interest"), state="readonly", font=("Segoe UI", 11))
        self.choice.set("Celsius to Fahrenheit")
        self.choice.pack(fill="x", ipady=5, pady=(0, 22))
        self.choice.bind("<<ComboboxSelected>>", self.update_fields)

        self.fields_frame = ttk.Frame(form, style="Card.TFrame")
        self.fields_frame.pack(fill="x")
        self.update_fields()

        actions = ttk.Frame(form, style="Card.TFrame")
        actions.pack(fill="x", pady=(24, 0))
        ttk.Button(actions, text="Calculate", style="Primary.TButton", command=self.calculate).pack(side="left")
        ttk.Button(actions, text="Clear", style="Secondary.TButton", command=self.clear).pack(side="left", padx=(10, 0))

        result = ttk.Frame(body, style="Result.TFrame", padding=34)
        result.grid(row=0, column=1, sticky="nsew", padx=(8, 0))
        ttk.Label(result, text="CALCULATION RESULT", style="ResultLabel.TLabel").pack(anchor="w")
        self.result_value = ttk.Label(result, text="--", style="ResultValue.TLabel", wraplength=310)
        self.result_value.pack(anchor="w", pady=(65, 12))
        self.expression = ttk.Label(result, text="Enter details to begin", style="ResultLabel.TLabel", wraplength=310)
        self.expression.pack(anchor="w")
        ttk.Separator(result).pack(fill="x", pady=28)
        ttk.Label(result, text="RESULT TYPE", style="ResultLabel.TLabel").pack(anchor="w", pady=(0, 8))
        self.result_type = ttk.Label(result, text="--", style="ResultLabel.TLabel")
        self.result_type.pack(anchor="w")

    def update_fields(self, event=None):
        for widget in self.fields_frame.winfo_children():
            widget.destroy()
        self.entries.clear()
        if self.choice.get() == "Simple Interest":
            fields = (("Principal Amount", "principal"), ("Annual Interest Rate (%)", "rate"), ("Time Period (Years)", "time"))
        else:
            label = {"Celsius to Fahrenheit": "Temperature in Celsius", "Kilometers to Miles": "Distance in Kilometers", "INR to USD": "Amount in INR"}[self.choice.get()]
            fields = ((label, "value"),)
        for label, key in fields:
            ttk.Label(self.fields_frame, text=label, style="Field.TLabel").pack(anchor="w", pady=(0, 5))
            entry = ttk.Entry(self.fields_frame, font=("Segoe UI", 11))
            entry.pack(fill="x", ipady=7, pady=(0, 16))
            self.entries[key] = entry

    def calculate(self):
        try:
            values = {key: float(entry.get().strip()) for key, entry in self.entries.items()}
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter valid numbers in all fields.")
            return
        choice = self.choice.get()
        if choice == "Celsius to Fahrenheit":
            result = values["value"] * 9 / 5 + 32
            expression = f"{values['value']:g} °C = {result:.2f} °F"
        elif choice == "Kilometers to Miles":
            result = values["value"] * 0.621371
            expression = f"{values['value']:g} Km = {result:.4f} Miles"
        elif choice == "INR to USD":
            result = values["value"] / 83
            expression = f"₹{values['value']:g} = ${result:.2f}"
        else:
            result = values["principal"] * values["rate"] * values["time"] / 100
            total = values["principal"] + result
            expression = f"Interest: ₹{result:.2f} | Total: ₹{total:.2f}"
        self.result_value.configure(text=f"{result:.2f}")
        self.expression.configure(text=expression)
        self.result_type.configure(text=type(result).__name__.title())

    def clear(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.result_value.configure(text="--")
        self.expression.configure(text="Enter details to begin")
        self.result_type.configure(text="--")


if __name__ == "__main__":
    app_window = tk.Tk()
    CalculatorApp(app_window)
    app_window.mainloop()
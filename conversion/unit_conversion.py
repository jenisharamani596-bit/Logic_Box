import tkinter as tk
from tkinter import messagebox, ttk


class UnitConversionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Conversion")
        self.root.geometry("760x560")
        self.root.minsize(650, 500)
        self.root.configure(bg="#edf1f5")
        self.create_styles()
        self.create_ui()

    def create_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Page.TFrame", background="#edf1f5")
        style.configure("Card.TFrame", background="#ffffff")
        style.configure("Title.TLabel", background="#ffffff", foreground="#173c5b", font=("Georgia", 30))
        style.configure("Subtitle.TLabel", background="#ffffff", foreground="#687782", font=("Segoe UI", 11))
        style.configure("Section.TLabel", background="#ffffff", foreground="#173c5b", font=("Segoe UI", 10, "bold"))
        style.configure("Field.TLabel", background="#ffffff", foreground="#405365", font=("Segoe UI", 10))
        style.configure("Result.TFrame", background="#173c5b")
        style.configure("ResultLabel.TLabel", background="#173c5b", foreground="#c7d6e1", font=("Segoe UI", 9, "bold"))
        style.configure("ResultValue.TLabel", background="#173c5b", foreground="#ffffff", font=("Georgia", 28))
        style.configure("Primary.TButton", background="#173c5b", foreground="#ffffff", padding=(20, 11), font=("Segoe UI", 10, "bold"))
        style.configure("Secondary.TButton", background="#ffffff", foreground="#173c5b", padding=(20, 11), font=("Segoe UI", 10))

    def create_ui(self):
        page = ttk.Frame(self.root, style="Page.TFrame", padding=32)
        page.pack(fill="both", expand=True)

        header = ttk.Frame(page, style="Card.TFrame", padding=(34, 28, 34, 25))
        header.pack(fill="x")
        ttk.Label(header, text="MEASUREMENT & CURRENCY", style="Section.TLabel").pack(anchor="w")
        ttk.Label(header, text="Unit Conversion", style="Title.TLabel").pack(anchor="w", pady=(7, 4))
        ttk.Label(header, text="Convert values quickly with a clear and simple interface.", style="Subtitle.TLabel").pack(anchor="w")

        body = ttk.Frame(page, style="Page.TFrame")
        body.pack(fill="both", expand=True, pady=(16, 0))
        body.columnconfigure(0, weight=1)
        body.columnconfigure(1, weight=1)
        body.rowconfigure(0, weight=1)

        form = ttk.Frame(body, style="Card.TFrame", padding=34)
        form.grid(row=0, column=0, sticky="nsew", padx=(0, 8))
        ttk.Label(form, text="CONVERSION DETAILS", style="Section.TLabel").pack(anchor="w", pady=(0, 24))

        ttk.Label(form, text="Conversion Type", style="Field.TLabel").pack(anchor="w", pady=(0, 5))
        self.conversion = ttk.Combobox(
            form,
            values=("Celsius to Fahrenheit", "Kilometers to Miles", "INR to USD"),
            state="readonly",
            font=("Segoe UI", 11),
        )
        self.conversion.set("Celsius to Fahrenheit")
        self.conversion.pack(fill="x", ipady=5, pady=(0, 18))

        ttk.Label(form, text="Value", style="Field.TLabel").pack(anchor="w", pady=(0, 5))
        self.value = ttk.Entry(form, font=("Segoe UI", 12))
        self.value.pack(fill="x", ipady=7, pady=(0, 24))
        self.value.focus_set()

        actions = ttk.Frame(form, style="Card.TFrame")
        actions.pack(fill="x")
        ttk.Button(actions, text="Convert", style="Primary.TButton", command=self.convert).pack(side="left")
        ttk.Button(actions, text="Clear", style="Secondary.TButton", command=self.clear).pack(side="left", padx=(10, 0))

        result_card = ttk.Frame(body, style="Result.TFrame", padding=34)
        result_card.grid(row=0, column=1, sticky="nsew", padx=(8, 0))
        ttk.Label(result_card, text="CONVERSION RESULT", style="ResultLabel.TLabel").pack(anchor="w")
        self.result_value = ttk.Label(result_card, text="--", style="ResultValue.TLabel", wraplength=300)
        self.result_value.pack(anchor="w", pady=(65, 12))
        self.expression = ttk.Label(result_card, text="Enter a value to begin", style="ResultLabel.TLabel", wraplength=300)
        self.expression.pack(anchor="w")
        ttk.Separator(result_card).pack(fill="x", pady=28)
        ttk.Label(result_card, text="RESULT TYPE", style="ResultLabel.TLabel").pack(anchor="w", pady=(0, 8))
        self.result_type = ttk.Label(result_card, text="--", style="ResultLabel.TLabel")
        self.result_type.pack(anchor="w")

    def convert(self):
        try:
            source_value = float(self.value.get().strip())
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")
            self.value.focus_set()
            return

        conversion = self.conversion.get()
        if conversion == "Celsius to Fahrenheit":
            result = (source_value * 9 / 5) + 32
            source_unit, target_unit = "°C", "°F"
        elif conversion == "Kilometers to Miles":
            result = source_value * 0.621371
            source_unit, target_unit = "Km", "Miles"
        else:
            result = source_value / 83
            source_unit, target_unit = "INR", "USD"

        self.result_value.configure(text=f"{result:.4f}".rstrip("0").rstrip("."))
        self.expression.configure(text=f"{source_value:g} {source_unit} = {result:.4f} {target_unit}")
        self.result_type.configure(text=type(result).__name__.title())

    def clear(self):
        self.value.delete(0, tk.END)
        self.conversion.set("Celsius to Fahrenheit")
        self.result_value.configure(text="--")
        self.expression.configure(text="Enter a value to begin")
        self.result_type.configure(text="--")
        self.value.focus_set()


if __name__ == "__main__":
    app_window = tk.Tk()
    UnitConversionApp(app_window)
    app_window.mainloop()
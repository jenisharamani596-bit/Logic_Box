import tkinter as tk
from tkinter import messagebox, ttk

class OperatorCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Operator Calculator")
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
        style.configure("ResultValue.TLabel", background="#173c5b", foreground="#ffffff", font=("Georgia", 30))
        style.configure("Primary.TButton", background="#173c5b", foreground="#ffffff", padding=(20, 11), font=("Segoe UI", 10, "bold"))
        style.configure("Secondary.TButton", background="#ffffff", foreground="#173c5b", padding=(20, 11), font=("Segoe UI", 10))

    def create_ui(self):
        page = ttk.Frame(self.root, style="Page.TFrame", padding=32)
        page.pack(fill="both", expand=True)

        header = ttk.Frame(page, style="Card.TFrame", padding=(34, 28, 34, 25))
        header.pack(fill="x")
        ttk.Label(header, text="MATHEMATICAL OPERATIONS", style="Section.TLabel").pack(anchor="w")
        ttk.Label(header, text="Operator Calculator", style="Title.TLabel").pack(anchor="w", pady=(7, 4))
        ttk.Label(header, text="Enter two values and select an operator to calculate.", style="Subtitle.TLabel").pack(anchor="w")

        body = ttk.Frame(page, style="Page.TFrame")
        body.pack(fill="both", expand=True, pady=(16, 0))
        body.columnconfigure(0, weight=1)
        body.columnconfigure(1, weight=1)
        body.rowconfigure(0, weight=1)

        form = ttk.Frame(body, style="Card.TFrame", padding=34)
        form.grid(row=0, column=0, sticky="nsew", padx=(0, 8))
        ttk.Label(form, text="CALCULATION DETAILS", style="Section.TLabel").pack(anchor="w", pady=(0, 24))

        ttk.Label(form, text="First Number", style="Field.TLabel").pack(anchor="w", pady=(0, 5))
        self.first_number = ttk.Entry(form, font=("Segoe UI", 12))
        self.first_number.pack(fill="x", ipady=7, pady=(0, 16))

        ttk.Label(form, text="Operator", style="Field.TLabel").pack(anchor="w", pady=(0, 5))
        self.operator = ttk.Combobox(form, values=("+", "-", "*", "/", "%", "//", "**"), state="readonly", font=("Segoe UI", 12))
        self.operator.set("+")
        self.operator.pack(fill="x", ipady=5, pady=(0, 16))

        ttk.Label(form, text="Second Number", style="Field.TLabel").pack(anchor="w", pady=(0, 5))
        self.second_number = ttk.Entry(form, font=("Segoe UI", 12))
        self.second_number.pack(fill="x", ipady=7, pady=(0, 24))

        actions = ttk.Frame(form, style="Card.TFrame")
        actions.pack(fill="x")
        ttk.Button(actions, text="Calculate", style="Primary.TButton", command=self.calculate).pack(side="left")
        ttk.Button(actions, text="Clear", style="Secondary.TButton", command=self.clear).pack(side="left", padx=(10, 0))

        result_card = ttk.Frame(body, style="Result.TFrame", padding=34)
        result_card.grid(row=0, column=1, sticky="nsew", padx=(8, 0))
        ttk.Label(result_card, text="CALCULATION RESULT", style="ResultLabel.TLabel").pack(anchor="w")
        self.result_value = ttk.Label(result_card, text="--", style="ResultValue.TLabel", wraplength=300)
        self.result_value.pack(anchor="w", pady=(65, 10))
        self.expression = ttk.Label(result_card, text="Enter values to begin", style="ResultLabel.TLabel", wraplength=300)
        self.expression.pack(anchor="w")
        ttk.Separator(result_card).pack(fill="x", pady=28)
        ttk.Label(result_card, text="RESULT TYPE", style="ResultLabel.TLabel").pack(anchor="w", pady=(0, 8))
        self.result_type = ttk.Label(result_card, text="--", style="ResultLabel.TLabel")
        self.result_type.pack(anchor="w")

    def calculate(self):
        try:
            first = float(self.first_number.get().strip())
            second = float(self.second_number.get().strip())
            operator = self.operator.get()
            if operator == "+":
                result = first + second
            elif operator == "-":
                result = first - second
            elif operator == "*":
                result = first * second
            elif operator == "/":
                result = first / second
            elif operator == "%":
                result = first % second
            elif operator == "//":
                result = first // second
            else:
                result = first ** second
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter valid numbers in both fields.")
            return
        except ZeroDivisionError:
            messagebox.showwarning("Invalid Operation", "Division by zero is not allowed.")
            return

        if isinstance(result, float) and result.is_integer():
            result = int(result)
        self.result_value.configure(text=str(result))
        self.expression.configure(text=f"{first:g} {operator} {second:g} = {result}")
        self.result_type.configure(text=type(result).__name__.title())

    def clear(self):
        self.first_number.delete(0, tk.END)
        self.second_number.delete(0, tk.END)
        self.operator.set("+")
        self.result_value.configure(text="--")
        self.expression.configure(text="Enter values to begin")
        self.result_type.configure(text="--")


if __name__ == "__main__":
    app_window = tk.Tk()
    OperatorCalculator(app_window)
    app_window.mainloop()
print("==============================")
print("       OPERATOR CALCULATOR")
print("==============================")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operator (+,-,*,/,%,//,**): ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
elif operator == "%":
    result = num1 % num2
elif operator == "//":
    result = num1 // num2
elif operator == "**":
    result = num1 ** num2
else:
    print("Invalid operator")
    result = None

if result is not None:
    print("Result:", num1, operator, num2, "=", result)
    print("Result type:", type(result))
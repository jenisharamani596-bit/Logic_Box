import tkinter as tk
from tkinter import messagebox, ttk


class PersonalIntroduction:
	def __init__(self, root):
		self.root = root
		self.root.title("Personal Introduction")
		self.root.geometry("920x650")
		self.root.minsize(760, 560)
		self.root.configure(bg="#edf1f5")

		self.entries = {}
		self.preview = {}
		self.setup_styles()
		self.create_page()

	def setup_styles(self):
		style = ttk.Style()
		style.theme_use("clam")
		style.configure("Page.TFrame", background="#edf1f5")
		style.configure("Card.TFrame", background="#ffffff")
		style.configure("Header.TLabel", background="#ffffff", foreground="#173c5b", font=("Georgia", 30))
		style.configure("Subheader.TLabel", background="#ffffff", foreground="#677584", font=("Segoe UI", 11))
		style.configure("Section.TLabel", background="#ffffff", foreground="#173c5b", font=("Segoe UI", 10, "bold"))
		style.configure("Field.TLabel", background="#ffffff", foreground="#405365", font=("Segoe UI", 10))
		style.configure("Summary.TFrame", background="#173c5b")
		style.configure("SummaryLabel.TLabel", background="#173c5b", foreground="#bbcede", font=("Segoe UI", 9, "bold"))
		style.configure("SummaryTitle.TLabel", background="#173c5b", foreground="#ffffff", font=("Georgia", 30))
		style.configure("SummaryValue.TLabel", background="#173c5b", foreground="#ffffff", font=("Georgia", 14))
		style.configure("Primary.TButton", background="#173c5b", foreground="#ffffff", padding=(18, 11), font=("Segoe UI", 10, "bold"))
		style.configure("Secondary.TButton", background="#ffffff", foreground="#173c5b", padding=(18, 11), font=("Segoe UI", 10))

	def create_page(self):
		page = ttk.Frame(self.root, style="Page.TFrame", padding=32)
		page.pack(fill="both", expand=True)

		header = ttk.Frame(page, style="Card.TFrame", padding=(34, 28, 34, 25))
		header.pack(fill="x")
		ttk.Label(header, text="PERSONAL INFORMATION", style="Section.TLabel").pack(anchor="w")
		ttk.Label(header, text="Personal Introduction", style="Header.TLabel").pack(anchor="w", pady=(7, 4))
		ttk.Label(header, text="Complete your details to create a professional introduction profile.", style="Subheader.TLabel").pack(anchor="w")

		body = ttk.Frame(page, style="Page.TFrame")
		body.pack(fill="both", expand=True, pady=(16, 0))
		body.columnconfigure(0, weight=1)
		body.columnconfigure(1, weight=1)
		body.rowconfigure(0, weight=1)

		form = ttk.Frame(body, style="Card.TFrame", padding=34)
		form.grid(row=0, column=0, sticky="nsew", padx=(0, 8))
		ttk.Label(form, text="INTRODUCTION DETAILS", style="Section.TLabel").pack(anchor="w", pady=(0, 24))

		fields = {
			"name": ("Full Name", "Enter your full name"),
			"age": ("Age", "Enter your age"),
			"city": ("City", "Enter your city"),
			"hobby": ("Hobby", "Enter your hobby"),
			"language": ("Language", "Enter your language"),
		}

		for key, (label, placeholder) in fields.items():
			ttk.Label(form, text=label, style="Field.TLabel").pack(anchor="w", pady=(0, 5))
			entry = ttk.Entry(form, font=("Segoe UI", 11))
			entry.pack(fill="x", ipady=7, pady=(0, 15))
			entry.insert(0, placeholder)
			entry.configure(foreground="#8995a1")
			entry.bind("<FocusIn>", lambda event, item=entry, text=placeholder: self.clear_placeholder(item, text))
			entry.bind("<FocusOut>", lambda event, item=entry, text=placeholder: self.restore_placeholder(item, text))
			entry.bind("<KeyRelease>", lambda event: self.update_summary())
			self.entries[key] = (entry, placeholder)

		actions = ttk.Frame(form, style="Card.TFrame")
		actions.pack(fill="x", pady=(8, 0))
		self.submit_button = ttk.Button(actions, text="Submit Information", style="Primary.TButton", command=self.submit)
		self.submit_button.pack(side="left")
		self.reset_button = ttk.Button(actions, text="Reset Form", style="Secondary.TButton", command=self.reset)
		self.reset_button.pack(side="left", padx=(10, 0))
		self.root.bind("<Return>", lambda event: self.submit())

		summary = ttk.Frame(body, style="Summary.TFrame", padding=36)
		summary.grid(row=0, column=1, sticky="nsew", padx=(8, 0))
		ttk.Label(summary, text="PROFILE SUMMARY", style="SummaryLabel.TLabel").pack(anchor="w")
		self.preview["name"] = ttk.Label(summary, text="Your name", style="SummaryTitle.TLabel", wraplength=330)
		self.preview["name"].pack(anchor="w", pady=(48, 5))
		self.preview["city"] = ttk.Label(summary, text="Your city", style="SummaryValue.TLabel")
		self.preview["city"].pack(anchor="w")
		ttk.Separator(summary).pack(fill="x", pady=28)

		for key in ("age", "hobby", "language"):
			ttk.Label(summary, text=key.upper(), style="SummaryLabel.TLabel").pack(anchor="w", pady=(0, 5))
			self.preview[key] = ttk.Label(summary, text="--", style="SummaryValue.TLabel", wraplength=330)
			self.preview[key].pack(anchor="w", pady=(0, 18))

		self.status = ttk.Label(summary, text="Awaiting submitted information.", style="SummaryLabel.TLabel", wraplength=330)
		self.status.pack(anchor="w", side="bottom")

	def clear_placeholder(self, entry, placeholder):
		if entry.get() == placeholder:
			entry.delete(0, tk.END)
			entry.configure(foreground="#182a3a")

	def restore_placeholder(self, entry, placeholder):
		if not entry.get().strip():
			entry.insert(0, placeholder)
			entry.configure(foreground="#8995a1")

	def get_value(self, key):
		entry, placeholder = self.entries[key]
		value = entry.get().strip()
		return "" if value == placeholder else value

	def update_summary(self):
		self.preview["name"].configure(text=self.get_value("name") or "Your name")
		self.preview["city"].configure(text=self.get_value("city") or "Your city")
		for key in ("age", "hobby", "language"):
			self.preview[key].configure(text=self.get_value(key) or "--")

	def submit(self):
		missing = [key.title() for key in self.entries if not self.get_value(key)]
		if missing:
			messagebox.showwarning("Incomplete Form", "Please complete: " + ", ".join(missing))
			return
		self.update_summary()
		self.status.configure(text="Information submitted successfully.")
		self.submit_button.focus_set()
		messagebox.showinfo("Submission Complete", "Your personal introduction has been submitted.")

	def reset(self):
		for entry, placeholder in self.entries.values():
			entry.delete(0, tk.END)
			entry.insert(0, placeholder)
			entry.configure(foreground="#8995a1")
		self.update_summary()
		self.status.configure(text="Awaiting submitted information.")
		self.submit_button.focus_set()


if __name__ == "__main__":
	app_window = tk.Tk()
	PersonalIntroduction(app_window)
	app_window.mainloop()

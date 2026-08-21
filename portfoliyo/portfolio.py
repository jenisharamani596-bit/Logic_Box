import tkinter as tk
from tkinter import messagebox, ttk


class PortfolioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jenish Ramani | Portfolio")
        self.root.geometry("920x650")
        self.root.minsize(760, 560)
        self.root.configure(bg="#edf1f5")
        self.setup_styles()
        self.build_ui()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Page.TFrame", background="#edf1f5")
        style.configure("Card.TFrame", background="#ffffff")
        style.configure("Hero.TFrame", background="#173c5b")
        style.configure("HeroKicker.TLabel", background="#173c5b", foreground="#b9cede", font=("Segoe UI", 10, "bold"))
        style.configure("HeroTitle.TLabel", background="#173c5b", foreground="#ffffff", font=("Georgia", 34))
        style.configure("HeroText.TLabel", background="#173c5b", foreground="#d8e4ec", font=("Segoe UI", 12))
        style.configure("Section.TLabel", background="#ffffff", foreground="#173c5b", font=("Segoe UI", 10, "bold"))
        style.configure("CardTitle.TLabel", background="#ffffff", foreground="#173c5b", font=("Segoe UI", 12, "bold"))
        style.configure("CardText.TLabel", background="#ffffff", foreground="#687782", font=("Segoe UI", 10))
        style.configure("StatValue.TLabel", background="#ffffff", foreground="#173c5b", font=("Georgia", 25))
        style.configure("StatLabel.TLabel", background="#ffffff", foreground="#687782", font=("Segoe UI", 9, "bold"))
        style.configure("Primary.TButton", background="#b38a3c", foreground="#ffffff", padding=(18, 10), font=("Segoe UI", 10, "bold"))
        style.configure("Secondary.TButton", background="#ffffff", foreground="#173c5b", padding=(18, 10), font=("Segoe UI", 10, "bold"))

    def build_ui(self):
        page = ttk.Frame(self.root, style="Page.TFrame", padding=30)
        page.pack(fill="both", expand=True)

        hero = ttk.Frame(page, style="Hero.TFrame", padding=(40, 34, 40, 36))
        hero.pack(fill="x")
        ttk.Label(hero, text="PERSONAL PORTFOLIO  /  01", style="HeroKicker.TLabel").pack(anchor="w")
        ttk.Label(hero, text="Jenish Ramani", style="HeroTitle.TLabel").pack(anchor="w", pady=(12, 5))
        ttk.Label(hero, text="Python Learner & Developer", style="HeroText.TLabel").pack(anchor="w")

        body = ttk.Frame(page, style="Page.TFrame")
        body.pack(fill="both", expand=True, pady=(16, 0))
        body.columnconfigure(0, weight=1)
        body.columnconfigure(1, weight=2)
        body.rowconfigure(0, weight=1)

        overview = ttk.Frame(body, style="Card.TFrame", padding=30)
        overview.grid(row=0, column=0, sticky="nsew", padx=(0, 8))
        ttk.Label(overview, text="PROFILE OVERVIEW", style="Section.TLabel").pack(anchor="w", pady=(0, 25))
        self.add_stat(overview, "5", "PROJECTS COMPLETED")
        self.add_stat(overview, "ACTIVE", "GIT & GITHUB LEARNING")
        ttk.Separator(overview).pack(fill="x", pady=18)
        ttk.Label(overview, text="Building practical Python projects while developing a strong foundation in professional workflows.", style="CardText.TLabel", wraplength=245).pack(anchor="w")
        ttk.Button(overview, text="Explore Portfolio", style="Primary.TButton", command=self.explore).pack(anchor="w", pady=(26, 0))

        roadmap = ttk.Frame(body, style="Card.TFrame", padding=30)
        roadmap.grid(row=0, column=1, sticky="nsew", padx=(8, 0))
        ttk.Label(roadmap, text="LEARNING ROADMAP", style="Section.TLabel").pack(anchor="w", pady=(0, 20))
        concepts = (
            ("01", "Git Installation & Configuration"),
            ("02", "GitHub Account & Repository Creation"),
            ("03", "Push, Pull & Commit Workflow"),
            ("04", "Branch Management"),
            ("05", "README Documentation"),
        )
        for number, title in concepts:
            row = ttk.Frame(roadmap, style="Card.TFrame")
            row.pack(fill="x", pady=(0, 15))
            ttk.Label(row, text=number, style="StatValue.TLabel", width=3).pack(side="left", anchor="n")
            ttk.Label(row, text=title, style="CardTitle.TLabel").pack(side="left", anchor="n", padx=(12, 0), pady=6)

    def add_stat(self, parent, value, label):
        ttk.Label(parent, text=value, style="StatValue.TLabel").pack(anchor="w")
        ttk.Label(parent, text=label, style="StatLabel.TLabel").pack(anchor="w", pady=(0, 21))

    def explore(self):
        messagebox.showinfo("Portfolio", "Welcome to Jenish Ramani's GitHub portfolio.")


if __name__ == "__main__":
    app_window = tk.Tk()
    PortfolioApp(app_window)
    app_window.mainloop()
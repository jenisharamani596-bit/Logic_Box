import tkinter as tk
import random

root = tk.Tk()
root.title("🕵️ Secret Code Challenge")
root.geometry("750x550")
root.configure(bg="#0b1020")
root.resizable(False, False)

# Title
title = tk.Label(
    root,
    text="🕵️ SECRET CODE CHALLENGE",
    font=("Arial", 28, "bold"),
    bg="#0b1020",
    fg="#00ffcc"
)
title.pack(pady=35)

subtitle = tk.Label(
    root,
    text="Can you guess the secret number?",
    font=("Arial", 15),
    bg="#0b1020",
    fg="white"
)
subtitle.pack()

# Secret number
secret = random.randint(1, 100)
attempts = 0

# Input
entry = tk.Entry(
    root,
    font=("Arial", 22, "bold"),
    justify="center",
    bg="#18233d",
    fg="white",
    insertbackground="white",
    relief="flat"
)
entry.pack(pady=30, ipady=10)

# Result
result = tk.Label(
    root,
    text="🔐 Enter a number between 1 and 100",
    font=("Arial", 16, "bold"),
    bg="#0b1020",
    fg="#ffd166"
)
result.pack(pady=10)

# Score
score = tk.Label(
    root,
    text="Attempts: 0",
    font=("Arial", 13),
    bg="#0b1020",
    fg="#94a3b8"
)
score.pack(pady=5)


def check_number():

    global secret, attempts

    try:
        guess = int(entry.get())
        attempts += 1

        score.config(text=f"Attempts: {attempts}")

        if guess < secret:
            result.config(
                text="⬆️ Too Low! Try a bigger number.",
                fg="#ff9f43"
            )

        elif guess > secret:
            result.config(
                text="⬇️ Too High! Try a smaller number.",
                fg="#ff6b6b"
            )

        else:
            result.config(
                text=f"🎉 YOU WON! Secret Number = {secret}",
                fg="#00ff99"
            )

    except ValueError:
        result.config(
            text="⚠️ Please enter a valid number!",
            fg="#ff4444"
        )


def new_game():

    global secret, attempts

    secret = random.randint(1, 100)
    attempts = 0

    entry.delete(0, tk.END)

    score.config(text="Attempts: 0")

    result.config(
        text="🔐 New secret number generated!",
        fg="#ffd166"
    )


# Buttons
button_frame = tk.Frame(root, bg="#0b1020")
button_frame.pack(pady=30)

check_btn = tk.Button(
    button_frame,
    text="🔓 CHECK",
    command=check_number,
    font=("Arial", 15, "bold"),
    bg="#00b894",
    fg="white",
    width=12,
    height=2,
    relief="flat",
    cursor="hand2"
)
check_btn.grid(row=0, column=0, padx=10)

new_btn = tk.Button(
    button_frame,
    text="🔄 NEW GAME",
    command=new_game,
    font=("Arial", 15, "bold"),
    bg="#6c5ce7",
    fg="white",
    width=12,
    height=2,
    relief="flat",
    cursor="hand2"
)
new_btn.grid(row=0, column=1, padx=10)

# Footer
footer = tk.Label(
    root,
    text="💻 Python Mini Project • Guess the Secret",
    font=("Arial", 11),
    bg="#0b1020",
    fg="#64748b"
)
footer.pack(pady=20)

root.mainloop()
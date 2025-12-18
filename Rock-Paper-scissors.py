import tkinter as tk
import random

# dritarja
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x320")
root.configure(bg="#1e1e2f")  # background (si body në CSS)

choices = ["Rock", "Paper", "Scissors"]

# title
title = tk.Label(
    root,
    text="Rock • Paper • Scissors",
    font=("Segoe UI", 14, "bold"),
    bg="#1e1e2f",
    fg="#ffffff"
)
title.pack(pady=10)

result_label = tk.Label(
    root,
    text="Zgjedh nje opsion",
    font=("Segoe UI", 12),
    bg="#1e1e2f",
    fg="#00ffcc"
)
result_label.pack(pady=10)

computer_label = tk.Label(
    root,
    text="",
    font=("Segoe UI", 10),
    bg="#1e1e2f",
    fg="#bbbbbb"
)
computer_label.pack(pady=5)

def play(player_choice):
    computer_choice = random.choice(choices)
    computer_label.config(text=f"Kompjuteri zgjodhi: {computer_choice}")

    if player_choice == computer_choice:
        result = " Barazim"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Scissors" and computer_choice == "Paper") or
        (player_choice == "Paper" and computer_choice == "Rock")
    ):
        result = " Fitove"
    else:
        result = " Humbje"

    result_label.config(text=result)

# stil butonash (si class në CSS)
btn_style = {
    "font": ("Segoe UI", 11, "bold"),
    "width": 15,
    "bg": "#2b2b40",
    "fg": "#ffffff",
    "activebackground": "#00ffcc",
    "activeforeground": "#000000",
    "bd": 0,
    "cursor": "hand2"
}

tk.Button(root, text=" Rock", command=lambda: play("Rock"), **btn_style).pack(pady=6)
tk.Button(root, text=" Paper", command=lambda: play("Paper"), **btn_style).pack(pady=6)
tk.Button(root, text=" Scissors", command=lambda: play("Scissors"), **btn_style).pack(pady=6)

root.mainloop()

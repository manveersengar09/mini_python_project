import tkinter as tk

root = tk.Tk()
root.title("Happy Birthday ####")
root.geometry("600x450")
root.config(bg="#e6f7ff")  # Light blue background

heading = tk.Label(
    root,
    text="🎉 Happy Birthday #### 🫠🫠 🎉",
    font=("Helvetica", 24, "bold"),
    bg="#e6f7ff",
    fg="#ff3366"
)
heading.pack(pady=15)

# Birthday date with cute emoji
birthday_date = tk.Label(
    root,
    text="📅 ##### date",
    font=("Helvetica", 16, "italic"),
    bg="#e6f7ff",
    fg="#ff3366"
)
birthday_date.pack(pady=5)

message = tk.Label(
    root,
    text="Wishing you a day filled with love, joy, and cake!\nMay your year ahead be as sweet as you are.",
    font=("Helvetica", 14),
    bg="#e6f7ff",
    fg="#cc0066"
)
message.pack(pady=15)

# Simple cake emoji without using PIL
cake_label = tk.Label(root, text="🎂", font=("Helvetica", 100), bg="#e6f7ff")
cake_label.pack(pady=15)

footer = tk.Label(root, text="With love, Manveer ❤️", font=("Helvetica", 12), bg="#e6f7ff", fg="#ff3366")
footer.pack(pady=10)

root.mainloop()

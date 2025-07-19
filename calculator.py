import tkinter as tk

def on_click(event):
    current_text = entry.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

def create_button(text, row, col, col_span=1, bg="#e0e0e0", fg="#000"):
    button = tk.Button(
        root, text=text, font=("Segoe UI", 16, "bold"),
        bd=2, width=5, height=2,
        bg=bg, fg=fg, relief="raised", activebackground="#d6d6d6"
    )
    button.grid(row=row, column=col, columnspan=col_span, padx=5, pady=5, sticky="nsew")
    button.bind("<Button-1>", on_click)
    return button

root = tk.Tk()
root.title("🧮 Calculator - CodSoft Task 2")
root.geometry("340x460")
root.configure(bg="#f7f7f7")

# Configure grid weights
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(7):
    root.grid_rowconfigure(i, weight=1)

# Heading
heading_label = tk.Label(root, text="Simple Calculator", font=("Helvetica", 18, "bold"), bg="#f7f7f7", fg="#333")
heading_label.grid(row=0, column=0, columnspan=4, pady=10)

# Entry display
entry = tk.Entry(root, font=("Helvetica", 22), bd=3, justify=tk.RIGHT, relief="sunken", bg="white")
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10, ipady=10)

# Buttons layout
create_button("7", 2, 0)
create_button("8", 2, 1)
create_button("9", 2, 2)
create_button("/", 2, 3, bg="#ffa500", fg="white")

create_button("4", 3, 0)
create_button("5", 3, 1)
create_button("6", 3, 2)
create_button("*", 3, 3, bg="#ffa500", fg="white")

create_button("1", 4, 0)
create_button("2", 4, 1)
create_button("3", 4, 2)
create_button("-", 4, 3, bg="#ffa500", fg="white")

create_button("0", 5, 0)
create_button(".", 5, 1)
create_button("=", 5, 2, bg="#4caf50", fg="white")
create_button("+", 5, 3, bg="#ffa500", fg="white")

create_button("C", 6, 0, 4, bg="#f44336", fg="white")

root.mainloop()

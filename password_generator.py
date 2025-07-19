import tkinter as tk
from tkinter import messagebox
import random
import string

entry_username = None
entry_password_length = None
entry_generated_password = None

def generate_password():
    global entry_generated_password
    try:
        password_length = int(entry_password_length.get())
        if password_length < 8:
            messagebox.showwarning("Warning", "Password length should be at least 8 characters.")
            return
    except ValueError:
        messagebox.showwarning("Warning", "Please enter a valid number.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choice(characters) for _ in range(password_length))
    entry_generated_password.delete(0, tk.END)
    entry_generated_password.insert(tk.END, generated_password)

def accept_password():
    global entry_username, entry_generated_password
    username = entry_username.get()
    password = entry_generated_password.get()
    if not username or not password:
        messagebox.showwarning("Warning", "Please enter username and generate a password.")
        return
    messagebox.showinfo("✅ Accepted", f"Username: {username}\nPassword: {password}")

def reset_fields():
    global entry_username, entry_password_length, entry_generated_password
    entry_username.delete(0, tk.END)
    entry_password_length.delete(0, tk.END)
    entry_generated_password.delete(0, tk.END)

def main():
    global entry_username, entry_password_length, entry_generated_password

    root = tk.Tk()
    root.title("🔐 Password Generator - CodSoft Task 3")
    root.geometry("450x300")
    root.configure(bg="#f0f4f8")

    heading_label = tk.Label(root, text="🔑 Password Generator", font=("Helvetica", 16, "bold"), bg="#f0f4f8", fg="#333")
    heading_label.grid(row=0, column=0, columnspan=3, pady=20)

    label_username = tk.Label(root, text="👤 Username:", font=("Segoe UI", 10), bg="#f0f4f8")
    label_username.grid(row=1, column=0, sticky=tk.E, padx=10, pady=5)

    entry_username = tk.Entry(root, width=30, font=("Segoe UI", 10))
    entry_username.grid(row=1, column=1, columnspan=2, pady=5)

    label_password_length = tk.Label(root, text="🔢 Password Length:", font=("Segoe UI", 10), bg="#f0f4f8")
    label_password_length.grid(row=2, column=0, sticky=tk.E, padx=10, pady=5)

    entry_password_length = tk.Entry(root, width=10, font=("Segoe UI", 10))
    entry_password_length.grid(row=2, column=1, pady=5)

    label_generated_password = tk.Label(root, text="🔐 Generated Password:", font=("Segoe UI", 10), bg="#f0f4f8")
    label_generated_password.grid(row=3, column=0, sticky=tk.E, padx=10, pady=5)

    entry_generated_password = tk.Entry(root, width=30, font=("Segoe UI", 10))
    entry_generated_password.grid(row=3, column=1, columnspan=2, pady=5)

    # Buttons
    button_generate_password = tk.Button(
        root, text="⚙️ Generate", command=generate_password,
        bg="#4caf50", fg="white", font=("Segoe UI", 10, "bold"), width=12
    )
    button_generate_password.grid(row=4, column=0, padx=10, pady=20)

    button_accept_password = tk.Button(
        root, text="✅ Accept", command=accept_password,
        bg="#2196f3", fg="white", font=("Segoe UI", 10, "bold"), width=12
    )
    button_accept_password.grid(row=4, column=1, padx=10, pady=20)

    button_reset_fields = tk.Button(
        root, text="🔄 Reset", command=reset_fields,
        bg="#f44336", fg="white", font=("Segoe UI", 10, "bold"), width=12
    )
    button_reset_fields.grid(row=4, column=2, padx=10, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()

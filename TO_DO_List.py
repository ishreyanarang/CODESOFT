import tkinter as tk
from tkinter import simpledialog, messagebox

def add_task():
    global listbox_tasks, entry_task
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    global listbox_tasks
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def edit_task():
    global listbox_tasks
    try:
        index = listbox_tasks.curselection()[0]
        old_task = listbox_tasks.get(index)
        new_task = simpledialog.askstring("Edit Task", "Edit the selected task:", initialvalue=old_task)
        if new_task:
            listbox_tasks.delete(index)
            listbox_tasks.insert(index, new_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to edit.")

def main():
    global listbox_tasks, entry_task
    root = tk.Tk()
    root.title("✨ To-Do List - CodSoft Task 1")
    root.geometry("500x400")
    root.configure(bg="#f9f9f9")

    # Title
    title_label = tk.Label(root, text="📝 Your Daily Tasks", font=("Helvetica", 16, "bold"), bg="#f9f9f9", fg="#333")
    title_label.pack(pady=10)

    # Task list frame
    frame_tasks = tk.Frame(root, bg="#f9f9f9")
    frame_tasks.pack(pady=10)

    listbox_tasks = tk.Listbox(
        frame_tasks,
        width=50,
        height=10,
        selectbackground="#a3d2ca",
        selectforeground="#000000",
        font=("Segoe UI", 11),
        relief=tk.FLAT,
        bd=2,
        highlightthickness=1
    )
    listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

    scrollbar_tasks = tk.Scrollbar(frame_tasks)
    scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.BOTH)

    listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
    scrollbar_tasks.config(command=listbox_tasks.yview)

    # Entry field
    entry_task = tk.Entry(root, width=50, font=("Segoe UI", 11), relief=tk.GROOVE, bd=2)
    entry_task.pack(pady=10)

    # Buttons Frame
    button_frame = tk.Frame(root, bg="#f9f9f9")
    button_frame.pack(pady=5)

    button_add_task = tk.Button(
        button_frame,
        text="➕ Add Task",
        command=add_task,
        bg="#4caf50",
        fg="white",
        font=("Segoe UI", 10, "bold"),
        width=12
    )
    button_add_task.pack(side=tk.LEFT, padx=5)

    button_delete_task = tk.Button(
        button_frame,
        text="❌ Delete Task",
        command=delete_task,
        bg="#f44336",
        fg="white",
        font=("Segoe UI", 10, "bold"),
        width=12
    )
    button_delete_task.pack(side=tk.LEFT, padx=5)

    button_edit_task = tk.Button(
        button_frame,
        text="✏️ Edit Task",
        command=edit_task,
        bg="#2196f3",
        fg="white",
        font=("Segoe UI", 10, "bold"),
        width=12
    )
    button_edit_task.pack(side=tk.LEFT, padx=5)

    root.mainloop()

if __name__ == "__main__":
    main()

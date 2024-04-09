import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)


def mark_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.itemconfig(selected_task, bg="dark cyan")

root = tk.Tk()
root.title("Task list")
root.configure(background="brown")


text1 = tk.Label(root, text="Введите Вашу задачу:", bg="coral3")
text1.pack()
task_entry = tk.Entry(root, width=40, bg="dark salmon")
task_entry.pack()

add_task_button = tk.Button(root, text="Добавить задачу", command=add_task)
add_task_button.pack(pady=5)

delete_button = tk.Button(root, text="Удалить задачу", command=delete_task)
delete_button.pack(pady=5)

mark_button = tk.Button(root, text="Отметить выполненную задачу", command=mark_task)
mark_button.pack(pady=5)


text2 = tk.Label(root, text="Список задач:", bg="coral3")
text2.pack()

task_listbox = tk.Listbox(root, height=10, width=50, bg="dark orange")
task_listbox.pack()

root.mainloop()
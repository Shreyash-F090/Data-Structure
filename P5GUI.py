import tkinter as tk
from tkinter import messagebox

class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def empty(self):
        return len(self.queue) == 0

    def isfull(self):
        return len(self.queue) == self.max_size

    def enqueue(self, item):
        if self.isfull():
            return "Queue is Full!"
        self.queue.append(item)
        return f"{item} inserted successfully."

    def dequeue(self):
        if self.empty():
            return "Queue is Empty!"
        item = self.queue.pop(0)
        return f"{item} removed successfully."

    def peek(self):
        if self.empty():
            return "Queue is Empty!"
        return f"Front Element: {self.queue[0]}"

    def traverse(self):
        if self.empty():
            return "Queue is Empty!"
        return " -> ".join(str(x) for x in self.queue)

    def display_list(self):
        if self.empty():
            return "Queue is Empty!"
        
        result = "Current Queue List:\n\n"
        for i, item in enumerate(self.queue, start=1):
            result += f"{i}. {item}\n"
        return result


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Queue Operations - Shreyash Kadam S091")
root.geometry("650x500")
root.resizable(False, False)

queue_obj = None

# Title
title = tk.Label(
    root,
    text="QUEUE OPERATIONS",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

# Queue Size Frame
size_frame = tk.Frame(root)
size_frame.pack(pady=5)

tk.Label(
    size_frame,
    text="Maximum Queue Size:"
).pack(side=tk.LEFT)

size_entry = tk.Entry(size_frame, width=10)
size_entry.pack(side=tk.LEFT, padx=5)

# Item Frame
item_frame = tk.Frame(root)
item_frame.pack(pady=5)

tk.Label(
    item_frame,
    text="Item:"
).pack(side=tk.LEFT)

item_entry = tk.Entry(item_frame, width=20)
item_entry.pack(side=tk.LEFT, padx=5)

# Output Box
output_box = tk.Text(root, height=12, width=70)
output_box.pack(pady=10)

def show_output(text):
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, text)

def create_queue():
    global queue_obj

    size = size_entry.get()

    if size == "":
        messagebox.showerror(
            "Error",
            "Enter Queue Size!"
        )
        return

    try:
        size = int(size)

        if size <= 0:
            messagebox.showerror(
                "Error",
                "Size must be greater than 0"
            )
            return

        queue_obj = Queue(size)

        show_output(
            f"Queue Created Successfully!\nMaximum Size = {size}"
        )

    except:
        messagebox.showerror(
            "Error",
            "Enter a valid integer."
        )

def enqueue_item():
    if queue_obj is None:
        messagebox.showerror(
            "Error",
            "Create Queue First!"
        )
        return

    item = item_entry.get()

    if item == "":
        messagebox.showerror(
            "Error",
            "Enter an item."
        )
        return

    result = queue_obj.enqueue(item)
    show_output(result)
    item_entry.delete(0, tk.END)

def dequeue_item():
    if queue_obj is None:
        messagebox.showerror(
            "Error",
            "Create Queue First!"
        )
        return

    show_output(queue_obj.dequeue())

def peek_item():
    if queue_obj is None:
        messagebox.showerror(
            "Error",
            "Create Queue First!"
        )
        return

    show_output(queue_obj.peek())

def traverse_queue():
    if queue_obj is None:
        messagebox.showerror(
            "Error",
            "Create Queue First!"
        )
        return

    show_output(queue_obj.traverse())

def display_queue():
    if queue_obj is None:
        messagebox.showerror(
            "Error",
            "Create Queue First!"
        )
        return

    show_output(queue_obj.display_list())

def check_empty():
    if queue_obj is None:
        messagebox.showerror(
            "Error",
            "Create Queue First!"
        )
        return

    if queue_obj.empty():
        show_output("Queue is Empty")
    else:
        show_output("Queue is Not Empty")

def check_full():
    if queue_obj is None:
        messagebox.showerror(
            "Error",
            "Create Queue First!"
        )
        return

    if queue_obj.isfull():
        show_output("Queue is Full")
    else:
        show_output("Queue is Not Full")

# Buttons Frame
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(
    btn_frame,
    text="Create Queue",
    width=15,
    command=create_queue
).grid(row=0, column=0, padx=5, pady=5)

tk.Button(
    btn_frame,
    text="Enqueue",
    width=15,
    command=enqueue_item
).grid(row=0, column=1, padx=5, pady=5)

tk.Button(
    btn_frame,
    text="Dequeue",
    width=15,
    command=dequeue_item
).grid(row=1, column=0, padx=5, pady=5)

tk.Button(
    btn_frame,
    text="Peek",
    width=15,
    command=peek_item
).grid(row=1, column=1, padx=5, pady=5)

tk.Button(
    btn_frame,
    text="Traverse",
    width=15,
    command=traverse_queue
).grid(row=2, column=0, padx=5, pady=5)

tk.Button(
    btn_frame,
    text="Display List",
    width=15,
    command=display_queue
).grid(row=2, column=1, padx=5, pady=5)

tk.Button(
    btn_frame,
    text="Check Empty",
    width=15,
    command=check_empty
).grid(row=3, column=0, padx=5, pady=5)

tk.Button(
    btn_frame,
    text="Check Full",
    width=15,
    command=check_full
).grid(row=3, column=1, padx=5, pady=5)

tk.Button(
    root,
    text="Exit",
    width=20,
    bg="red",
    fg="white",
    command=root.destroy
).pack(pady=10)

root.mainloop()

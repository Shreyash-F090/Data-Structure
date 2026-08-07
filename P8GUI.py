import tkinter as tk
from tkinter import messagebox
import heapq


class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None


class AVLTree:
    def get_height(self, root):
        return root.height if root else 0

    def get_balance(self, root):
        if root:
            return self.get_height(root.left) - self.get_height(root.right)
        return 0

    def left_rotate(self, z, output):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(
            self.get_height(z.left),
            self.get_height(z.right)
        )

        y.height = 1 + max(
            self.get_height(y.left),
            self.get_height(y.right)
        )

        output.insert(tk.END, f"Left Rotation on {z.key}\n")
        return y

    def right_rotate(self, z, output):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(
            self.get_height(z.left),
            self.get_height(z.right)
        )

        y.height = 1 + max(
            self.get_height(y.left),
            self.get_height(y.right)
        )

        output.insert(tk.END, f"Right Rotation on {z.key}\n")
        return y

    def insert(self, root, key, output):
        if not root:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key, output)
        else:
            root.right = self.insert(root.right, key, output)

        root.height = 1 + max(
            self.get_height(root.left),
            self.get_height(root.right)
        )

        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.right_rotate(root, output)

        if balance < -1 and key > root.right.key:
            return self.left_rotate(root, output)

        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left, output)
            return self.right_rotate(root, output)

        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right, output)
            return self.left_rotate(root, output)

        return root

    def pre_order(self, root, result):
        if root:
            result.append(str(root.key))
            self.pre_order(root.left, result)
            self.pre_order(root.right, result)


class TaskManager:
    def __init__(self):
        self.pq = []

    def add_task(self, priority, description):
        heapq.heappush(self.pq, (priority, description))

    def run_tasks(self):
        result = []

        while self.pq:
            priority, task = heapq.heappop(self.pq)
            result.append(f"Priority {priority} > Task: {task}")

        return result


avl = AVLTree()
root = None
manager = TaskManager()


def show_avl():
    global root

    values = entry_values.get().strip()

    if not values:
        messagebox.showwarning(
            "Input Required",
            "Enter AVL values."
        )
        return

    try:
        numbers = [int(x.strip()) for x in values.split(",")]
    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Enter numbers separated by commas."
        )
        return

    root = None

    output.delete(
        "1.0",
        tk.END
    )

    output.insert(
        tk.END,
        "=== AVL Tree Insertion and Balancing ===\n"
    )

    output.insert(
        tk.END,
        "-" * 55 + "\n"
    )

    for value in numbers:
        output.insert(
            tk.END,
            f"Inserting {value}...\n"
        )

        root = avl.insert(
            root,
            value,
            output
        )

    result = []

    avl.pre_order(
        root,
        result
    )

    output.insert(
        tk.END,
        "\nAVL Tree Pre-Order Traversal:\n"
    )

    output.insert(
        tk.END,
        " ".join(result) + "\n"
    )


def show_heaps():
    values = entry_heap.get().strip()

    if not values:
        messagebox.showwarning(
            "Input Required",
            "Enter heap values."
        )
        return

    try:
        numbers = [
            int(x.strip())
            for x in values.split(",")
        ]
    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Enter numbers separated by commas."
        )
        return

    min_heap = numbers.copy()

    heapq.heapify(
        min_heap
    )

    max_heap = [
        -x for x in numbers
    ]

    heapq.heapify(
        max_heap
    )

    max_result = [
        -x for x in max_heap
    ]

    output.delete(
        "1.0",
        tk.END
    )

    output.insert(
        tk.END,
        "=== Heap Examples ===\n"
    )

    output.insert(
        tk.END,
        "-" * 55 + "\n"
    )

    output.insert(
        tk.END,
        f"Original Data: {numbers}\n\n"
    )

    output.insert(
        tk.END,
        f"Min-Heap: {min_heap}\n"
    )

    output.insert(
        tk.END,
        f"Max-Heap: {max_result}\n"
    )


def add_task():
    priority = entry_priority.get().strip()
    description = entry_task.get().strip()

    if not priority or not description:
        messagebox.showwarning(
            "Input Required",
            "Enter both priority and task description."
        )
        return

    try:
        priority = int(priority)
    except ValueError:
        messagebox.showerror(
            "Invalid Priority",
            "Priority must be an integer."
        )
        return

    manager.add_task(
        priority,
        description
    )

    output.insert(
        tk.END,
        f"Added Task: Priority {priority} > {description}\n"
    )

    entry_priority.delete(
        0,
        tk.END
    )

    entry_task.delete(
        0,
        tk.END
    )


def run_tasks():
    if not manager.pq:
        messagebox.showwarning(
            "Task Manager",
            "No tasks available."
        )
        return

    output.delete(
        "1.0",
        tk.END
    )

    output.insert(
        tk.END,
        "=== Task Manager using Priority Queue ===\n"
    )

    output.insert(
        tk.END,
        "-" * 55 + "\n"
    )

    output.insert(
        tk.END,
        "Processing Tasks by Priority:\n\n"
    )

    tasks = manager.run_tasks()

    for task in tasks:
        output.insert(
            tk.END,
            task + "\n"
        )


def clear_all():
    global root

    root = None

    entry_values.delete(
        0,
        tk.END
    )

    entry_heap.delete(
        0,
        tk.END
    )

    entry_priority.delete(
        0,
        tk.END
    )

    entry_task.delete(
        0,
        tk.END
    )

    output.delete(
        "1.0",
        tk.END
    )


def exit_program():
    window.destroy()


window = tk.Tk()

window.title(
    "P8GUI - AVL Tree, Heap and Priority Queue - Shreyash Kadam S091"
)

window.geometry(
    "950x750"
)

window.minsize(
    850,
    650
)

title = tk.Label(
    window,
    text="AVL TREE, HEAP & PRIORITY QUEUE",
    font=("Arial", 20, "bold")
)

title.pack(
    pady=10
)

student = tk.Label(
    window,
    text="Shreyash Kadam S091",
    font=("Arial", 12)
)

student.pack()


main_frame = tk.Frame(
    window
)

main_frame.pack(
    fill=tk.BOTH,
    expand=True,
    padx=15,
    pady=10
)


avl_frame = tk.LabelFrame(
    main_frame,
    text="AVL Tree",
    font=("Arial", 11, "bold")
)

avl_frame.pack(
    fill=tk.X,
    pady=5
)


tk.Label(
    avl_frame,
    text="Enter values (comma separated):"
).grid(
    row=0,
    column=0,
    padx=5,
    pady=10
)


entry_values = tk.Entry(
    avl_frame,
    width=45
)

entry_values.grid(
    row=0,
    column=1,
    padx=5
)

entry_values.insert(
    0,
    "20, 4, 15, 70, 50, 100, 80"
)


tk.Button(
    avl_frame,
    text="Run AVL",
    width=15,
    command=show_avl
).grid(
    row=0,
    column=2,
    padx=5
)


heap_frame = tk.LabelFrame(
    main_frame,
    text="Heap Examples",
    font=("Arial", 11, "bold")
)

heap_frame.pack(
    fill=tk.X,
    pady=5
)


tk.Label(
    heap_frame,
    text="Enter values (comma separated):"
).grid(
    row=0,
    column=0,
    padx=5,
    pady=10
)


entry_heap = tk.Entry(
    heap_frame,
    width=45
)

entry_heap.grid(
    row=0,
    column=1,
    padx=5
)

entry_heap.insert(
    0,
    "9, 5, 6, 2, 3"
)


tk.Button(
    heap_frame,
    text="Show Heaps",
    width=15,
    command=show_heaps
).grid(
    row=0,
    column=2,
    padx=5
)


task_frame = tk.LabelFrame(
    main_frame,
    text="Task Manager using Priority Queue",
    font=("Arial", 11, "bold")
)

task_frame.pack(
    fill=tk.X,
    pady=5
)


tk.Label(
    task_frame,
    text="Priority:"
).grid(
    row=0,
    column=0,
    padx=5,
    pady=8
)


entry_priority = tk.Entry(
    task_frame,
    width=10
)

entry_priority.grid(
    row=0,
    column=1,
    padx=5
)


tk.Label(
    task_frame,
    text="Task Description:"
).grid(
    row=0,
    column=2,
    padx=5
)


entry_task = tk.Entry(
    task_frame,
    width=40
)

entry_task.grid(
    row=0,
    column=3,
    padx=5
)


tk.Button(
    task_frame,
    text="Add Task",
    width=12,
    command=add_task
).grid(
    row=0,
    column=4,
    padx=5
)


tk.Button(
    task_frame,
    text="Run Tasks",
    width=12,
    command=run_tasks
).grid(
    row=1,
    column=3,
    pady=8
)


button_frame = tk.Frame(
    main_frame
)

button_frame.pack(
    pady=8
)


tk.Button(
    button_frame,
    text="Clear",
    width=15,
    command=clear_all
).grid(
    row=0,
    column=0,
    padx=5
)


tk.Button(
    button_frame,
    text="Exit",
    width=15,
    command=exit_program
).grid(
    row=0,
    column=1,
    padx=5
)


output_label = tk.Label(
    main_frame,
    text="Output:",
    font=("Arial", 12, "bold")
)

output_label.pack(
    anchor="w"
)


output_frame = tk.Frame(
    main_frame
)

output_frame.pack(
    fill=tk.BOTH,
    expand=True,
    pady=5
)


scrollbar = tk.Scrollbar(
    output_frame
)

scrollbar.pack(
    side=tk.RIGHT,
    fill=tk.Y
)


output = tk.Text(
    output_frame,
    font=("Courier New", 11),
    yscrollcommand=scrollbar.set
)

output.pack(
    side=tk.LEFT,
    fill=tk.BOTH,
    expand=True
)


scrollbar.config(
    command=output.yview
)


window.mainloop()

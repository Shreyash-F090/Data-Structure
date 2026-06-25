import tkinter as tk
from tkinter import messagebox


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is Empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is Empty")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        if self.items:
            return "\n".join(reversed(self.items))
        return "Stack is Empty"


class StackGUI:
    def __init__(self, root):
        self.stack = Stack()
        self.root = root

        self.root.title("S090 Shreyash")
        self.root.state("zoomed")
        self.root.configure(bg="#DCEEFF")

        title = tk.Label(
            root,
            text="STACK OPERATIONS",
            font=("Arial", 24, "bold"),
            bg="#DCEEFF"
        )
        title.pack(pady=20)

        self.entry = tk.Entry(
            root,
            font=("Arial", 14),
            width=30
        )
        self.entry.pack(pady=10)

        btn_frame = tk.Frame(root, bg="#DCEEFF")
        btn_frame.pack(pady=10)

        tk.Button(
            btn_frame,
            text="Push",
            width=12,
            height=2,
            command=self.push_item
        ).grid(row=0, column=0, padx=5, pady=5)

        tk.Button(
            btn_frame,
            text="Pop",
            width=12,
            height=2,
            command=self.pop_item
        ).grid(row=0, column=1, padx=5, pady=5)

        tk.Button(
            btn_frame,
            text="Peek",
            width=12,
            height=2,
            command=self.peek_item
        ).grid(row=1, column=0, padx=5, pady=5)

        tk.Button(
            btn_frame,
            text="Size",
            width=12,
            height=2,
            command=self.size_item
        ).grid(row=1, column=1, padx=5, pady=5)

        tk.Button(
            btn_frame,
            text="Is Empty?",
            width=12,
            height=2,
            command=self.empty_item
        ).grid(row=2, column=0, padx=5, pady=5)

        tk.Button(
            btn_frame,
            text="Clear Stack",
            width=12,
            height=2,
            command=self.clear_stack
        ).grid(row=2, column=1, padx=5, pady=5)

        tk.Button(
            btn_frame,
            text="Exit",
            width=26,
            height=2,
            command=self.root.destroy
        ).grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        content_frame = tk.Frame(root, bg="#DCEEFF")
        content_frame.pack(pady=20)

        info_frame = tk.LabelFrame(
            content_frame,
            text="Stack Information",
            font=("Arial", 12, "bold"),
            padx=20,
            pady=20
        )
        info_frame.grid(row=0, column=0, padx=20)

        self.info_label = tk.Label(
            info_frame,
            text="Size : 0\nTop : None\nEmpty : True",
            font=("Arial", 12),
            justify="left"
        )
        self.info_label.pack()

        display_frame = tk.LabelFrame(
            content_frame,
            text="Stack Visualization",
            font=("Arial", 12, "bold"),
            padx=10,
            pady=10
        )
        display_frame.grid(row=0, column=1, padx=20)

        self.stack_display = tk.Text(
            display_frame,
            width=35,
            height=20,
            font=("Consolas", 14)
        )
        self.stack_display.pack()

        self.root.bind("<Return>", lambda event: self.push_item())

        self.update_display()

    def update_info(self):

        size = len(self.stack.items)

        if self.stack.is_empty():
            top = "None"
            empty = "True"
        else:
            top = self.stack.peek()
            empty = "False"

        self.info_label.config(
            text=f"Size : {size}\nTop : {top}\nEmpty : {empty}"
        )

    def update_display(self):

        self.stack_display.delete(1.0, tk.END)

        if self.stack.is_empty():

            self.stack_display.insert(
                tk.END,
                "\n\n      Stack is Empty"
            )

        else:

            self.stack_display.insert(
                tk.END,
                "TOP\n\n"
            )

            for item in reversed(self.stack.items):

                self.stack_display.insert(
                    tk.END,
                    f"┌─────────┐\n"
                    f"│ {str(item):^7} │\n"
                    f"└─────────┘\n"
                )

        self.update_info()

    def push_item(self):

        item = self.entry.get()

        if item == "":
            messagebox.showwarning(
                "Warning",
                "Please enter a value"
            )
            return

        self.stack.push(item)
        self.entry.delete(0, tk.END)
        self.update_display()

    def pop_item(self):

        try:
            item = self.stack.pop()

            messagebox.showinfo(
                "Popped",
                f"Removed: {item}"
            )

            self.update_display()

        except IndexError as e:
            messagebox.showerror(
                "Error",
                str(e)
            )

    def peek_item(self):

        try:
            item = self.stack.peek()

            messagebox.showinfo(
                "Top Element",
                f"Top = {item}"
            )

        except IndexError as e:
            messagebox.showerror(
                "Error",
                str(e)
            )

    def size_item(self):

        messagebox.showinfo(
            "Size",
            f"Stack Size = {self.stack.size()}"
        )

    def empty_item(self):

        messagebox.showinfo(
            "Empty Check",
            "Yes" if self.stack.is_empty() else "No"
        )

    def clear_stack(self):

        self.stack.items.clear()
        self.update_display()


root = tk.Tk()
app = StackGUI(root)
root.mainloop()

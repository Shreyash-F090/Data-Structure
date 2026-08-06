import tkinter as tk
from tkinter import messagebox


class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def insert(self, item, position):

        if position < 0 or position > len(self.items):
            raise IndexError("Invalid Position")

        self.items.insert(position, item)

    def delete(self, position):

        if position < 0 or position >= len(self.items):
            raise IndexError("Invalid Position")

        return self.items.pop(position)

    def peek(self):

        if self.is_empty():
            raise IndexError("Stack is Empty")

        return self.items[-1]

    def size(self):
        return len(self.items)

    def traverse(self):

        if self.is_empty():
            raise IndexError("Stack is Empty")

        return " <- ".join(self.items)

    def __str__(self):

        if self.items:
            return "\n".join(reversed(self.items))

        return "Stack is Empty"


class StackGUI:

    def __init__(self, root):

        self.stack = Stack()

        self.root = root

        self.root.title("S091 Shreyash")

        self.root.state("zoomed")

        self.root.configure(bg="#DCEEFF")

        title = tk.Label(
            root,
            text="STACK OPERATIONS",
            font=("Arial",24,"bold"),
            bg="#DCEEFF"
        )

        title.pack(pady=20)

        input_frame = tk.Frame(root,bg="#DCEEFF")
        input_frame.pack()

        tk.Label(
            input_frame,
            text="Item",
            font=("Arial",12,"bold"),
            bg="#DCEEFF"
        ).grid(row=0,column=0,padx=10,pady=10)

        self.item_entry = tk.Entry(
            input_frame,
            width=20,
            font=("Arial",12)
        )

        self.item_entry.grid(row=0,column=1,padx=10)

        tk.Label(
            input_frame,
            text="Position",
            font=("Arial",12,"bold"),
            bg="#DCEEFF"
        ).grid(row=0,column=2,padx=10)

        self.position_entry = tk.Entry(
            input_frame,
            width=10,
            font=("Arial",12)
        )

        self.position_entry.grid(row=0,column=3,padx=10)

        btn_frame = tk.Frame(root,bg="#DCEEFF")
        btn_frame.pack(pady=20)

        tk.Button(
            btn_frame,
            text="Insert",
            width=15,
            height=2,
            command=self.insert_item
        ).grid(row=0,column=0,padx=5,pady=5)

        tk.Button(
            btn_frame,
            text="Delete",
            width=15,
            height=2,
            command=self.delete_item
        ).grid(row=0,column=1,padx=5,pady=5)

        tk.Button(
            btn_frame,
            text="Peek",
            width=15,
            height=2,
            command=self.peek_item
        ).grid(row=1,column=0,padx=5,pady=5)

        tk.Button(
            btn_frame,
            text="Traverse",
            width=15,
            height=2,
            command=self.traverse_stack
        ).grid(row=1,column=1,padx=5,pady=5)

        tk.Button(
            btn_frame,
            text="Size",
            width=15,
            height=2,
            command=self.size_stack
        ).grid(row=2,column=0,padx=5,pady=5)

        tk.Button(
            btn_frame,
            text="Is Empty?",
            width=15,
            height=2,
            command=self.empty_stack
        ).grid(row=2,column=1,padx=5,pady=5)

        tk.Button(
            btn_frame,
            text="Exit",
            width=32,
            height=2,
            command=root.destroy
        ).grid(row=3,column=0,columnspan=2,pady=5)

        content_frame = tk.Frame(root,bg="#DCEEFF")
        content_frame.pack(pady=20)

        info_frame = tk.LabelFrame(
            content_frame,
            text="Stack Information",
            font=("Arial",12,"bold"),
            padx=20,
            pady=20
        )

        info_frame.grid(row=0,column=0,padx=20)

        self.info_label = tk.Label(
            info_frame,
            text="Size : 0\nTop : None\nEmpty : True",
            font=("Arial",12),
            justify="left"
        )

        self.info_label.pack()

        display_frame = tk.LabelFrame(
            content_frame,
            text="Stack Visualization",
            font=("Arial",12,"bold"),
            padx=10,
            pady=10
        )

        display_frame.grid(row=0,column=1,padx=20)

        self.stack_display = tk.Text(
            display_frame,
            width=35,
            height=20,
            font=("Consolas",14)
        )

        self.stack_display.pack()

        self.update_display()


    def update_info(self):

        size = self.stack.size()

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

        self.stack_display.delete(1.0,tk.END)

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
                    f"┌─────────────┐\n"
                    f"│ {str(item):^11} │\n"
                    f"└─────────────┘\n"
                )

        self.update_info()
        
    def insert_item(self):

        item = self.item_entry.get()

        if item == "":
            messagebox.showwarning(
                "Warning",
                "Please Enter an Item"
            )
            return

        try:

            position = int(self.position_entry.get())

            self.stack.insert(item, position)

            self.item_entry.delete(0, tk.END)
            self.position_entry.delete(0, tk.END)

            self.update_display()

            messagebox.showinfo(
                "Success",
                f"'{item}' inserted successfully."
            )

        except ValueError:
            messagebox.showerror(
                "Error",
                "Position must be an integer."
            )

        except IndexError as e:
            messagebox.showerror(
                "Error",
                str(e)
            )


    def delete_item(self):

        try:

            position = int(self.position_entry.get())

            item = self.stack.delete(position)

            self.position_entry.delete(0, tk.END)

            self.update_display()

            messagebox.showinfo(
                "Deleted",
                f"Removed : {item}"
            )

        except ValueError:
            messagebox.showerror(
                "Error",
                "Position must be an integer."
            )

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


    def size_stack(self):

        messagebox.showinfo(
            "Stack Size",
            f"Size = {self.stack.size()}"
        )


    def empty_stack(self):

        if self.stack.is_empty():

            messagebox.showinfo(
                "Empty Check",
                "Yes, Stack is Empty"
            )

        else:

            messagebox.showinfo(
                "Empty Check",
                "No, Stack is Not Empty"
            )


    def traverse_stack(self):

        try:

            messagebox.showinfo(
                "Traversal",
                self.stack.traverse()
            )

        except IndexError as e:

            messagebox.showerror(
                "Error",
                str(e)
            )


root = tk.Tk()

app = StackGUI(root)

root.mainloop()

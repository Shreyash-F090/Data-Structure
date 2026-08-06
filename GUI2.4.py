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

    def size(self):
        return len(self.items)


class PrefixGUI:

    def __init__(self, root):

        self.root = root

        self.root.title("S091 Shreyash")

        self.root.state("zoomed")

        self.root.configure(bg="#DCEEFF")

        self.stack = Stack()

        title = tk.Label(
            root,
            text="PREFIX TO POSTFIX CONVERSION",
            font=("Arial",24,"bold"),
            bg="#DCEEFF"
        )

        title.pack(pady=20)

        tk.Label(
            root,
            text="Enter Prefix Expression",
            font=("Arial",14,"bold"),
            bg="#DCEEFF"
        ).pack()

        self.entry = tk.Entry(
            root,
            width=40,
            font=("Arial",14)
        )

        self.entry.pack(pady=10)

        tk.Button(
            root,
            text="Convert",
            width=20,
            height=2,
            command=self.convert_expression
        ).pack(pady=10)

        info_frame = tk.LabelFrame(
            root,
            text="Postfix Expression",
            font=("Arial",12,"bold"),
            padx=20,
            pady=20
        )

        info_frame.pack(pady=20)

        self.result_label = tk.Label(
            info_frame,
            text="",
            font=("Arial",16,"bold")
        )

        self.result_label.pack()

        display_frame = tk.LabelFrame(
            root,
            text="Stack Visualization",
            font=("Arial",12,"bold"),
            padx=10,
            pady=10
        )

        display_frame.pack(pady=20)

        self.display = tk.Text(
            display_frame,
            width=35,
            height=18,
            font=("Consolas",14)
        )

        self.display.pack()

        tk.Button(
            root,
            text="Exit",
            width=20,
            height=2,
            command=root.destroy
        ).pack(pady=10)

        self.update_display()


    def update_display(self):

        self.display.delete(1.0, tk.END)

        if self.stack.is_empty():

            self.display.insert(
                tk.END,
                "\n\n      Stack is Empty"
            )

        else:

            self.display.insert(
                tk.END,
                "TOP\n\n"
            )

            for item in reversed(self.stack.items):

                self.display.insert(
                    tk.END,
                    f"┌─────────────┐\n"
                    f"│ {item:^11} │\n"
                    f"└─────────────┘\n"
                )
    def is_operator(self, ch):

        return ch in "+-*/^"


    def convert_expression(self):

        prefix = self.entry.get()

        if prefix == "":

            messagebox.showwarning(
                "Warning",
                "Please Enter a Prefix Expression"
            )
            return

        self.stack = Stack()

        try:

            expression = prefix[::-1]

            for ch in expression:

                if ch.isalnum():

                    self.stack.push(ch)
                    self.update_display()

                elif self.is_operator(ch):

                    op1 = self.stack.pop()
                    self.update_display()

                    op2 = self.stack.pop()
                    self.update_display()

                    new_expression = op1 + op2 + ch

                    self.stack.push(new_expression)
                    self.update_display()

            result = self.stack.pop()
            self.update_display()

            self.result_label.config(
                text=result
            )

            messagebox.showinfo(
                "Success",
                "Conversion Completed"
            )

            self.entry.delete(0, tk.END)

        except IndexError:

            messagebox.showerror(
                "Error",
                "Invalid Prefix Expression"
            )


root = tk.Tk()

app = PrefixGUI(root)

root.mainloop()

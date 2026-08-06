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

    def __str__(self):
        if self.items:
            return "\n".join(reversed(self.items))
        return "Stack is Empty"


class DelimiterGUI:

    def __init__(self, root):

        self.root = root

        self.root.title("S091 Shreyash")

        self.root.state("zoomed")

        self.root.configure(bg="#DCEEFF")

        self.stack = Stack()

        title = tk.Label(
            root,
            text="DELIMITER MATCHING",
            font=("Arial",24,"bold"),
            bg="#DCEEFF"
        )

        title.pack(pady=20)

        tk.Label(
            root,
            text="Enter Expression",
            font=("Arial",14,"bold"),
            bg="#DCEEFF"
        ).pack()

        self.entry = tk.Entry(
            root,
            width=50,
            font=("Arial",14)
        )

        self.entry.pack(pady=10)

        tk.Button(
            root,
            text="Check Delimiters",
            width=20,
            height=2,
            command=self.check_delimiter
        ).pack(pady=10)

        content = tk.Frame(root,bg="#DCEEFF")
        content.pack(pady=20)

        info_frame = tk.LabelFrame(
            content,
            text="Information",
            font=("Arial",12,"bold"),
            padx=20,
            pady=20
        )

        info_frame.grid(row=0,column=0,padx=20)

        self.info_label = tk.Label(
            info_frame,
            text="Stack Size : 0",
            font=("Arial",12),
            justify="left"
        )

        self.info_label.pack()

        display_frame = tk.LabelFrame(
            content,
            text="Stack Visualization",
            font=("Arial",12,"bold"),
            padx=10,
            pady=10
        )

        display_frame.grid(row=0,column=1,padx=20)

        self.display = tk.Text(
            display_frame,
            width=35,
            height=20,
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

        self.display.delete(1.0,tk.END)

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
                    f"┌─────────┐\n"
                    f"│ {item:^7} │\n"
                    f"└─────────┘\n"
                )

        self.info_label.config(
            text=f"Stack Size : {self.stack.size()}"
        )
    def check_delimiter(self):

        expression = self.entry.get()

        if expression == "":
            messagebox.showwarning(
                "Warning",
                "Please Enter an Expression"
            )
            return

        self.stack = Stack()

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        balanced = True

        for ch in expression:

            if ch in "([{":

                self.stack.push(ch)
                self.update_display()

            elif ch in ")]}":

                if self.stack.is_empty():
                    balanced = False
                    break

                top = self.stack.pop()
                self.update_display()

                if top != pairs[ch]:
                    balanced = False
                    break

        if not self.stack.is_empty():
            balanced = False

        self.update_display()

        if balanced:

            messagebox.showinfo(
                "Result",
                "Balanced Delimiters"
            )

        else:

            messagebox.showerror(
                "Result",
                "Not Balanced"
            )

        self.entry.delete(0, tk.END)


root = tk.Tk()

app = DelimiterGUI(root)

root.mainloop()

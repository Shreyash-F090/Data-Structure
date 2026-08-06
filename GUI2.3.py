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
            raise IndexError("Nothing to Undo")

        return self.items.pop()

    def size(self):
        return len(self.items)


class UndoGUI:

    def __init__(self, root):

        self.root = root
        self.stack = Stack()
        self.text = ""

        self.root.title("S091 Shreyash")
        self.root.state("zoomed")
        self.root.configure(bg="#DCEEFF")

        title = tk.Label(
            root,
            text="UNDO MECHANISM USING STACK",
            font=("Arial",24,"bold"),
            bg="#DCEEFF"
        )

        title.pack(pady=20)

        tk.Label(
            root,
            text="Enter Text",
            font=("Arial",14,"bold"),
            bg="#DCEEFF"
        ).pack()

        self.entry = tk.Entry(
            root,
            width=40,
            font=("Arial",14)
        )

        self.entry.pack(pady=10)

        button_frame = tk.Frame(root,bg="#DCEEFF")
        button_frame.pack(pady=10)

        tk.Button(
            button_frame,
            text="Add Text",
            width=15,
            height=2,
            command=self.add_text
        ).grid(row=0,column=0,padx=10)

        tk.Button(
            button_frame,
            text="Undo",
            width=15,
            height=2,
            command=self.undo_text
        ).grid(row=0,column=1,padx=10)

        tk.Button(
            button_frame,
            text="Exit",
            width=32,
            height=2,
            command=root.destroy
        ).grid(row=1,column=0,columnspan=2,pady=10)

        info_frame = tk.LabelFrame(
            root,
            text="Current Text",
            font=("Arial",12,"bold"),
            padx=20,
            pady=20
        )

        info_frame.pack(pady=20)

        self.text_display = tk.Text(
            info_frame,
            width=60,
            height=10,
            font=("Arial",14)
        )

        self.text_display.pack()

        self.update_display()


    def update_display(self):

        self.text_display.delete(1.0, tk.END)

        self.text_display.insert(
            tk.END,
            self.text
        )


    def add_text(self):

        new_text = self.entry.get()

        if new_text == "":
            messagebox.showwarning(
                "Warning",
                "Please Enter Text"
            )
            return

        self.stack.push(self.text)

        self.text += new_text

        self.entry.delete(0, tk.END)

        self.update_display()

        messagebox.showinfo(
            "Success",
            "Text Added Successfully"
        )


    def undo_text(self):

        try:

            self.text = self.stack.pop()

            self.update_display()

            messagebox.showinfo(
                "Undo",
                "Last Action Undone"
            )

        except IndexError as e:

            messagebox.showerror(
                "Error",
                str(e)
            )
            
root = tk.Tk()
app = UndoGUI(root)

root.mainloop()

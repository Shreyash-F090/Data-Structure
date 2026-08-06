import tkinter as tk
from tkinter import messagebox

class PriorityQueue:
    def __init__(self,maxcap):
        self.max=maxcap
        self.queue=[]

    def is_empty(self):
        return len(self.queue)==0

    def is_full(self):
        return len(self.queue)>=self.max

    def enqueue(self,item,priority):
        if self.is_full():
            return "Priority Queue is Full."
        self.queue.append((item,priority))
        self.queue.sort(key=lambda x:x[1])
        return f"Enqueued: {item} (Priority {priority})"

    def dequeue(self):
        if self.is_empty():
            return "Priority Queue is Empty."
        item=self.queue.pop(0)
        return f"Dequeued: {item[0]}"

    def traverse(self):
        if self.is_empty():
            return "Priority Queue is Empty."
        return "\n".join([f"Item: {i}  Priority: {p}" for i,p in self.queue])

    def ascending(self):
        return self.traverse()

    def descending(self):
        if self.is_empty():
            return "Priority Queue is Empty."
        return "\n".join([f"Item: {i}  Priority: {p}" for i,p in sorted(self.queue,key=lambda x:x[1],reverse=True)])

pq=None

root=tk.Tk()
root.title("Priority Queue - Shreyash Kadam S091")
root.geometry("600x600")

tk.Label(root,text="Priority Queue GUI",font=("Arial",16,"bold")).pack()

f=tk.Frame(root);f.pack(pady=5)
tk.Label(f,text="Max Size").grid(row=0,column=0)
maxe=tk.Entry(f,width=10);maxe.grid(row=0,column=1)

def create():
    global pq
    try:
        pq=PriorityQueue(int(maxe.get()))
        out("Priority Queue Created.")
    except:
        messagebox.showerror("Error","Enter valid maximum size")

tk.Button(f,text="Create Queue",command=create).grid(row=0,column=2,padx=5)

g=tk.Frame(root);g.pack(pady=5)
tk.Label(g,text="Item").grid(row=0,column=0)
iteme=tk.Entry(g,width=15);iteme.grid(row=0,column=1)
tk.Label(g,text="Priority").grid(row=0,column=2)
prie=tk.Entry(g,width=10);prie.grid(row=0,column=3)

text=tk.Text(root,width=65,height=18)
text.pack(pady=10)

def out(msg):
    text.delete("1.0",tk.END)
    text.insert(tk.END,msg)

def check():
    if pq is None:
        messagebox.showwarning("Queue","Create Queue First")
        return False
    return True

def enq():
    if not check(): return
    try:
        out(pq.enqueue(iteme.get(),int(prie.get())))
    except:
        messagebox.showerror("Error","Enter valid priority")

def deq():
    if check(): out(pq.dequeue())
def trav():
    if check(): out(pq.traverse())
def asc():
    if check(): out(pq.ascending())
def desc():
    if check(): out(pq.descending())
def isempty():
    if check(): out("Queue is Empty" if pq.is_empty() else "Queue is Not Empty")
def isfull():
    if check(): out("Queue is Full" if pq.is_full() else "Queue is Not Full")
def clear():
    text.delete("1.0",tk.END)

b=tk.Frame(root);b.pack()
for t,c in [("Enqueue",enq),("Dequeue",deq),("Traverse",trav),("Ascending",asc),("Descending",desc),("Check Empty",isempty),("Check Full",isfull),("Clear",clear),("Exit",root.destroy)]:
    tk.Button(b,text=t,width=15,command=c).pack(pady=2)

root.mainloop()

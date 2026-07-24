import os
import time
from colorama import Fore, Style, init

class Queue:
    def __init__(self, maxSize):
        self.queue = []
        self.maxSize = maxSize
        init(autoreset=True)

    def empty(self):
        return len(self.queue) == 0

    def isfull(self):
        return len(self.queue) == maxSize

    def enqueue(self, item):
        if self.isfull():
            print(Fore.RED + "Queue is not empty")
        else:
            self.queue.append(item)
            print(Fore.GREEN + f"Enqueued {item}")
            time.sleep(0.3)

    def dequeue(self):
        if self.empty():
            print(Fore.RED + "Queue is Empty")
            return none
        item = self.queue.pop(0)
        print(Fore.GREEN + f"Dequeued {item}")
        time.sleep(0.3)
        return item

    def peek(self):
        if self.empty():
            print(Fore.RED + "Queue is empty")
            return none
        print(Fore.GREEN + f"front of the queue is {self.queue[0]}")
        return self.queue[0]

    def traverse(self):
        if self.empty():
            print(Fore.RED + "Queue is empty")
        else:
            print(Fore.GREEN + "position of queue:", end="  ")
            for item in self.queue:
                print(Fore.CYAN + str(item), end=" ", flush=True)
                time.sleep(0.2)
            print()
        time.sleep(0.3)

    def displaylist(self):
        if self.empty():
            print(Fore.RED + "Queue is empty")
        else:
            print(Fore.BLUE + "Current Queue List")
            for index, item in  enumerate(self.queue):
                print(Fore.BLUE + f"{index + 1}. {item}")
                time.sleep(0.2)
        time.sleep(0.3)

def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    maxSize = int(input(Fore.YELLOW + "enter the maximum sze of the queue: "))
    q = Queue(maxSize)

    while True:
        clearscreen()
        print(Fore.MAGENTA + "=======Queue operation========")
        print(Fore.MAGENTA + "1. Enqueue")
        print(Fore.MAGENTA + "2. Dequeue")
        print(Fore.MAGENTA + "3. peek")
        print(Fore.MAGENTA + "4. Traverse")
        print(Fore.MAGENTA + "5. Display list")
        print(Fore.MAGENTA + "6. Check if Queue is empty")
        print(Fore.MAGENTA + "7. Check if Queue is full")
        print(Fore.MAGENTA + "8. Exit")
        choice = input(Fore.YELLOW + "Enter your choice")

        if choice == '1':
            item = input(Fore.YELLOW + "Enter the item to enqueue: ")
            q.enqueue(item)
        elif choice == '2':
            q.dequeue()
        elif choice == '3':
            q.peek()
        elif choice == '4':
            q.traverse()
        elif choice == '5':
            q.displaylist()
        elif choice == '6':
            if q.empty():
                print(Fore.RED + "Queue is empty.")
            else:
                print(Fore.GREEN + "Queue is not empty.")
        elif choice == '7':
            if q.isfull():
                print(Fore.RED + "Queue is full.")
            else:
                print(Fore.GREEN + "Queue is not full.")
        elif choice == '8':
            break
        else:
            print(Fore.RED + "Invalid choice! Please try again.")
        input(Fore.GREEN + "Press Enter to continue...")

clearscreen()
print(Fore.MAGENTA + "Exiting the program. Goodbye!")

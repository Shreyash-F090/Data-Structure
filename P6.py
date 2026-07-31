from colorama import init, Fore, Style
import time
init()

class S091_priorityQ:
    def __init__(self, maxcapacity):
        self.queue = []
        self.maxcapacity = maxcapacity


    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) >= self.maxcapacity

    def enqueue(self, item, priority):
        if self.is_full():
            print(Fore.RED + "Priority Queue is full. Cannot enqueue." + Style.RESET_ALL)
            return
        self.queue.append((item, priority))
        self.queue.sort(key=lambda x:x[1])
        print(Fore.GREEN + f"Enqueued: {item} with priority: {priority}" + Style.RESET_ALL)
        self.loading_animation()

    def dequeue(self):
        if self.is_empty():
            print(Fore.RED + "Priority Queue is empty. Cannot Dequeue." + Style.RESET_ALL)
            return None
        item = self.queue.pop(0)[0]
        print(Fore.GREEN + f"Dequeued:{item}." + Style.RESET_ALL)
        self.loading_animation()
        return item

    def traverse(self):
        if self.is_empty():
            print(Fore.YELLOW + "Priority Queue is empty." + Style.RESET_ALL)
        else:
            print(Fore.CYAN + "Priority Queue contains:" + Style.RESET_ALL)
            for item, priority in self.queue:
                print(Fore.CYAN + f"Item: {item}, Priority: {priority}" + Style.RESET_ALL)

    def show_ascending(self):
        if self.is_empty():
            print(Fore.YELLOW + "Priority Queue is empty." + Style.RESET_ALL)
        else:
            print(Fore.CYAN + "Priority Queue in ascending order:" + Style.RESET_ALL)
            for item, priority in sorted(self.queue, key=lambda x: x[1]):
                print(Fore.CYAN + f"Item: {item}, Priority: {priority}" + Style.RESET_ALL)

    def show_descending(self):
        if self.is_empty():
            print(Fore.YELLOW + "Priority Queue is empty." + Style.RESET_ALL)
        else:
            print(Fore.CYAN + "Priority Queue in descending order:" + Style.RESET_ALL)
            for item, priority in sorted(self.queue, key=lambda x: x[1], reverse=True):
                print(Fore.CYAN + f"Item: {item}, Priority: {priority}" + Style.RESET_ALL)
    def loading_animation(self):
        for _ in range(3):
            for ch in ['-', '\\', '|', '/']:
                print(Fore.BLUE + f'\rLoading {ch}' + Style.RESET_ALL, end='', flush=True)
                time.sleep(0.1)
        print('\r' + ' ' * 20 + '\r', end='', flush=True)

def Main():
    while True:
        try:
            maxcapacity = int(input("Enter the maximum capacity of the Priority Queue: "))
            break
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter an integer value." + Style.RESET_ALL)

    pq = S091_priorityQ(maxcapacity)

    while True:
        print(Fore.RED + "Shreyash Kadam S091" + Style.RESET_ALL)
        print(Fore.YELLOW + "\nPriority Queue Menu:" + Style.RESET_ALL)
        print(Fore.YELLOW + "1. Enqueue" + Style.RESET_ALL)
        print(Fore.YELLOW + "2. Dequeue" + Style.RESET_ALL)
        print(Fore.YELLOW + "3. Traverse" + Style.RESET_ALL)
        print(Fore.YELLOW + "4. Check if Empty" + Style.RESET_ALL)
        print(Fore.YELLOW + "5. Check if Full" + Style.RESET_ALL)
        print(Fore.YELLOW + "6. Show Ascending Order" + Style.RESET_ALL)
        print(Fore.YELLOW + "7. Show Descending Order" + Style.RESET_ALL)
        print(Fore.YELLOW + "8. Exit" + Style.RESET_ALL)

        try:
            choice = int(input(Fore.BLUE + "Enter your choice: " + Style.RESET_ALL))
        except ValueError:
            print(Fore.RED + "Invalid choice. Please enter a number between 1 and 8." + Style.RESET_ALL)
            continue

        if choice == 1:
            item = input(Fore.BLUE + "Enter item to enqueue: " + Style.RESET_ALL)
            try:
                priority = int(input(Fore.BLUE + "Enter priority: " + Style.RESET_ALL))
                pq.enqueue(item, priority)
            except ValueError:
                print(Fore.RED + "Invalid priority. Please enter an integer value." + Style.RESET_ALL)
        elif choice == 2:
            pq.dequeue()
        elif choice == 3:
            pq.traverse()
        elif choice == 4:
            if pq.is_empty():
                print(Fore.CYAN + "Priority Queue is empty." + Style.RESET_ALL)
            else:
                print(Fore.CYAN + "Priority Queue is not empty." + Style.RESET_ALL)
        elif choice == 5:
            if pq.is_full():
                print(Fore.CYAN + "Priority Queue is full." + Style.RESET_ALL)
            else:
                print(Fore.CYAN + "Priority Queue is not full." + Style.RESET_ALL)
        elif choice == 6:
            pq.show_ascending()
        elif choice == 7:
            pq.show_descending()
        elif choice == 8:
            print(Fore.RED + "Exiting..." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)

if __name__ == "__main__":
    Main()


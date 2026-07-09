import os
import time
from termcolor import colored, cprint


class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        print(colored("State Saved.", "green"))
        self.animate_save()

    def pop(self):
        if self.is_empty():
            raise IndexError("Nothing to Undo")

        item = self.items.pop()

        print(colored("Undo Successful.", "red"))
        self.animate_undo()

        return item

    def animate_save(self):
        for _ in range(3):
            print(colored("Saving Current State...", "yellow"))
            time.sleep(0.4)
            self.clear_screen()

    def animate_undo(self):
        for _ in range(3):
            print(colored("Undoing Last Action...", "magenta"))
            time.sleep(0.4)
            self.clear_screen()

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')


def undo_program():

    stack = Stack()
    text = ""

    cprint("Undo Mechanism Using Stack", "cyan", attrs=["bold"])

    while True:

        print("\nCurrent Text :", colored(text, "blue"))

        print(colored("1. Add Text", "yellow"))
        print(colored("2. Undo", "yellow"))
        print(colored("3. Exit", "yellow"))

        try:
            choice = int(input(colored("Enter Choice (1-3): ", "green")))

        except ValueError:
            cprint("Invalid Input!", "red")
            continue

        if choice == 1:

            stack.push(text)

            new_text = input(colored("Enter Text: ", "green"))

            text += new_text

        elif choice == 2:

            try:
                text = stack.pop()

            except IndexError as e:
                cprint(str(e), "red")

        elif choice == 3:

            cprint("Exiting Program...", "cyan", attrs=["bold"])
            break

        else:

            cprint("Invalid Choice!", "red")


if __name__ == "__main__":
    undo_program()

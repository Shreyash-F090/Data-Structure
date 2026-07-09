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
        print(colored(f"'{item}' pushed into stack.", "green"))
        self.animate_push(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is Empty")

        item = self.items.pop()

        print(colored(f"'{item}' popped from stack.", "red"))
        self.animate_pop(item)

        return item

    def animate_push(self, item):
        for _ in range(3):
            print(colored(f"Pushing {item}...", "yellow"))
            time.sleep(0.4)
            self.clear_screen()

    def animate_pop(self, item):
        for _ in range(3):
            print(colored(f"Popping {item}...", "magenta"))
            time.sleep(0.4)
            self.clear_screen()

    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")


def delimiter_matching(expression):

    stack = Stack()

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in expression:

        if ch in "([{":
            stack.push(ch)

        elif ch in ")]}":

            if stack.is_empty():
                return False

            top = stack.pop()

            if top != pairs[ch]:
                return False

    return stack.is_empty()


def main():

    cprint("Delimiter Matching Program", "cyan", attrs=["bold"])

    expression = input(colored("Enter an Expression: ", "green"))

    if delimiter_matching(expression):

        cprint("\nBalanced Delimiters", "green", attrs=["bold"])

    else:

        cprint("\nNot Balanced", "red", attrs=["bold"])


if __name__ == "__main__":
    main()

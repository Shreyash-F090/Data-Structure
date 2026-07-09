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
        print(colored(f"Pushed '{item}' into stack.", "green"))
        self.animate_push(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is Empty")

        item = self.items.pop()

        print(colored(f"Popped '{item}' from stack.", "red"))
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
        os.system('cls' if os.name == 'nt' else 'clear')


def is_operator(ch):
    return ch in "+-*/^"


def prefix_to_postfix(expression):

    stack = Stack()

    expression = expression[::-1]

    for ch in expression:

        if ch.isalnum():

            stack.push(ch)

        elif is_operator(ch):

            op1 = stack.pop()
            op2 = stack.pop()

            new_expression = op1 + op2 + ch

            stack.push(new_expression)

    return stack.pop()


def main():

    cprint("Prefix to Postfix Conversion", "cyan", attrs=["bold"])

    prefix = input(colored("Enter Prefix Expression: ", "green"))

    try:

        postfix = prefix_to_postfix(prefix)

        cprint("\nPostfix Expression : " + postfix, "blue", attrs=["bold"])

    except IndexError:

        cprint("Invalid Prefix Expression!", "red")


if __name__ == "__main__":
    main()

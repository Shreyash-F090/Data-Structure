import tkinter as tk
from tkinter import messagebox
import heapq
from collections import Counter


class Node:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanCoding:

    def __init__(self):
        self.codebook = {}
        self.root = None
        self.frequencies = {}

    def build_huffman_tree(self, frequencies, output):
        heap = [Node(char, freq) for char, freq in frequencies.items()]
        heapq.heapify(heap)

        output.insert(tk.END, "\nStarting Huffman Tree Construction...\n")
        output.insert(tk.END, "-" * 55 + "\n")

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)

            left_char = str(left.char) if left.char is not None else "None"
            right_char = str(right.char) if right.char is not None else "None"

            output.insert(
                tk.END,
                f"Merging nodes: {left_char} ({left.freq}) "
                f"and {right_char} ({right.freq})\n"
            )

            merged = Node(freq=left.freq + right.freq)
            merged.left = left
            merged.right = right

            heapq.heappush(heap, merged)

        self.root = heap[0]

    def generate_codes(self, node, prefix="", output=None):
        if node is None:
            return

        if node.char is not None:
            code = prefix if prefix != "" else "0"
            self.codebook[node.char] = code

            if output:
                output.insert(
                    tk.END,
                    f"Assigning code to character {node.char}: {code}\n"
                )

        self.generate_codes(node.left, prefix + "0", output)
        self.generate_codes(node.right, prefix + "1", output)

    def encode(self, data):
        return "".join(self.codebook[char] for char in data)

    def decode(self, encoded_data, output):
        reverse_codebook = {
            value: key for key, value in self.codebook.items()
        }

        decoded_data = ""
        current_code = ""

        output.insert(tk.END, "\nStarting Huffman Decoding...\n")
        output.insert(tk.END, "-" * 55 + "\n")

        for bit in encoded_data:
            current_code += bit

            if current_code in reverse_codebook:
                character = reverse_codebook[current_code]

                output.insert(
                    tk.END,
                    f"Decoding: {current_code} -> {character}\n"
                )

                decoded_data += character
                current_code = ""

        return decoded_data

    def huffman_encoding(self, data, output):
        self.frequencies = Counter(data)

        output.insert(tk.END, "\nCharacter Frequencies:\n")
        output.insert(tk.END, "-" * 55 + "\n")

        for char, frequency in self.frequencies.items():
            display_char = "[SPACE]" if char == " " else char

            output.insert(
                tk.END,
                f"{display_char}: {frequency}\n"
            )

        self.build_huffman_tree(self.frequencies, output)

        output.insert(tk.END, "\nGenerating Huffman Codes...\n")
        output.insert(tk.END, "-" * 55 + "\n")

        self.codebook = {}

        self.generate_codes(
            self.root,
            "",
            output
        )

        encoded_data = self.encode(data)

        return encoded_data


def start_encoding():
    data = input_text.get("1.0", tk.END).rstrip("\n")

    if data == "":
        messagebox.showwarning(
            "Input Required",
            "Please enter text to encode."
        )
        return

    output.delete("1.0", tk.END)

    output.insert(
        tk.END,
        "Welcome to Huffman Coding GUI Application!\n"
    )

    output.insert(
        tk.END,
        "=" * 65 + "\n"
    )

    output.insert(
        tk.END,
        f"Input Text: {data}\n"
    )

    output.insert(
        tk.END,
        "\nStarting Huffman Encoding...\n"
    )

    huffman = HuffmanCoding()

    encoded_data = huffman.huffman_encoding(
        data,
        output
    )

    output.insert(
        tk.END,
        "\nEncoding completed!\n"
    )

    output.insert(
        tk.END,
        "\nCodebook:\n"
    )

    output.insert(
        tk.END,
        "-" * 55 + "\n"
    )

    for char, code in huffman.codebook.items():
        display_char = "[SPACE]" if char == " " else char

        output.insert(
            tk.END,
            f"{display_char}: {code}\n"
        )

    output.insert(
        tk.END,
        "\nEncoded Data:\n"
    )

    output.insert(
        tk.END,
        encoded_data + "\n"
    )

    decoded_data = huffman.decode(
        encoded_data,
        output
    )

    output.insert(
        tk.END,
        "\nDecoding completed!\n"
    )

    output.insert(
        tk.END,
        "\nOriginal Data:\n"
    )

    output.insert(
        tk.END,
        data + "\n"
    )

    output.insert(
        tk.END,
        "\nDecoded Data:\n"
    )

    output.insert(
        tk.END,
        decoded_data + "\n"
    )

    output.insert(
        tk.END,
        "\n" + "=" * 65 + "\n"
    )

    if data == decoded_data:
        output.insert(
            tk.END,
            "Success: The original and decoded data match!\n"
        )
    else:
        output.insert(
            tk.END,
            "Error: The original and decoded data do not match!\n"
        )

    output.see(tk.END)


def clear_output():
    input_text.delete(
        "1.0",
        tk.END
    )

    output.delete(
        "1.0",
        tk.END
    )


def exit_program():
    root.destroy()


root = tk.Tk()

root.title(
    "P7GUI - Huffman Coding - Shreyash Kadam S091"
)

root.geometry(
    "900x750"
)

root.resizable(
    True,
    True
)

title = tk.Label(
    root,
    text="HUFFMAN CODING",
    font=("Arial", 22, "bold")
)

title.pack(
    pady=10
)

student = tk.Label(
    root,
    text="Shreyash Kadam S091",
    font=("Arial", 12)
)

student.pack(
    pady=2
)

input_frame = tk.Frame(
    root
)

input_frame.pack(
    pady=10
)

input_label = tk.Label(
    input_frame,
    text="Enter the text to encode:",
    font=("Arial", 12, "bold")
)

input_label.pack()

input_text = tk.Text(
    input_frame,
    height=4,
    width=80,
    font=("Arial", 12)
)

input_text.pack(
    pady=5
)

button_frame = tk.Frame(
    root
)

button_frame.pack(
    pady=10
)

encode_button = tk.Button(
    button_frame,
    text="Start Huffman Coding",
    width=22,
    height=2,
    command=start_encoding
)

encode_button.grid(
    row=0,
    column=0,
    padx=5
)

clear_button = tk.Button(
    button_frame,
    text="Clear",
    width=15,
    height=2,
    command=clear_output
)

clear_button.grid(
    row=0,
    column=1,
    padx=5
)

exit_button = tk.Button(
    button_frame,
    text="Exit",
    width=15,
    height=2,
    command=exit_program
)

exit_button.grid(
    row=0,
    column=2,
    padx=5
)

output_label = tk.Label(
    root,
    text="Huffman Coding Process:",
    font=("Arial", 12, "bold")
)

output_label.pack(
    pady=5
)

output_frame = tk.Frame(
    root
)

output_frame.pack(
    fill=tk.BOTH,
    expand=True,
    padx=15,
    pady=5
)

scrollbar = tk.Scrollbar(
    output_frame
)

scrollbar.pack(
    side=tk.RIGHT,
    fill=tk.Y
)

output = tk.Text(
    output_frame,
    width=90,
    height=30,
    font=("Courier New", 11),
    yscrollcommand=scrollbar.set
)

output.pack(
    side=tk.LEFT,
    fill=tk.BOTH,
    expand=True
)

scrollbar.config(
    command=output.yview
)

root.mainloop()

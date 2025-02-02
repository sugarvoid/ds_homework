"""
Name:         David Durham
Week:         2
Project:      4.2
Description:  This program accepts input and will check if it is a palindrome.
"""

import tkinter as tk
import tkinter.font as tkFont
from classes import Stack


def update_label_text(label: tk.Entry, new_str: str) -> None:
    label.config(text=new_str)


def check_input(event: tk.Event = None) -> None:
    _stack = Stack(100)
    # Get the text from the txt_input box
    _item = txt_input.get()

    # Make sure something was entered
    if _item:
        # Loop over letters in word
        for char in _item:
            # Make sure char is a letter a-z
            if char.isalpha():
                # Remove whitespace and normalize the case of letters
                _stack.push(char.strip().lower())
                txt_input.delete(0, tk.END)
                if _stack.get_stack_str() == _stack.get_reverse():
                    update_label_text(lbl_feedback, "Input is a palindrome")
                else:
                    update_label_text(lbl_feedback, "Input is not a palindrome")
    else:
        update_label_text(lbl_feedback, "Please enter some text")
    txt_input.focus()


# Set up GUI
root = tk.Tk()
root.title("Palindrome Checker")

normal_font = tkFont.Font(family="Helvetica", size=14, weight=tkFont.NORMAL)

lbl_instruction = tk.Label(root, text="Enter Text", font=normal_font)
lbl_instruction.pack(pady=10, padx=10)

lbl_feedback = tk.Label(root, text="", font=normal_font)
lbl_feedback.pack(pady=10, padx=10)

txt_input = tk.Entry(root, font=normal_font)
txt_input.pack(pady=10, padx=10)

btn_check = tk.Button(root, text="Check", command=check_input)
btn_check.pack(pady=5)

root.bind("<Return>", check_input)
root.bind("<KP_Enter>", check_input)

# Start GUI
root.mainloop()

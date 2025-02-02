import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox 
from classes import Stack



#determines whether an input string is a palindrome or not, ignoring whitespace, digits, punctuation, and the case of letters


root = tk.Tk()
root.title("palindrome Checker")

normal_font = tkFont.Font(family="Helvetica", size=14, weight=tkFont.NORMAL)


lbl_instruction = tk.Label(root, text="Enter Word", font=normal_font)
lbl_instruction.pack(pady=10)

lbl_feedback = tk.Label(root, text="", font=normal_font)
lbl_feedback.pack(pady=10)


def check_input():
    stack = Stack(100) 
    # Get the text from the txt_input box
    _item = txt_input.get()  
    
    # Make sure something was entered
    if _item:  
        # Loop over letters in word
        for char in _item:
            # Make sure char is a letter a-z
            if char.isalpha(): 
                # Remove whitespace and normalize the case of letters
                stack.push(char.strip().lower())
                txt_input.delete(0, tk.END)  
    
    print(stack.get_stack_str() == stack.get_reverse())
    

    print(f"The reverse is: {stack.get_reverse()}")
    update_label_text( lbl_feedback,f"The reverse is: {stack.get_reverse()}")

def update_label_text(label: tk.Entry,new_str: str) -> None:
    label.config(text=new_str) 


txt_input = tk.Entry(root, font=("Arial", 16))
txt_input.pack(pady=10)

btn_check = tk.Button(root, text="Check", command=check_input)
btn_check.pack()

root.mainloop()






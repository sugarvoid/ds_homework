import tkinter as tk
from tkinter import messagebox 
from classes import Stack


root = tk.Tk()
root.title("Homework Thing")

lbl_instruction = tk.Label(root, text="Enter Word", font=("Arial", 14))
lbl_instruction.pack(pady=10)

lbl_feedback = tk.Label(root, text="", font=("Arial", 14))
lbl_feedback.pack(pady=10)


def check_input():
    stack = Stack(100) 
    # Get the text from the txt_input box
    _item = txt_input.get()  
    
    # Make sure something was entered
    if _item:  
        # Loop over letters in word
        for letter in _item: 
            stack.push(letter)
            txt_input.delete(0, tk.END)  
    
    _reverse = stack.get_reverse()

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






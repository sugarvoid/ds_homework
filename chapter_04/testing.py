import tkinter as tk

class Stack:
    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size

    def push(self, item):
        if len(self.stack) < self.max_size:
            self.stack.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        return None

    def isEmpty(self):
        return len(self.stack) == 0

    def __str__(self):
        return str(self.stack)

# Create the main window
root = tk.Tk()
root.title("Stack Display")

# Create a stack and push some items
stack = Stack(5)
for word in ['May', 'the', 'force', 'be', 'with', 'you']:
    stack.push(word)

# Create a label to display the stack
stack_label = tk.Label(root, text="Stack contents: " + str(stack), font=("Arial", 14))
stack_label.pack(pady=20)

# Function to update the label after a pop operation
def pop_from_stack():
    if not stack.isEmpty():
        stack.pop()
        stack_label.config(text="Stack contents: " + str(stack))  # Update the label

# Function to update the label after a pop operation
def push_to_stack():
    if not stack.isEmpty():
        stack.pop()
        stack_label.config(text="Stack contents: " + str(stack))  # Update the label

# Button to pop an item from the stack
pop_button = tk.Button(root, text="Pop item", command=pop_from_stack)
pop_button.pack()

# Start the Tkinter event loop
root.mainloop()

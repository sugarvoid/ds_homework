# David Durham
# Week 2
# Projects 4.1


from classes import Stack


stack = Stack(12)
#stack.pop()

for word in ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']:
    stack.push(word)
print('After pushing', len(stack), 'words on the stack, it contains:\n', stack)
print('Is stack full?', stack.isFull())


stack.push("eleven")




print('Popping items off the stack:')
while not stack.isEmpty():
    print(stack.pop(), end=' ')
print()


stack = Stack(100) # Create a stack to hold letters
word = input("Word to reverse: ")
for letter in word: # Loop over letters in word
    if not stack.isFull(): # Push letters on stack if not full
        stack.push(letter)
reverse = '' # Build the reversed version
while not stack.isEmpty(): # by popping the stack until empty
    reverse += stack.pop()
print('The reverse of', word, 'is', reverse)
